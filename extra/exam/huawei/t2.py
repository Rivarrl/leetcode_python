import sys

# 华为t2，n个*和k-1个|的全排列

n, k = map(int, sys.stdin.readline().strip().split(' '))

def C(N, M):
    return A(N, M) // A(M, M)

def A(N, M):
    ans = 1
    for e in range(M):
        ans *= (N - e)
    return ans

ans = C(n+k-1, n)
print(ans)
def cross_print(i, j, cur):
    if i == n:
        cur += '|' * (k-1-j)
        print(cur)
        return
    if j == k - 1:
        cur += '*' * (n - i)
        print(cur)
        return
    cross_print(i+1, j, cur+'*')
    cross_print(i, j+1, cur+'|')

cross_print(0, 0, '')
