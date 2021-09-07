def solution(s, n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = list(s)
    t = []
    for i in s:
        if i in alphabet:
            w = alphabet.index(i)
            if n > 25 - w:
                next = (n % 26) + w - 26
            else:
                next = w + n
            t.append(alphabet[next])
        elif i == ' ':
            t.append(i)
        else:
            i = i.lower()
            w = alphabet.index(i)
            if n > 25 - w:
                next = (n % 26) + w - 26
            else:
                next = w + n
            t.append(alphabet[next].upper())
    return ''.join(t)
