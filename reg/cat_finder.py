import sys
import re

N = 2
CAT = r'cat'

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(CAT, line)) >= N:
        print(line)