card = [i for i in range(1, int(input()) + 1)]
def find(c):
    if len(c) <= 2:
        return c[-1]
    else:
        q = card + [0] * (len(c) - 2)
        idx = -1
        cnt = 1
        while abs(idx) < len(q):
            l = len(q)
            idx -= (cnt * 2)
            cnt *= 2
    return q[idx + cnt]
print(find(card))
