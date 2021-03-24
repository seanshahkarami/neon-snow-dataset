#!/usr/bin/env python3
from pathlib import Path
import subprocess

# generate image list from labels
with Path("images.txt").open("w") as f:
    for path in Path("labels").glob("*.png"):
        site, year, month, day, _ = path.stem.split("_")
        url = f"https://phenocam.sr.unh.edu/data/archive/{site}/{year}/{month}/{path.stem}.jpg"
        print(url, file=f)

# download batch
subprocess.run(["wget", "-N", "-i", "images.txt", "-P", "images"])
