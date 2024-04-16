from parse import *
import sys
inputt=sys.stdin.readline()
delete=parse("DELETE {:l}:{:d}\n",inputt)
print(delete)