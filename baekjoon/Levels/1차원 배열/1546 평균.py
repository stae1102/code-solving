a = int(input())
b = list(map(int, input().split()))
print(sum(b) / max(b) * 100 / len(b))

################ 숏코딩 ################

n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)
