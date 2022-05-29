a = int(input())
numbers = 0
s = 0
if a != 1:
    while s != a:
        numbers += 1
        s = numbers + sum(map(int, list(str(numbers)[:])))
        if numbers > a:
            numbers = 0
            break
elif a == 1:
    s = 0
print(numbers)

############## 새로운 인사이트 #################

def solve():
  n = int(input())
  for i in range(1, n):
    cnt = i
    test = i
    while True:
      cnt += (test % 10)
      test = test // 10
      if test == 0:
        break
    if cnt == n:
      print(i)
      return
  print(0)

solve()

"""
test // 10과 test % 10으로 자리수를 더하는 원리를 알게되었음
"""
