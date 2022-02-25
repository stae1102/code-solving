import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))

arr_dict={i:v for v,i in enumerate(sort_arr)}

for i in arr:
    print(f'{arr_dict[i]} ')
    
####### 복잡도 높았던 시도들 ########

import sys
n = sys.stdin.readline()
s = list(map(int, sys.stdin.readline().split()))
a = set(s)
lst = sorted(list(a))

for i in s:
    print(lst.index(i), end=' ')
    
    
------------------------

import sys
n = sys.stdin.readline()
s = list(map(int, sys.stdin.readline().split()))
ans = []
for i in s:
    cnt = set()
    for j in s:
        if i > j:
            cnt.add(j)
    else:
        ans.append(len(cnt))
print(ans)
