n = int(input())
i = 0
z = []
fuck = 1
for i in range(n):
    z.append(i+1)
print(z)
i = 1
for i in range(n):
    fuck = fuck* z[i]
print(fuck)