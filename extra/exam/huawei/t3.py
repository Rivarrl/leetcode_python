import sys

# 华为t3，多组编辑距离求和
arr = []

n = int(sys.stdin.readline().strip())
for i in range(n*2):
    arr.append(sys.stdin.readline().strip())
dp = [[0] * 105 for _ in range(105)]

def helper(s, t):
    n, m = len(s), len(t)
    for i in range(n+1):
        for j in range(m+1):
            dp[i][j] = 0
    for i in range(n+1):
        dp[i][0] = i
    for i in range(m+1):
        dp[0][i] = i
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = min(dp[i][j] + int(s[i] != t[i]), dp[i+1][j] + 1, dp[i][j+1] + 1)
    return dp[n][m]

ans = 0
for i in range(n):
    ans += helper(arr[i], arr[i+n])

print(ans)