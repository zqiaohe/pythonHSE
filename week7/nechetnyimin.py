import sys

print(bool(list(filter(lambda x: x == 0,map(int,sys.stdin.read().split('\n'))))))
