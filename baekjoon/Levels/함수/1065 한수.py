def number(d: int) -> int:
    count = 0
    for i in range(1, d + 1):
        if (i == 1000) or ((100 <= i < 1000) and (i // 100 - (i % 100) // 10) != ((i % 100) // 10 - i % 10)): continue
        count += 1
    return count

print(number(int(input())))

##### 우수 사례 #####

print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))
