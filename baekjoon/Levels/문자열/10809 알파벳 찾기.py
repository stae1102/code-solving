a = input()
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in a: print(a.index(i), end=' ')
    else: print(-1, end=' ')

##### 새롭게 배운 것 #####
      
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')

"""
find( ) 함수가 찾기에 실패했을 때 -1을 출력
"""
