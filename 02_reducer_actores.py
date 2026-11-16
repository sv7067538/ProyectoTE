#!/usr/bin/env python3
import sys

import io; sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

actual = None
ids = set()

for linea in sys.stdin:
    linea = linea.rstrip("\n")
    if "\t" not in linea:
        continue
    actor, show_id = linea.split("\t", 1)
    if actor != actual:
        if actual is not None:
            print(f"{actual}\t{len(ids)}")
        actual, ids = actor, set()
    ids.add(show_id)

if actual is not None:
    print(f"{actual}\t{len(ids)}")
