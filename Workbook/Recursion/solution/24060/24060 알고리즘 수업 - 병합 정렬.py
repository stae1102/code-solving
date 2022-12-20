tmp = [0, 0, 0, 0, 0]


def merge_sort(arr, l, r):
    if (l < r):
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    i, j, t = l, mid, 1
    while i <= mid and j <= r:
        if (arr[i] <= arr[j]):
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1

    while i <= mid:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1
    i, t = l, 1
    while i <= r:
        arr[i] = tmp[t]
        i += 1
        t += 1


arr = [4, 5, 1, 3, 2]
merge_sort(arr, 0, len(arr) - 1)

print(arr)
