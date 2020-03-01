import sys
sys.setrecursionlimit(30000)

# 输入有向图G的边集，起点集和终点
# 输出所有起点到终点途经的点集
# 输入：[[1,3],[1,4],[2,3],[2,4]]|[1,2]|3
# 输出：[1,2,3]

line = sys.stdin.readline().strip()
ps = line.split('|')
ff = ps[0].replace('[', '').replace(']', '').split(',')
arr = [[int(ff[i]), int(ff[i + 1])] for i in range(0, len(ff), 2)]
stk = list(map(int, ps[1].replace('[', '').replace(']', '').split(',')))
dout = int(ps[2])

graph = [[] for _ in range(len(arr) + 1)]
for x, y in arr:
    graph[y].append(x)

vis = {}
def dfs(u, path):
    if u in stk:
        res.update(set(path))
    if u in vis: return
    vis[u] = 1
    for v in graph[u]:
        dfs(v, path + [v])

res = set()
res.add(dout)
dfs(dout, [])
print(str(sorted(list(set(res)))).replace(' ', ''))
