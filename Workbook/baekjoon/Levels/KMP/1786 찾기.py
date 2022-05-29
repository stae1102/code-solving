def kmp_search(txt: str, pat: str) -> None:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)
    cnt = 0
    l = []

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    pt = pp = 0
    while pt != len(txt):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
        if pp == len(pat):
            cnt += 1
            l.append(pt - pp + 1)
            pp = skip[pp]

    print(cnt)
    print(*l, sep=' ')
    
kmp_search(input(), input())

"""
KMP법을 완전히 학습할 수 있는 좋은 기회였다.
KMP법을 그냥 쓰는 게 아니라, 얼마나 카운트 했고, 어떤 인덱스에서 찾았는지도 작성해야 했기에 부분 수정이 필요했다.
기존 알고있는 알고리즘에서 수정이 필요했던 부분은 일단 list를 만들어야 했고, 원래 KMP가 다 찾으면 탐색을 저장하지 않았기에
29번 라인 이후에서 if pp == len(pat):라는 내용을 추가했다.
pp를 skip[pp]로 해주어서 접미사와 겹치는 부분부터 다시 탐색을 시작했고, cnt와 append를 통해 횟수와 인덱스를 계산했다.
"""
