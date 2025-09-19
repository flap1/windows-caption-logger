#!/usr/bin/env python3
"""
Windows Live Caption Logger
Copyright (c) 2025 flap1
MIT License
"""

import uiautomation as auto
import time
import difflib

OUTPUT_FILE = "captions_log.txt"

def main():
    # Find Live Caption window (try both English and Japanese names)
    window = auto.WindowControl(searchDepth=1, Name="Live captions")
    if not window.Exists(3, 1):
        window = auto.WindowControl(searchDepth=1, Name="ライブ キャプション")
        if not window.Exists(3, 1):
            print("Live Caption window not found. Please launch it with Win+Ctrl+L")
            return

    print("Monitoring Live Captions...")
    last_line = ""

    while True:
        # Get caption text
        text_elem = window.TextControl()
        full_text = text_elem.Name.strip() if text_elem else ""
        lines = [line.strip() for line in full_text.splitlines() if line.strip()]

        if not lines:
            time.sleep(0.5)
            continue

        current_last = lines[-1]  # Current ongoing line

        if current_last != last_line:
            # Extract only new portion using diff
            diff = difflib.SequenceMatcher(None, last_line, current_last)
            _, _, _, j1, j2 = diff.get_opcodes()[-1]
            new_part = current_last[j1:j2]

            # Save new text
            if new_part.strip():
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(new_part)
                print(new_part, end="")

            last_line = current_last

        time.sleep(0.5)

if __name__ == "__main__":
    main()