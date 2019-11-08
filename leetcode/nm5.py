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


@timeit
def minSubArrayLen(s: int, nums: List[int]) -> int:
    """
    209. 长度最小的子数组
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
    示例: 
    输入: s = 7, nums = [2,3,1,2,4,3]
    输出: 2
    解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
    进阶:
    如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
    """
    """
    # 双指针 O(n)
    if s > sum(nums): return 0
    i, n = 0, len(nums)
    res, cur = n + 1, 0
    for j in range(n):
        cur += nums[j]
        while cur >= s:
            res = min(res, j - i + 1)
            cur -= nums[i]
            i += 1
    return res
    """
    # 前缀和 + 二分查找 O(nlogn)
    n = len(nums)
    # 求前缀和
    pre = [0] * (n+1)
    for i in range(1, n+1):
        pre[i] += pre[i-1] + nums[i-1]
    if pre[-1] < s: return 0
    # 在满足条件的前缀和中二分查找获得最优区间
    res = n + 1
    for i in range(n+1):
        if pre[i] - s >= 0:
            lo, hi = 0, i
            while lo < hi:
                mid = lo + (hi + 1 - lo) // 2
                if pre[i] - pre[mid] >= s:
                    lo = mid
                else:
                    hi = mid - 1
            res = min(res, i - lo)
    return res


if __name__ == '__main__':
    # minSubArrayLen(697439, [5334,6299,4199,9663,8945,3566,9509,3124,6026,6250,7475,5420,9201,9501,38,5897,4411,6638,9845,161,9563,8854,3731,5564,5331,4294,3275,1972,1521,2377,3701,6462,6778,187,9778,758,550,7510,6225,8691,3666,4622,9722,8011,7247,575,5431,4777,4032,8682,5888,8047,3562,9462,6501,7855,505,4675,6973,493,1374,3227,1244,7364,2298,3244,8627,5102,6375,8653,1820,3857,7195,7830,4461,7821,5037,2918,4279,2791,1500,9858,6915,5156,970,1471,5296,1688,578,7266,4182,1430,4985,5730,7941,3880,607,8776,1348,2974,1094,6733,5177,4975,5421,8190,8255,9112,8651,2797,335,8677,3754,893,1818,8479,5875,1695,8295,7993,7037,8546,7906,4102,7279,1407,2462,4425,2148,2925,3903,5447,5893,3534,3663,8307,8679,8474,1202,3474,2961,1149,7451,4279,7875,5692,6186,8109,7763,7798,2250,2969,7974,9781,7741,4914,5446,1861,8914,2544,5683,8952,6745,4870,1848,7887,6448,7873,128,3281,794,1965,7036,8094,1211,9450,6981,4244,2418,8610,8681,2402,2904,7712,3252,5029,3004,5526,6965,8866,2764,600,631,9075,2631,3411,2737,2328,652,494,6556,9391,4517,8934,8892,4561,9331,1386,4636,9627,5435,9272,110,413,9706,5470,5008,1706,7045,9648,7505,6968,7509,3120,7869,6776,6434,7994,5441,288,492,1617,3274,7019,5575,6664,6056,7069,1996,9581,3103,9266,2554,7471,4251,4320,4749,649,2617,3018,4332,415,2243,1924,69,5902,3602,2925,6542,345,4657,9034,8977,6799,8397,1187,3678,4921,6518,851,6941,6920,259,4503,2637,7438,3893,5042,8552,6661,5043,9555,9095,4123,142,1446,8047,6234,1199,8848,5656,1910,3430,2843,8043,9156,7838,2332,9634,2410,2958,3431,4270,1420,4227,7712,6648,1607,1575,3741,1493,7770,3018,5398,6215,8601,6244,7551,2587,2254,3607,1147,5184,9173,8680,8610,1597,1763,7914,3441,7006,1318,7044,7267,8206,9684,4814,9748,4497,2239])
    minSubArrayLen(3, [1,1])
    # res = numberOfSubarrays([1,1,2,1,1], 3)
    # print(res)
    # res = numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
    # print(res)
    # res = minRemoveToMakeValid("lee(t(c)o)de)")
    # print(res)
    # res = treeDiameter([[0,1],[0,2]])
    # print(res)
    # res = treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]])
    # print(res)
    pass