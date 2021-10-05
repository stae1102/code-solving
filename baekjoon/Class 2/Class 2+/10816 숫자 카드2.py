##### 시간 복잡도 1등 #####
import sys
arr = [0] * 20000001

N = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))

for i in card:
    arr[i + 10000000] += 1

M = sys.stdin.readline()
find = list(map(int, sys.stdin.readline().split()))

for j in find:
    print(arr[j + 10000000], end = ' ')

##### 시간 복잡도 2등 #####

import sys
N = sys.stdin.readline()
n_lst = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
m_lst = list(map(int, sys.stdin.readline().split()))
hash = {}

for i in n_lst:
    hash[i] = hash.get(i, 0) + 1

print(*list(str(hash[j]) if j in hash else "0" for j in m_lst), end = ' ')

##### 시간 복잡도 3등 #####

import sys
N = sys.stdin.readline()
n_lst = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
m_lst = list(map(int, sys.stdin.readline().split()))
hash = {}

for i in n_lst:
    hash[i] = hash.get(i, 0) + 1

print(*list(str(hash[j]) if j in hash else "0" for j in m_lst), end = ' ')
