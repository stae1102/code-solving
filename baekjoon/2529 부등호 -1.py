import sys
input = sys.stdin.readline


def getGreatestNum(ies):
    great = ['9']
    tmp = 0
    nums = [str(i) for i in range(9)]

    for i in ies:
        if i == "<":
            great.insert(tmp, nums.pop())
        else:
            great.append(nums.pop())
            tmp = len(great) - 1

    return ''.join(great)


def getSmallestNum(ies):
    small = ['0']
    tmp = 0
    nums = [str(i) for i in range(9, 0, -1)]

    for i in ies:
        if i == "<":
            small.append(nums.pop())
            tmp = len(small) - 1
        else:
            small.insert(tmp, nums.pop())

    return ''.join(small)


k = int(input())
ies = input().rstrip().split()

greatest_num = getGreatestNum(ies)
smallest_num = getSmallestNum(ies)

print(greatest_num)
print(smallest_num)
