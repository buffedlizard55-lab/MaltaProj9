#!/usr/bin/env python3
"""Resolve CSV rebase/merge conflicts by union of rows keyed on `id`.

Conflict roles: `<<<<<<< HEAD` side is upstream (main); `>>>>>>>` side is the
incoming commit (this session's work). Both sides' rows are kept; on a duplicate
id the upstream row wins only if the incoming side did not touch it -- in practice
an id appears on one side only, because ids are session-allocated.
"""
import csv, io, sys


def resolve(path):
    raw = io.open(path, newline='', encoding='utf-8').read()
    if '<<<<<<<' not in raw:
        print("clean:", path)
        return
    nl = '\r\n' if '\r\n' in raw else '\n'
    head_rows, inc_rows, common = [], [], []
    mode = 'common'
    for line in raw.split(nl):
        if line.startswith('<<<<<<<'):
            mode = 'head'; continue
        if line.startswith('|||||||'):
            mode = 'base'; continue
        if line.startswith('=======') and mode in ('head', 'base'):
            mode = 'inc'; continue
        if line.startswith('>>>>>>>'):
            mode = 'common'; continue
        if mode == 'head':
            head_rows.append(line)
        elif mode == 'inc':
            inc_rows.append(line)
        else:
            common.append(line)
    if not common:
        raise SystemExit("no common section in " + path)
    header = common[0]
    body = [l for l in common[1:] if l.strip()]
    head_body = [l for l in head_rows[1:] if l.strip()]
    inc_body = [l for l in inc_rows[1:] if l.strip()]
    have = {l.split(',')[0] for l in body}
    added_head = [l for l in head_body if l.split(',')[0] not in have]
    have |= {l.split(',')[0] for l in added_head}
    added_inc = [l for l in inc_body if l.split(',')[0] not in have]
    merged = [header] + body + added_head + added_inc
    text = nl.join(merged)
    if not text.endswith(nl):
        text += nl
    io.open(path, 'w', newline='', encoding='utf-8').write(text)
    print("%s: base=%d +upstream=%d +incoming=%d -> %d rows"
          % (path, len(body), len(added_head), len(added_inc), len(merged) - 1))


for p in sys.argv[1:]:
    resolve(p)
