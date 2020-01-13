import sys

print(any(lambda x: x == 0,map(int,sys.stdin.read().split('\n'))))
