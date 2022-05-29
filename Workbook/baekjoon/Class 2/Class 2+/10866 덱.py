import sys
n = int(sys.stdin.readline())
d = []

for i in range(n):
    a, *b = sys.stdin.readline().rstrip().split()
    if "push_front" in a:
        d.insert(0, b[0])
    elif "push_back" in a:
        d.append(b[0])
    elif a == "pop_front":
        print(d.pop(0) if d else -1)
    elif a == "pop_back":
        print(d.pop() if d else -1)
    elif a == "size":
        print(len(d))
    elif a == "empty":
        print(1 if not d else 0)
    elif a == "front":
        print(d[0] if d else -1)
    else:
        print(d[-1] if d else -1)
        
######## 리스트 사용 ########

import sys
n = int(sys.stdin.readline())
d = []
res = []

for i in range(n):
    a, *b = sys.stdin.readline().rstrip().split()
    if "push_front" in a:
        d.insert(0, b[0])
    elif "push_back" in a:
        d.append(b[0])
    elif a == "pop_front":
        res.append(d.pop(0) if d else '-1')
    elif a == "pop_back":
        res.append(d.pop() if d else '-1')
    elif a == "size":
        res.append(str(len(d)))
    elif a == "empty":
        res.append('1' if not d else '0')
    elif a == "front":
        res.append(d[0] if d else '-1')
    else:
        res.append(d[-1] if d else '-1')
print("\n".join(res))
