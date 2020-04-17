import sys
import re

CAT = r'(\w)\1+'
DOG = r'\1'


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(CAT,DOG , line))