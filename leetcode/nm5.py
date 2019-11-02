from typing import List

from algorithm_utils import *

def treeDiameter(edges: List[List[int]]) -> int:
    """
    5098. 树的直径
    我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。
    树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。
    给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。
    示例 1：
    输入：edges = [[0,1],[0,2]]
    输出：2
    解释：
    这棵树上最长的路径是 1 - 0 - 2，边数为 2。
    示例 2：
    输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    输出：4
    解释：
    这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。
    提示：
    0 <= edges.length < 10^4
    edges[i][0] != edges[i][1]
    0 <= edges[i][j] <= edges.length
    edges 会形成一棵无向树
    """
    from collections import defaultdict
    if len(edges) == 0: return 0
    d = defaultdict(set)
    for x, y in edges:
        d[x].add(y)
        d[y].add(x)
    start = 0
    for k, v in d.items():
        if len(v) == 1:
            start = k
    res = 0
    for i in range(2):
        stk1 = [(start, 0)]
        visit = {start}
        c, step = start, 0
        while stk1:
            c, step = stk1.pop()
            for e in d[c]:
                if not e in visit:
                    visit.add(e)
                    stk1.insert(0, (e, step+1))
        start = c
        res = step
    return res

if __name__ == '__main__':
    res = treeDiameter([[0,1],[0,2]])
    print(res)
    res = treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]])
    print(res)
    pass