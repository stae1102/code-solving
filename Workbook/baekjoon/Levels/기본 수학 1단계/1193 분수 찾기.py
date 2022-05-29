n = int(input())
x = 0
l = []
while True:
    x += 1
    if n == 1:
        print("1/1")
        break
    elif 1 + ((x - 1) * x / 2) <= n <= 1 + ((x - 1) * x / 2) + (x - 1):
        top = abs(1 + ((x - 1) * x / 2) - n) + 1
        bottom = x + 1 - top
        if x % 2 == 1:
            print(f'{int(bottom)}/{int(top)}')
        else:
            print(f'{int(top)}/{int(bottom)}')
        break
        
##############################################
"""
1

2 3

4 5,6

7 8,9,10

11 12,13,14,15

16

1 + ((x - 1) * x / 2)

x = 1 일때 값은 1

x = 2 -> value = 2 ~ 2 + (x - 1)

x = 3 -> value = 4 ~ 4 + (x - 1)

x = 4 -> value = 7 ~ 7 + (x - 1)

x = 5 -> value = 11 ~ 11 + (x - 1)

또한 x가 홀수일 때와 짝수일 때 출력 순서가 바뀌므로 이것을 잘 고려해야 함
ex) x가 짝수이면 분모가 내림차순 / x가 홀수이면 분자가 

"""
