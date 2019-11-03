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


def minRemoveToMakeValid(s: str) -> str:
    """
    5249. 移除无效的括号
    给你一个由 '('、')' 和小写字母组成的字符串 s。
    你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
    请返回任意一个合法字符串。
    有效「括号字符串」应当符合以下 任意一条 要求：
    空字符串或只包含小写字母的字符串
    可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
    可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
    示例 1：
    输入：s = "lee(t(c)o)de)"
    输出："lee(t(c)o)de"
    解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
    示例 2：
    输入：s = "a)b(c)d"
    输出："ab(c)d"
    示例 3：
    输入：s = "))(("
    输出：""
    解释：空字符串也是有效的
    示例 4：
    输入：s = "(a(b(c)d)"
    输出："a(b(c)d)"
    提示：
    1 <= s.length <= 10^5
    s[i] 可能是 '('、')' 或英文小写字母
    """
    res = []
    stk = []
    for i, c in enumerate(s):
        if c == ')':
            if not stk: continue
            res.append(c)
            res.insert(stk.pop(), '(')
        elif c == '(':
            stk.append(len(res))
        else:
            res.append(c)
    return ''.join(res) if res else ''


def numberOfSubarrays(nums: List[int], k: int) -> int:
    """
    5248. 统计「优美子数组」
    给你一个整数数组 nums 和一个整数 k。
    如果某个子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    示例 1：
    输入：nums = [1,1,2,1,1], k = 3
    输出：2
    解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
    示例 2：
    输入：nums = [2,4,6], k = 1
    输出：0
    解释：数列中不包含任何奇数，所以不存在优美子数组。
    示例 3：
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    提示：
    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length
    """
    # 计算每个奇数的左右边缘来确定窗口左和右边界的可能性，最后左*右得到答案
    from collections import defaultdict
    n = len(nums)
    d = defaultdict(list)
    arr = []
    last = -1
    for i in range(n):
        if nums[i] & 1:
            d[i].append(i - last)
            arr.append(i)
            last = i
    if len(arr) < k: return 0
    last = n
    for i in range(n-1, -1, -1):
        if nums[i] & 1:
            d[i].append(last - i)
            last = i
    res = 0
    for i in range(len(arr) - k + 1):
        res += d[arr[i]][0] * d[arr[i + k - 1]][1]
    return res


def numberOfSubarrays2(nums: List[int], k: int) -> int:
    # 前缀和, 把奇数当作1，偶数当作0，前缀和的值就是该窗口中奇数的个数
    from collections import defaultdict
    s = defaultdict(int)
    s[0] += 1
    c = 0
    res = 0
    for x in nums:
        if x & 1:
            c += 1
        if c >= k:
            res += s[c - k]
        s[c] += 1
    return res


if __name__ == '__main__':
    res = numberOfSubarrays([1,1,2,1,1], 3)
    print(res)
    res = numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
    print(res)
    # res = minRemoveToMakeValid("lee(t(c)o)de)")
    # print(res)
    # res = treeDiameter([[0,1],[0,2]])
    # print(res)
    # res = treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]])
    # print(res)
    pass