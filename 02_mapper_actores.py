#!/usr/bin/env python3
import sys
import csv

# Posiciones en netflix_clean.csv: show_id = 0, cast = 4
IDX_ID, IDX_CAST = 0, 4

import io; sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", newline="")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

for row in csv.reader(sys.stdin):
    if len(row) <= IDX_CAST:
        continue
    show_id = row[IDX_ID].strip()
    if show_id == "show_id" or not show_id:  # omite cabecera
        continue
    for actor in row[IDX_CAST].split(","):
        actor = actor.strip()
        if actor:
            print(f"{actor}\t{show_id}")
