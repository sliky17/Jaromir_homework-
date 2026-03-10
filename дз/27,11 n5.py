n = 1
for np in range(16, 53):
    if np % 6 == 0:
        n = np * n
print(n)