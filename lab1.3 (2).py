n = bin(int(input()))
n = n[2:6]
new = ''
i = len(n) - 1
while(i >= 0):
	new += n[i]
	i -= 1
print(int(new,2))