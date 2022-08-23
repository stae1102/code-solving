from sys import stdin, stdout

dot = stdin.readlines()[1:]

dot.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))

stdout.write(''.join(dot))