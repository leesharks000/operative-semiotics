#!/usr/bin/env python3
"""verify_quotes.py — check each witness's quoted finding against the text of its source pages (2026-10-30).

For every witness in the given file (default data/witnesses/witnesses.json), fetch each of its source URLs once, with the archive's own
user agent, and the publisher's record of each DOI it names (Crossref's abstract; for medRxiv and bioRxiv DOIs, the server's own record
of every version's abstract), reduce each to text (tags dropped, entities decoded, whitespace and typographic quotes and dashes normalized), and look
for every quote. A quote is `verified` when it is found on one of the pages, `not found` when every page was read and none carries it,
and `unreachable` when no page could be read (a refusal is recorded with its status). Writes the result as JSON beside the input
(<input>.quotes.json) and prints a line per quote. It does not edit the witnesses.
    python3 scripts/witnesses/verify_quotes.py [witnesses.json]"""
import html, json, pathlib, re, sys, urllib.request
UA = "alexanarch-seating/1.0 (https://www.alexanarch.org)"
ROOT = pathlib.Path(__file__).resolve().parents[2]


def norm(s):
    s = html.unescape(s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace(' ', ' ')
    s = s.replace('­', '').replace('ﬁ', 'fi').replace('ﬂ', 'fl')
    return re.sub(r'\s+', ' ', s).strip().lower()


_cache = {}
def page(url):
    if url in _cache:
        return _cache[url]
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=40)
        body = r.read()
        if body[:5] == b'%PDF-' or 'pdf' in (r.headers.get('Content-Type') or ''):   # a PDF is read through pdftotext
            import subprocess, tempfile
            with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
                f.write(body); f.flush()
                raw = subprocess.run(['pdftotext', '-layout', f.name, '-'], capture_output=True, text=True).stdout
            txt = norm(re.sub(r'-\n\s*', '', raw))
        else:
            raw = body.decode('utf-8', 'replace')
            txt = norm(re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', ' ', raw, flags=re.S)))
        _cache[url] = ('ok', txt)
    except Exception as e:
        _cache[url] = ('refused', str(getattr(e, 'code', '') or e)[:80])
    return _cache[url]


def doi_texts(w):
    """The DOIs a witness names (source.doi, doi.org URLs, and medRxiv/bioRxiv content URLs) -> their abstracts as recorded by Crossref and,
    for 10.1101/10.64898, by the server's API."""
    ds = set()
    if w['source'].get('doi'):
        ds.add(w['source']['doi'])
    for u in (w['source'].get('urls') or []) + [v.get('url') or '' for v in w.get('versions') or []]:
        m = re.search(r'doi\.org/(10\.[^\s?#]+)', u or '') or re.search(r'(?:medrxiv|biorxiv)\.org/content/(10\.\d+/[0-9.]+)', u or '')
        if m:
            ds.add(re.sub(r'v\d+$', '', m.group(1)))
    out = []
    for d in sorted(ds):
        out.append(f'https://api.crossref.org/works/{d}')
        if d.startswith(('10.1101/', '10.64898/')):
            out.append(f'https://api.biorxiv.org/details/medrxiv/{d}')
            out.append(f'https://api.biorxiv.org/details/biorxiv/{d}')
    return out


def main(path):
    W = json.load(open(path))
    W = W['witnesses'] if isinstance(W, dict) else W
    out = []
    for w in W:
        urls = list(dict.fromkeys((w['source'].get('urls') or []) + [v['url'] for v in w.get('versions') or [] if v.get('url')] + doi_texts(w)))
        for f in w.get('finding') or []:
            q = norm(f['quote']); state, where, refused = 'unreachable', None, []
            for u in urls:
                s, t = page(u)
                if s != 'ok':
                    refused.append(f'{u} ({t})'); continue
                if q in t:
                    state, where = 'verified', u; break
                state = 'not found'
            out.append({'witness': w['id'], 'quote': f['quote'], 'state': state, 'where': where, 'refused': refused})
            print(f"  {w['id']} {state:11} {f['quote'][:70]!r}" + (f'  [{where}]' if where else ''))
    p = pathlib.Path(str(path) + '.quotes.json')
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
    c = {k: sum(1 for o in out if o['state'] == k) for k in ('verified', 'not found', 'unreachable')}
    print('quotes:', c, '->', p)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'data/witnesses/witnesses.json')
