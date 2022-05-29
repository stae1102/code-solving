import sys
input = sys.stdin.readline
ans = set()

for _ in range(int(input())):
    command = input().rstrip().split()
    if command[0] == "add":
        ans.add(int(command[-1]))
    elif command[0] == "remove":
        try:
            ans.remove(int(command[-1]))
        except:
            continue
    elif command[0] == "check":
        if int(command[-1]) in ans:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        try:
            ans.remove(int(command[-1]))
        except:
            ans.add(int(command[-1]))
    elif command[0] == "all":
        ans = {i for i in range(1, 21)}
    else:
        ans = set()
