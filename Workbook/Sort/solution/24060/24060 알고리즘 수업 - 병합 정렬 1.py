inserted_value = []

def merge_sort(arr, first, last):
  global inserted_value
  if (first < last):

    mid = (first + last) // 2

    merge_sort(arr, first, mid)
    merge_sort(arr, mid + 1, last)

    return merge(arr, first, last)
  

def merge(arr, first, last):
  global inserted_value
  mid = (first + last) // 2
  lp, rp = first, mid + 1
  tmp = []

  while lp <= mid and rp <= last:
    if arr[lp] <= arr[rp]:
      tmp.append(arr[lp])
      inserted_value.append(arr[lp])
      lp += 1

    else:
      tmp.append(arr[rp])
      inserted_value.append(arr[rp])
      rp += 1

  while lp <= mid:
    tmp.append(arr[lp])
    inserted_value.append(arr[lp])
    lp += 1

  while rp <= last:
    tmp.append(arr[rp])
    inserted_value.append(arr[rp])
    rp += 1

  # for k in range(first, last + 1):
  #   arr[k] = tmp[k - first]
  arr[first:last + 1] = tmp

  return arr

a, k = map(int, input().split())
l = list(map(int, input().split()))
l = merge_sort(l, 0, len(l) - 1)

if len(inserted_value) < k:
  print(-1)
else:
  print(inserted_value[k - 1])