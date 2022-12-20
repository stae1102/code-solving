<<<<<<< HEAD
import sys
input = sys.stdin.readline


def lotto(arr, idx, lot):
    if len(lot) == 6:
        print(*lot)
        return
    if idx == len(arr):
        return
    lotto(arr, idx+1, lot+[arr[idx]])
    lotto(arr, idx+1, lot)


while True:
    n, *data = list(map(int, input().split()))
    if n == 0:
        break
    lotto(data, 0, [])
    print()
=======
import sys
input = sys.stdin.readline


def lotto(arr, idx, lot):
    if len(lot) == 6:
        print(*lot)
        return
    if idx == len(arr):
        return
    lotto(arr, idx+1, lot+[arr[idx]])
    lotto(arr, idx+1, lot)


while True:
    n, *data = list(map(int, input().split()))
    if n == 0:
        break
    lotto(data, 0, [])
    print()
>>>>>>> origin/ubuntu
