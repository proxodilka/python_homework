import sys
import re

CAT = r'\b(\w)(\w)'
DOG = r'\2\1'


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(CAT,DOG , line))
     

