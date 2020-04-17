import sys
import re

CAT = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(CAT, line) :
        print(line)