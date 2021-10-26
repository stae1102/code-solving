##################
##### 보텀업 #####
##################

n = int(input())

d = [0] * 1000001
d[0] = 0
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[i] = d[i - 1] % 15746 + d[i - 2] % 15746
    d[i] %= 15746
print(d[n])

##################
##### 탑다운 #####
##################

mem={0:0,1:1}
mod=15746
def tile(t):
    if t in mem:
        return mem[t]
    else:
        if t%2==0:
            a=tile(t//2-1)%mod
            b=tile(t//2)%mod
            f=((2*a+b)*b)%mod
        else:
            f=(tile((t+1)//2)%mod)**2+(tile((t-1)//2)%mod)**2
        mem[t]=f%mod
        return f%mod
print(tile(int(input())+1))
