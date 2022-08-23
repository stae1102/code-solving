'''
def make_nums(nums, top, length):
    # 종료 조건
    if length == n:
        print(nums)
        exit()

    for i in range(1, 4):
        if i != top:
            if is_valid(nums + str(i)):
                make_nums(nums + str(i), i, length + 1)


def is_valid(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-2 * i: -1 * i] == num[-1 * i:]:
            return False
    return True


n = int(input())
make_nums("", None, 0)
'''


def make_nums():
    global tmp
    # 종료 조건
    if len(tmp) == n:
        print(''.join(tmp))
        exit()

    for i in range(1, 4):
        if is_valid(tmp, str(i)):
            tmp.append(str(i))
            make_nums()
            tmp.pop()


def is_valid(l, k):
    num = ''.join(l) + k
    for i in range(1, len(num) // 2 + 1):
        if num[-2 * i: -1 * i] == num[-1 * i:]:
            return False
    return True


n = int(input())
tmp = []
make_nums()
