import heapq

def heap_sort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heap_sort([1, 2, 5, 7, 3, 6, 9, 8, 4])

print(result)