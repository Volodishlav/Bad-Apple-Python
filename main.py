#!/usr/bin/env python3

import os
import sys
import time
import pygame
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
FRAMES_DIR = SCRIPT_DIR / "frames-ascii"
AUDIO_FILE = SCRIPT_DIR / "bad_apple.mp3"

def usage():
    print(f"Usage: {sys.argv[0]} [-h|--help]")
    sys.exit(0)


def natural_sort_key(path):
    name = path.stem

    try:
        return int(name)
    except ValueError:
        return name


def get_frame_size():
    files = sorted(
        [f for f in FRAMES_DIR.iterdir() if f.is_file()],
        key=natural_sort_key
    )

    if not files:
        raise RuntimeError("No frames found.")

    with open(files[0], encoding="utf-8") as f:
        lines = f.readlines()

    width = max(len(line.rstrip("\n")) for line in lines)
    height = len(lines)

    return width, height


def resize_console(cols, rows):
    if os.name == "nt":
        os.system(f"mode con: cols={cols} lines={rows}")


def clear_screen():
    print("\033[2J", end="")


def move_cursor_top():
    print("\033[H", end="")


def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("bad_apple.mp3")
    pygame.mixer.music.set_volume(0.25)  # 25%
    pygame.mixer.music.play()


def main():

    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        usage()

    if not FRAMES_DIR.exists():
        print(f"Folder not found: {FRAMES_DIR}")
        sys.exit(1)

    play_audio()

    width, height = get_frame_size()
    resize_console(width + 2, height + 2)

    clear_screen()

    files = sorted(
        [f for f in FRAMES_DIR.iterdir() if f.is_file()],
        key=natural_sort_key
    )

    FRAME_TIME = 1 / 30 # 33ms

    start = time.perf_counter()

    for i, frame_file in enumerate(files):

        target_time = start + i * FRAME_TIME

        now = time.perf_counter()

        if target_time > now:
            time.sleep(target_time - now)

        move_cursor_top()

        with open(frame_file, encoding="utf-8") as f:
            sys.stdout.write(f.read())

        sys.stdout.flush()

    print("\nFin.")


if __name__ == "__main__":
    main()