#!/usr/bin/env python3
"""Draft entry writer for the weirdest job-title bounty (v1)."""

import os

ENTRY = "Chief Vibes Officer of the Department of Lost Left Socks"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
