import sys
import math

n, *trees = map(int, sys.stdin.readlines())
trees.sort()
trees = [w - v for v, w in zip(trees, trees[1:])]
g = math.gcd(*trees)

print(sum(i // g - 1 for i in trees))
