def w(a: str) -> str:
    words = dict()
    for i in a:
        words[i] = words.get(i, 0) + 1
    bigcount = None
    bigword = None
    for word, count in words.items():
        if (bigcount is None) or count > bigcount:
            bigcount = count
            bigword = word
        if (bigword != word) and (count == max(words.values())):
            return "?"
    return bigword

print(w(input().upper()))

##### 시간 복잡도 줄이기 #####

n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
  result.append(n.count(i))
if result.count(max(result)) > 1:
  print("?")
else:
  print(alpa[result.index(max(result))])
  
"""
여기서의 insight는 count(max()) > 1을 통해서 중복값이 있는 것을 파악하는 것.
"""
