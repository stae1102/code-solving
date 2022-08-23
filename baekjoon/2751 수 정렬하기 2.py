from sys import stdin, stdout
n = int(stdin.readline())

nums = sorted(map(int, stdin.read().split()))
print('\n'.join(map(str, nums)))