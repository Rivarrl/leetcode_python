# -*- coding:utf-8 -*-
import json
from collections import defaultdict

# ==============
# csv 转 json字符串
# ==============

path = './data'
data = '/'.join([path, 'data.csv'])

ds = []
with open(data, 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        row = line.strip().split(',')
        ds.append(row)
        line = f.readline()

print(ds)

n, m = len(ds), len(ds[0])
d = defaultdict()

def bfs(col, start, end):
    res = []
    if col == m - 1:
        res = [ds[i][col] for i in range(start, end+1) if ds[i][col]]
    else:
        last = end
        for i in range(end, start-1, -1):
            if ds[i][col]:
                res.insert(0, {ds[i][col]: bfs(col+1, i, last)})
                last = i - 1
    return res

res = bfs(0, 0, n-1)
res_str = json.dumps(res[0], ensure_ascii=False)
print(res_str)