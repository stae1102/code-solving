import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

pf, ps, pt = 0, 1, 2 # 처음 중간 끝 커서를 설정
highest = None

while pf != n - 2: # 처음 커서가 두 번째 커서를 넘지 않는 경우
    s = l[pf] + l[ps] + l[pt] # 처음 중간 끝 커서의 인덱스를 더함
    if (highest is None or s > highest) and s <= m: # 매 순간 합이 최댓값이며 m을 넘는지 확인
        highest = s
    pt += 1 # 끝 커서를 계속 이동
    if pt > n - 1: # 끝 커서가 초과하면 두 번째 커서의 위치를 이동
        ps += 1 # 두 번째 커서 이동
        pt = ps + 1 # 세 번째 커서의 위치 초기화
    if ps > n - 2: # 두 번째 커서가 정해진 인덱스를 넘어가면
        pf += 1 # 첫 번째 커서 이동
        ps = pf + 1 # 두 번째 커서 위치 초기화
        pt = ps + 1 # 세 번째 커서 위치 초기화
print(highest)

########### 새롭게 배운 인사이트 #############

def P(n,m,c):
	t=set()
	for i in range(n-2): # for 반복문을 통해서 정해진 위치를 미리 지정해주면 더욱 편하고, 복잡도도 줄어듦
		for o in range(i+1,n-1):
			for p in range(o+1,n):
				s=c[i]+c[o]+c[p]
				if s<=m:
					t.add(s)
					break

	return max([*t])
print(P(*map(int,input().split()),list(sorted(map(int,input().split()))[::-1])))
