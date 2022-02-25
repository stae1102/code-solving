import sys
l = sys.stdin.readlines()
new_list = []
for i in l:
    new_list.append(i[:-1])
print(new_list)
new_list.sort(key=lambda x: (x[:][-3:-1]))
print(*new_list, sep='\n')