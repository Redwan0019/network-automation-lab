import difflib
import glob
import os
import sys

HOST = "devnetsandboxiosxec8k.cisco.com"
IGNORE = ("!", "Current configuration", "memory free low-watermark")

files = sorted(glob.glob(f"{HOST}_*.txt"), key=os.path.getmtime)

if len(files) < 2:
    print(f"Need at least 2 backups for {HOST}, found {len(files)}.")
    sys.exit()

before_file = files[-2]
after_file = files[-1]
print(f"Comparing:\n  before: {before_file}\n  after:  {after_file}\n")

with open(before_file) as f:
    before = [l for l in f.readlines() if not l.startswith(IGNORE)]

with open(after_file) as f:
    after = [l for l in f.readlines() if not l.startswith(IGNORE)]

diff = list(difflib.unified_diff(before, after, fromfile="before", tofile="after", lineterm=""))

print(f"Number of diff lines: {len(diff)}")
for line in diff:
    print(line.rstrip())