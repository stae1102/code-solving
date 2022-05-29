N = input()


N = int(N, 2)

print(oct(N).replace("0o", ''))


############################

n = input()

def octal(binary):
    octal = ""
    if len(binary) == 1:
        return binary
    elif len(binary) == 2:
        return int(binary[0]) * 2 + int(binary[1])
    for i in range(len(binary) - 1, -1, -3):
        if i == 0:
            octal = binary[i] + octal
        elif i == 1:
            octal = str(int(binary[i - 1]) * 2 + int(binary[i])) + octal
        else:
            octal = str(int(binary[i - 2]) * 4 + int(binary[i - 1]) * 2 + int(binary[i])) + octal
    return octal

print(octal(n))

#################################

binary = input()
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
octal = ""
while decimal >= 8:
    octal += str(decimal % 8)
    decimal //= 8
octal += str(decimal)
print(octal[::-1])
