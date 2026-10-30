#!/usr/bin/env python3
"""check_witnesses.py — check the external witnesses of the prediction index and compute their order (2026-10-30).

Protocol: data/witnesses/WITNESS-PROTOCOL.md (adopted by Lee Sharks, 2026-10-30). Refuses a witness whose claims do not exist, whose
class, direction or bears_on is outside the vocabulary, or which lacks a source, a dated version or a quoted finding; refuses a search
whose witness or candidate references do not resolve. Prints each witness's order per claim: after, before (an anticipation) or
undetermined. Writes nothing.
    python3 scripts/witnesses/check_witnesses.py"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
W = ROOT / 'data/witnesses'


def order(registered, versions):
    """after | before | undetermined, from the claim's registered date and the earliest dated version (YYYY, YYYY-MM or YYYY-MM-DD)."""
    ds = sorted(v['date'] for v in versions if v.get('date'))
    if not ds or not registered:
        return 'undetermined', None
    first = ds[0]
    n = min(len(first), len(registered))
    a, b = first[:n], registered[:n]
    if a == b:
        return ('undetermined' if len(first) < 10 else 'same day'), first
    return ('after' if a > b else 'before'), first


def check():
    claims = {c['id']: c for c in json.load(open(ROOT / 'data/reading/triage/claims.json'))['claims']}
    wd = json.load(open(W / 'witnesses.json')); sd = json.load(open(W / 'searches.json'))
    bad, rows = [], []
    ids = set()
    for w in wd['witnesses']:
        i = w.get('id'); ids.add(i)
        if w.get('evidence_class') not in wd['evidence_classes']:
            bad.append((i, 'evidence_class', w.get('evidence_class')))
        if w.get('direction') not in wd['directions']:
            bad.append((i, 'direction', w.get('direction')))
        if not (w.get('source') or {}).get('title') or not ((w['source'].get('urls') or w['source'].get('doi'))):
            bad.append((i, 'source needs a title and a URL or DOI'))
        if not any(v.get('date') for v in w.get('versions') or []):
            bad.append((i, 'no dated version'))
        if not any((f.get('quote') or '').strip() for f in w.get('finding') or []):
            bad.append((i, 'no quoted finding'))
        for k in ('shows', 'does_not_show', 'checked'):
            if not w.get(k):
                bad.append((i, 'missing ' + k))
        for c in w.get('claims') or []:
            if c.get('claim') not in claims:
                bad.append((i, 'no such claim', c.get('claim'))); continue
            if c.get('bears_on') not in wd['bears_on']:
                bad.append((i, 'bears_on', c.get('bears_on')))
            if not c.get('scope'):
                bad.append((i, c['claim'], 'no scope'))
            o, first = order(claims[c['claim']]['registered'], w['versions'])
            rows.append((i, c['claim'], claims[c['claim']]['registered'], first, o, w['direction'], w['evidence_class']))
        if not w.get('claims'):
            bad.append((i, 'no claims'))
    sids = {s['id'] for s in sd['searches']}
    for s in sd['searches']:
        for x in (s.get('outcome') or {}).get('witnesses') or []:
            if x not in ids:
                bad.append((s['id'], 'unknown witness', x))
    for w in wd['witnesses']:
        for s in w.get('found_by') or []:
            if s not in sids:
                bad.append((w['id'], 'unknown search', s))
    return rows, bad


if __name__ == '__main__':
    rows, bad = check()
    for r in rows:
        print(f'  {r[0]} → {r[1]} (registered {r[2]}): earliest version {r[3]} · {r[4]} · {r[5]} · {r[6]}')
    for b in bad:
        print('  ✗', *b)
    print(f'witnesses: {len({r[0] for r in rows})} · links: {len(rows)} · problems: {len(bad)}')
    sys.exit(1 if bad else 0)
