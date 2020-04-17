import sys
import re

CAT = r'(1(01*0)*1|0)*'
for line in sys.stdin:
    line = line.rstrip()
    if(re.fullmatch(CAT,line)):
        print(line)


        