import sys
for i in range(int(sys.stdin.readline())):
    strs = list(sys.stdin.readline().split())
    for str in strs:
        print(str[::-1], end=" ") # 하나씩 거꾸로 출력
    print()
    
##### 모범 답안 #####

import sys

N = int(sys.stdin.readline())

for i in range(N):
    sentence = sys.stdin.readline()[::-1]
    store = sentence.split()
    store.reverse()
    sentence_reverse = ' '.join(store)
    print(sentence_reverse)
