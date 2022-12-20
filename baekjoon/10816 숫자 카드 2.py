def binary_search(arr, n):
    pl = 0
    pr = len(arr) - 1
    num = 0
    while (pl <= pr):
        mid = (pl + pr) // 2
        if arr[mid] >= n:
            num = mid
            pr = mid - 1
        else:
            pl = mid + 1
    return dict_card[num] if arr[num] == n else 0

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
compare = input().split()

dict_card = {}
for card in cards:
    dict_card[card] = dict_card.get(card, 0) + 1
print(dict_card.keys())
for i in range(m):
    k = binary_search(dict_card.keys(), compare[i])
    print(k, end=' ')
print(dict_card)