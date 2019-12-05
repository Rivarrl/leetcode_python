from typing import List
from algorithm_utils import *

@timeit
def minimumMoves(arr: List[int]) -> int:
    """
    5115. 删除回文子数组
    给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
    注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
    请你计算并返回从数组中删除所有数字所需的最少操作次数。
    示例 1：
    输入：arr = [1,2]
    输出：2
    示例 2：
    输入：arr = [1,3,4,1,5]
    输出：3
    解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
    提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 20
    """
    n = len(arr)
    dp = [[n] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][i] = 1
        dp[i-1][i] = 1 if arr[i-1] == arr[i] else 2
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                for x in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][x] + dp[x+1][j])
    print(dp)
    return dp[0][n-1]


@timeit
def minimumMoves2(arr):
    def fdp(i, j):
        if i > j: return 0
        if i == j: return 1
        if i + 1 == j:
            if arr[i] == arr[j]:
                return 1
            else:
                return 2
        if dp[i][j] != -1:
            return dp[i][j]
        res = n
        for k in range(i, j+1):
            if arr[i] != arr[k]: continue
            left = fdp(i+1, k-1)
            if left == 0: left = 1
            res = min(res, left + fdp(k+1, j))
        dp[i][j] = res
        return res
    n = len(arr)
    dp = [[-1] * n for _ in range(n)]
    res = fdp(0, n-1)
    print(dp)
    return res


def isGoodArray(nums: List[int]) -> bool:
    """
    5250. 检查「好数组」
    给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
    假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。
    示例 1：
    输入：nums = [12,5,7,23]
    输出：true
    解释：挑选数字 5 和 7。
    5*3 + 7*(-2) = 1
    示例 2：
    输入：nums = [29,6,10]
    输出：true
    解释：挑选数字 29, 6 和 10。
    29*1 + 6*(-3) + 10*(-1) = 1
    示例 3：
    输入：nums = [3,6]
    输出：false
    提示：
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    """
    def gcd(x, y):
        if x == 0: return y
        return gcd(y%x, x)
    n = len(nums)
    if n == 1: return nums[0] == 1
    c = nums[0]
    for i in range(1, n):
        c = gcd(c, nums[i])
        if c == 1: return True
    return False


@timeit
def numDupDigitsAtMostN(N: int) -> int:
    """
    1012. 至少有 1 位重复的数字
    给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数。
    示例 1：
    输入：20
    输出：1
    解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
    示例 2：
    输入：100
    输出：10
    解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
    示例 3：
    输入：1000
    输出：262
    提示：
    1 <= N <= 10^9
    """
    def f1(n):
        res, x = 0, 1
        for i in range(n):
            x *= q[i]
            res += x
        return res

    def f2(k, base):
        res = base
        for i in range(k+1, n):
            res *= q[i]
        return res

    def f3(i):
        m = int(sn[i])
        if i == n - 1: return m + 1 - sum(visit[:m+1])
        res = 0
        base = m - sum(visit[:m])
        if visit[m] == 0:
            visit[m] = 1
            res += f3(i + 1)
        if base > 0:
            res += f2(i, base)
        return res

    if N < 10: return 0
    sn = str(N)
    n = len(sn)
    q = [9] + [i for i in range(9, 0, -1)]
    visit = [0] * 11
    res = N
    if n - 1 >= 10:
        res -= f1(10)
    else:
        x = int(sn[0])
        res -= f1(n-1)
        if x - 1 > 0:
            res -= f2(0, x - 1)
        visit[x] += 1
        res -= f3(1)
    return res


@timeit
def maximizeSweetness(sweetness: List[int], K: int) -> int:
    """
    5111. 分享巧克力
    你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。
    你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。
    为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。
    请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。
    示例 1：
    输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
    输出：6
    解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。
    示例 2：
    输入：sweetness = [5,6,7,8,9,1,2,3,4], K = 8
    输出：1
    解释：只有一种办法可以把巧克力分成 9 块。
    示例 3：
    输入：sweetness = [1,2,2,1,2,2,1,2,2], K = 2
    输出：5
    解释：你可以把巧克力分成 [1,2,2], [1,2,2], [1,2,2]。
    提示：
    0 <= K < sweetness.length <= 10^4
    1 <= sweetness[i] <= 10^5
    """
    def judge(x):
        # 最小块大小为x的时候，能不能掰够K+1块
        cur = piece = 0
        for a in sweetness:
            cur += a
            if cur >= x:
                cur = 0
                piece += 1
            if piece >= K+1:
                return True
        return False
    lo, hi = 1, sum(sweetness) // (K+1)
    while lo < hi:
        mid = lo + (hi + 1 - lo) // 2
        if judge(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


@timeit
def countRangeSum(nums: List[int], lower: int, upper: int) -> int:
    """
    327. 区间和的个数
    给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
    区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
    说明:
    最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
    示例:
    输入: nums = [-2,5,-1], lower = -2, upper = 2,
    输出: 3
    解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
    """
    """
    # 前缀和遍历 O(n^2)
    from collections import defaultdict
    d = defaultdict(int)
    d[0] = 1
    res, c = 0, 0
    for x in nums:
        c += x
        for i in range(lower, upper+1):
            res += d[c - i]
        d[c] += 1
    return res
    """
    """
    # 前缀和 + 二分查找 O(nlogn)
    import bisect
    # 计算前缀和
    pre = [0]
    for e in nums:
        pre += [pre[-1] + e]
    # 将前缀和，二分查找计算范围内的命中数，并使其变为有序
    res = 0
    q = []
    # 一定要倒序遍历，因为边界是要较小的前缀和分别加lower和upper
    for k in pre[::-1]:
        i, j = k + lower, k + upper
        left = bisect.bisect_left(q, i)
        right = bisect.bisect_right(q, j)
        res += right - left
        bisect.insort(q, k)
    return res
    """
    # 前缀和 + 归并排序
    def merge(lo, hi):
        if lo >= hi: return 0
        mid = lo + (hi - lo) // 2
        res = merge(lo, mid) + merge(mid+1, hi)
        # 计数，落入区间[lower, upper] = [0, upper] - [0, lower)
        left = lo
        _lower = _upper = mid + 1
        while left < mid + 1:
            # [0, lower)
            while _lower <= hi and pre[_lower] - pre[left] < lower:
                _lower += 1
            # [0, upper]
            while _upper <= hi and pre[_upper] - pre[left] <= upper:
                _upper += 1
            res += _upper - _lower
            left += 1
        # 归并
        left, right = lo, mid + 1
        i = lo
        while left <= mid or right <= hi:
            if left > mid:
                aux[i] = pre[right]
                right += 1
            elif right > hi:
                aux[i] = pre[left]
                left += 1
            elif pre[left] > pre[right]:
                aux[i] = pre[right]
                right += 1
            else:
                aux[i] = pre[left]
                left += 1
            i += 1
        for i in range(lo, hi+1):
            pre[i] = aux[i]
        return res

    pre = [0]
    for e in nums:
        pre += [pre[-1] + e]
    # 归并用的辅助数组
    n = len(pre)
    aux = [0] * n
    res = merge(0, n-1)
    return res


def shortestSubarray(A: List[int], K: int) -> int:
    """
    862. 和至少为 K 的最短子数组
    返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
    如果没有和至少为 K 的非空子数组，返回 -1 。
    示例 1：
    输入：A = [1], K = 1
    输出：1
    示例 2：
    输入：A = [1,2], K = 4
    输出：-1
    示例 3：
    输入：A = [2,-1,2], K = 3
    输出：3
    提示：
    1 <= A.length <= 50000
    -10 ^ 5 <= A[i] <= 10 ^ 5
    1 <= K <= 10 ^ 9
    """
    pre = [0]
    for x in A:
        pre += [pre[-1] + x]
    q = []
    i, n = 0, len(pre)
    res = n + 1
    for i in range(n):
        while q and pre[i] <= pre[q[-1]]:
            q.pop()
        while q and pre[i] >= pre[q[0]] + K:
            res = min(res, i - q.pop(0))
        q.append(i)
    return res if res != n + 1 else -1


@timeit
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    """
    140. 单词拆分 II
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
    说明：
    分隔时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。
    示例 1：
    输入:
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    输出:
    [
      "cats and dog",
      "cat sand dog"
    ]
    示例 2：
    输入:
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    输出:
    [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    解释: 注意你可以重复使用字典中的单词。
    示例 3：
    输入:
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出:
    []
    """
    def _possible(s, words):
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]

    n = len(s)
    ws = set(wordDict)
    if not _possible(s, ws): return []
    def helper(i):
        res = []
        if i == n:
            res.append("")
        for j in range(i+1, n+1):
            if s[i:j] in ws:
                back = helper(j)
                for e in back:
                    cur = s[i:j] + " " + e if e != "" else s[i:j]
                    res.append(cur)
        return res
    return helper(0)


if __name__ == '__main__':
    # countRangeSum([-2,5,-1,0],-2,0)
    # maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)
    # wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
    # res = numDupDigitsAtMostN(1962)
    # res = isGoodArray([1])
    # print(res)
    # res = minimumMoves([16,6,14,6,7,6,20,6,5,4,20,19,8,13,11,7,7,5,2,19,14,6,20,10,10,4,9,5,19,10,11,16,3,9,9,6,18,1,3,12,12,11,17,3,11,11,7,16,12,12,5,8,7,10,15,20,3,15,9,10,11,11,2,1,15,19,4,11,15,19,17,13,10,20,20,19,8,6,2,14,12,5,2,4,16,10,3,4,4,12,2,6,5,9,15,4,10,2,15,15])
    # print(res)
    # res = minimumMoves2([16,6,14,6,7,6,20,6,5,4,20,19,8,13,11,7,7,5,2,19,14,6,20,10,10,4,9,5,19,10,11,16,3,9,9,6,18,1,3,12,12,11,17,3,11,11,7,16,12,12,5,8,7,10,15,20,3,15,9,10,11,11,2,1,15,19,4,11,15,19,17,13,10,20,20,19,8,6,2,14,12,5,2,4,16,10,3,4,4,12,2,6,5,9,15,4,10,2,15,15])
    # print(res)
    pass
