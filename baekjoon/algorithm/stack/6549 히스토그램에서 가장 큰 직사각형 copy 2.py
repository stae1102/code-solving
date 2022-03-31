import math
import sys

sys.setrecursionlimit(10**6)

def init(left, right, node):
    if left == right:
        tree[node] = left
    else:
        mid = (left + right) // 2
        init(left, mid, node*2)
        init(mid + 1, right, node*2 + 1)
        # node - 1은 부모, node*2-1과 node*2는 각각 왼쪽, 오른쪽 자식 노드를 의미
        
        # 부모 노드에 더 작은 자식 노드 입력
        if arr[tree[node*2+1]] < arr[tree[node*2]]:
            tree[node] = tree[node*2+1]
        else:
            tree[node] = tree[node*2]

# 구간 최솟값을 찾아주는 쿼리 함수
def query(node, start, end, lidx, ridx):
    # 주어진 범위가 전체 범위를 벗어난 경우
    if lidx > end or ridx < start:
        return -1
    # 주어진 범위가 전체 범위 안에 포함되는 경우
    if lidx <= start and end <= ridx:
        return tree[node]
    
    mid = (start+end) // 2
    left = query(node*2, start, mid, lidx, ridx)
    right = query(node*2+1, mid+1, end, lidx, ridx)

    # 한쪽 노드가 범위를 벗어난 경우 자연스럽게 반대쪽 노드가 선택됨
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        # 더 작은 값의 인덱스 선택
        if arr[left] >= arr[right]:
            return right
        else:
            return left

def solve(start, end):
    # 해당 구간 범위의 최솟값 인덱스를 구함
    index = query(1, 0, len(arr) - 1, start, end)

    # 단일 블럭인 경우
    if end - start == 0:
        return arr[index]

    # v1 = 가장 낮은 블럭의 높이 * 히스토그램의 길이
    v1, v2, v3 = arr[index] * (end-start+1), 0, 0

    # 범위를 벗어나지 않는 경우 분할
    if index-1 >= start:
        v2 = solve(start, index - 1)
    if index+1 <= end:
        v3 = solve(index + 1, end)
    
    return max(v1, v2, v3)

while True:
    n, *arr = list(map(int, input().split()))
    if n == 0:
        break

    tree = [0] * (pow(2, math.ceil(math.log2(n)) + 1))
    
    init(0, len(arr) - 1, 1)
    print(tree)
    print(solve(0, len(arr) - 1))