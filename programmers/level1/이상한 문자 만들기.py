def solution(s):
    a = s.split(" ")
    b = []
    for i in a:
        i = list(i)
        for j in range(len(i)):
            if j % 2:
                i[j] = i[j].lower()
            else:
                i[j] = i[j].upper()
        k = ''.join(i)
        b.append(k)
    return ' '.join(b)
