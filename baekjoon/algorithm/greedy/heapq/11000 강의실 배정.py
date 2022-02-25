import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = [tuple(map(int, input().split())) for _ in range(n)]    # 강의실 시간표 초기화
q.sort()    # 시작 시간을 기준으로 오름차순으로 정리해줌 (수업을 시작하는 순서가 중요하기 때문에)

heap = []

for s, t in q:
    if heap:
        x = heapq.heappop(heap)
        if x > s:    # 끝나는 시간이 시작 시간보다 더 크기 때문에
            heapq.heappush(heap, x)    # 다시 값을 넣어줌
        heapq.heappush(heap, t)    # 새로운 강의 시간 입력
    else:
        heapq.heappush(heap, t)    # 새로운 강의 시간 입력

print(len(heap))
