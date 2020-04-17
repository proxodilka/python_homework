import sys
import re

CAT = r'z...z'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(CAT, line) :
        print(line)