#!/usr/bin/env python3
"""Re-apply session arena/cbb12598's appended rows on top of upstream (main) tables.

Upstream session arena/da6d01ac (PR #8) added rows that collide on ID with this
session's rows. This session's rows are renumbered into the free ID range of each
table so both sessions' findings are published. IDs shift only where they collide.
"""
import csv, io, re, subprocess, sys

MY_REF = "f73e54b"

# table -> (my new id list, shift)
def rng(prefix, lo, hi):
    return ["%s-%02d" % (prefix, i) for i in range(lo, hi + 1)]


SHIFTS = {
    "work-requirements-law.csv": (rng("WR", 17, 36), 2),
    "work-requirement-exemptions.csv": (rng("EX", 17, 23), 0),
    "california-implementation.csv": (rng("CA", 13, 28), 2),
    "income-treatment.csv": (rng("IN", 16, 20), 3),
    "medi-cal-eligibility.csv": (rng("MC", 16, 18), 0),
    "covered-california.csv": (rng("CC", 13, 20), 1),
    "other-programs.csv": (rng("OT", 9, 15), 0),
    "options-summary.csv": (rng("OP", 7, 9), 0),
    "flagged-items.csv": (rng("FL", 11, 25), 2),
}


def load(ref, path):
    out = subprocess.run(["git", "show", "%s:data/%s" % (ref, path)],
                         capture_output=True, text=True, check=True).stdout
    return list(csv.DictReader(io.StringIO(out)))


def renumber_flags(text):
    """Shift this session's FL-11..FL-25 references by +2 (FL-13..FL-27)."""
    def sub(m):
        n = int(m.group(1))
        return "FL-%d" % (n + 2) if 11 <= n <= 25 else m.group(0)
    return re.sub(r"FL-(\d+)", sub, text)


for path, (ids, shift) in SHIFTS.items():
    mine = load(MY_REF, path)
    by_id = {r["id"]: r for r in mine}
    full = "data/" + path
    raw = io.open(full, newline="", encoding="utf-8").read()
    crlf = "\r\n" in raw
    nl = "\r\n" if crlf else "\n"
    rows = list(csv.DictReader(io.StringIO(raw)))
    have = {r["id"] for r in rows}
    new_rows = []
    for old in ids:
        r = by_id.get(old)
        if r is None:
            raise SystemExit("missing %s in %s" % (old, MY_REF))
        new_id = "%s-%d" % (old.split("-")[0], int(old.split("-")[1]) + shift)
        if new_id in have:
            raise SystemExit("collision on %s in %s" % (new_id, path))
        r = dict(r)
        r["id"] = new_id
        for k in ("detail", "notes", "value", "item"):
            if r.get(k):
                r[k] = renumber_flags(r[k])
        new_rows.append(r)
        have.add(new_id)
    out = io.StringIO()
    w = csv.DictWriter(out, fieldnames=list(rows[0].keys()),
                       lineterminator=nl, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    for r in rows + new_rows:
        w.writerow({k: r.get(k, "") for k in r})
    io.open(full, "w", newline="", encoding="utf-8").write(out.getvalue())
    print("%s: +%d rows -> %d total (%s)" % (path, len(new_rows), len(rows) + len(new_rows),
                                            "CRLF" if crlf else "LF"))
