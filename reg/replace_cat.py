import sys
import re

CAT = r'\b[a,A]+\b'
DOG = r'argh'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(CAT, DOG, line, count = 0))