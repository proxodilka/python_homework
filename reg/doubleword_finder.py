import sys
import re

CAT = r'\b(\w+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(CAT, line):
        print(line)

