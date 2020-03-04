import sys
# 华为t1，矩阵转置

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split(' '))))
m = int(sys.stdin.readline().strip())

m %= 4

res = [[0] * n for _ in range(n)]
if m == 0:
    res = arr
elif m == 1:
    x = y = 0
    for j in range(n):
        for i in range(n-1, -1, -1):
            res[x][y] = arr[i][j]
            y += 1
            if y == n:
                y = 0
                x += 1
elif m == 2:
    res = [e[::-1] for e in arr[::-1]]
else:
    x = y = 0
    for j in range(n-1, -1, -1):
        for i in range(n):
            res[x][y] = arr[i][j]
            y += 1
            if y == n:
                y = 0
                x += 1

for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    if i != n-1:
        print()
