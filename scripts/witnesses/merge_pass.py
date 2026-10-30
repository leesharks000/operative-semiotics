#!/usr/bin/env python3
"""merge_pass.py — merge a reader pass into the witness record (2026-10-30).

Reads the readers' outputs (out-<THEME>.json) and the quote checks verify_quotes.py wrote beside them (<file>.quotes.json). For each
witness, keeps only the quotes found at source; a witness with no quote found at source becomes a candidate (its quotes recorded as not
found). Witnesses with the same source (DOI or first URL) and the same direction are merged into one, their claim links joined; a source
recorded in both directions stays two witnesses, one per direction (the protocol: a witness carries one direction). New ids continue
the record (W-, S-, C-). Each reader's searches become one search record; the quote check is recorded as its own search record.
Appends to data/witnesses/witnesses.json and searches.json; the raw reader outputs are kept under data/witnesses/passes/<date>/.
    python3 scripts/witnesses/merge_pass.py <date> <out-file> [<out-file> ...]"""
import json, pathlib, shutil, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
W = ROOT / 'data/witnesses'


def key(w):
    s = w['source']
    return (s.get('doi') or (s.get('urls') or [''])[0] or s.get('title', '')).lower().rstrip('/').replace('https://doi.org/', ''), w['direction']


def main(date, files):
    wd = json.load(open(W / 'witnesses.json')); sd = json.load(open(W / 'searches.json'))
    claims = {c['id'] for c in json.load(open(ROOT / 'data/reading/triage/claims.json'))['claims']}
    nw = max(int(x['id'][2:]) for x in wd['witnesses']) + 1
    ns = max(int(x['id'][2:]) for x in sd['searches']) + 1
    cands_all = [c for s in sd['searches'] for c in (s.get('outcome') or {}).get('candidates') or []]
    nc = max([int(c['id'][2:]) for c in cands_all if c.get('id')] + [0]) + 1
    have = {key(x): x for x in wd['witnesses']}
    pdir = W / 'passes' / date; pdir.mkdir(parents=True, exist_ok=True)
    qcheck = {'id': None, 'date': date, 'by': 'Claude (Opus 5.5), in session: scripts/witnesses/verify_quotes.py',
              'aimed_at': 'every quote the readers returned, checked against the text of its source pages and the publisher records of its DOIs',
              'method': 'verify_quotes.py: pages fetched with the archive\'s own agent; PDFs read through pdftotext; Crossref and the medRxiv/bioRxiv API for DOIs; a quote kept only if found verbatim (whitespace, typographic quotes and dashes normalized).',
              'queries': [], 'outcome': {'quotes_verified': 0, 'quotes_dropped': [], 'witnesses_demoted_to_candidates': []}}
    added, merged, demoted, new_searches = [], [], [], []
    for f in files:
        f = pathlib.Path(f); o = json.load(open(f)); q = json.load(open(str(f) + '.quotes.json'))
        shutil.copy(f, pdir / f.name); shutil.copy(str(f) + '.quotes.json', pdir / (f.name + '.quotes.json'))
        ok = {(r['witness'], r['quote']) for r in q if r['state'] == 'verified'}
        sid = f'S-{ns:04d}'; ns += 1
        rec = {'id': sid, 'date': date, 'by': f'intake reader, theme {o["theme"]}, in session (brief: data/witnesses/passes/{date}/BRIEF.md)',
               'aimed_at': f'the forecasts and unbuilt tests of theme {o["theme"]} (claims list: data/witnesses/passes/{date}/claims-{o["theme"]}.json)',
               'method': 'WebSearch and WebFetch only, the readers\' own account per query; every quote then checked at source by the record that follows this pass\'s readers.',
               'queries': o.get('searches', []), 'outcome': {'witnesses': [], 'candidates': [], 'notes': o.get('notes')}}
        for w in o.get('witnesses', []):
            fq = [x for x in w.get('finding', []) if (w['id'], x['quote']) in ok]
            drop = [x['quote'] for x in w.get('finding', []) if (w['id'], x['quote']) not in ok]
            qcheck['outcome']['quotes_verified'] += len(fq)
            qcheck['outcome']['quotes_dropped'] += [{'reader_id': w['id'], 'quote': d} for d in drop]
            links = [l for l in w.get('claims', []) if l.get('claim') in claims]
            if not fq or not links:
                c = {'id': f'C-{nc:04d}', 'source': w['source'].get('title'), 'url': (w['source'].get('urls') or [None])[0],
                     'claims': [l.get('claim') for l in w.get('claims', [])], 'reader_id': w['id'],
                     'state': 'no quote found at source by verify_quotes.py' if not fq else 'no claim of the index matched'}
                nc += 1; rec['outcome']['candidates'].append(c); demoted.append(w['id']); qcheck['outcome']['witnesses_demoted_to_candidates'].append(w['id'])
                continue
            ch = dict(w.get('checked') or {})
            ch = {'by': f'intake reader, theme {o["theme"]}; quotes checked at source by scripts/witnesses/verify_quotes.py', 'date': date,
                  'how': ch.get('how', ''), 'unverified': (ch.get('unverified') or []) + [f'quote not found at source, dropped: "{d}"' for d in drop]}
            k = key(w)
            if k in have:
                x = have[k]
                x['claims'] += [l for l in links if l['claim'] not in {y['claim'] for y in x['claims']}]
                x['finding'] += [y for y in fq if y['quote'] not in {z['quote'] for z in x['finding']}]
                x.setdefault('found_by', []).append(sid); x['checked']['unverified'] += ch['unverified']
                merged.append((w['id'], x['id'])); rec['outcome']['witnesses'].append(x['id'])
                continue
            nwid = f'W-{nw:04d}'; nw += 1
            x = {'id': nwid, 'direction': w['direction'], 'evidence_class': w['evidence_class'], 'claims': links, 'source': w['source'],
                 'versions': w.get('versions', []), 'finding': fq, 'shows': w.get('shows'), 'does_not_show': w.get('does_not_show'),
                 'checked': ch, 'found_by': [sid], 'reader_id': w['id']}
            wd['witnesses'].append(x); have[k] = x; added.append(nwid); rec['outcome']['witnesses'].append(nwid)
        for c in o.get('candidates', []):
            rec['outcome']['candidates'].append({'id': f'C-{nc:04d}', **c}); nc += 1
        new_searches.append(rec)
    qcheck['id'] = f'S-{ns:04d}'
    sd['searches'] += new_searches + [qcheck]
    for x in (W / '..' / '..').resolve().glob('nothing'):
        pass
    json.dump(wd, open(W / 'witnesses.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(sd, open(W / 'searches.json', 'w'), ensure_ascii=False, indent=1)
    print(f'added {len(added)} witnesses ({added[0] if added else "-"}–{added[-1] if added else "-"}); merged {len(merged)} into existing; demoted {len(demoted)} to candidates; '
          f'searches {", ".join(s["id"] for s in new_searches)} + quote check {qcheck["id"]}; quotes verified {qcheck["outcome"]["quotes_verified"]}, dropped {len(qcheck["outcome"]["quotes_dropped"])}')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
