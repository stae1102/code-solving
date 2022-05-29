import sys
input = sys.stdin.readline

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if dis > (r1 + r2) ** 2: # 첫 번째 케이스, 두 원이 접하지 않을 때
        print(0)
    elif dis == (r1 + r2) ** 2: # 두 원이 외접하고 겹치는 지점이 1개일 때
        print(1)
    else:
        if dis >= max(r1 ** 2, r2 ** 2): # 중심점이 원 내부에 없을 때
            print(2)
        else: # 중심점이 원 내부에 있을 때
            if x1 == x2 and y1 == y2 and r1 == r2:
                print(-1)
            elif (r1 - r2) ** 2 < dis:
                print(2)
            elif (r1 - r2) ** 2 == dis:
                print(1)
            else:
                print(0)
