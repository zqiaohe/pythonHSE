import sys

contents = sys.stdin.read()
word_list = contents.split()
print(len(set(word_list)))
