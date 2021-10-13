while True:
    try:
        cnt = [0, 0, 0, 0]
        for str in input():
            if str.islower():
                cnt[0] += 1
            elif str.isupper():
                    cnt[1] += 1
            elif str.isnumeric():
                cnt[2] += 1
            elif str == " ":
                cnt[3] += 1
            else:
                break
        print(cnt[0], cnt[1], cnt[2], cnt[3])
    except EOFError:
        break
