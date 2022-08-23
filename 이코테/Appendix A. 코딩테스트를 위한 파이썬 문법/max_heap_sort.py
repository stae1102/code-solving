import heapq

def heap_sort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heap_sort([1, 3, 2, 6, 7, 5, 8, 9, 4])

print(result)