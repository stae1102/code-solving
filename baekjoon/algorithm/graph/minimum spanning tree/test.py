data = [987654312]

a = [1, 2, 3, 4]
b = [6, 7, 8, 9]

a[3] = data[0]
b[3] = data[0]

b[3] = 123456789

print(b)
print(a)