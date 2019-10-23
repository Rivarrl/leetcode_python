from typing import List

from algorithm_utils import *

# leetcode困难题2

def numberToWords(num):
    """
    273. 整数转换英文表示
    将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
    示例 1:
    输入: 123
    输出: "One Hundred Twenty Three"
    示例 2:
    输入: 12345
    输出: "Twelve Thousand Three Hundred Forty Five"
    示例 3:
    输入: 1234567
    输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    示例 4:
    输入: 1234567891
    输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    :param num: int
    :return: str
    """
    twenty = " One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    ty = "  Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    hundred = "Hundred"
    unit = " Thousand Million Billion".split(' ')
    if num == 0: return "Zero"
    def recur(n, t):
        if n < 20:
            return [twenty[n], unit[t]]
        elif 20 <= n < 100:
            return [ty[n//10]] + recur(n%10, t)
        elif 100 <= n < 1000:
            return [twenty[n//100], hundred] + recur(n%100, t)
        else:
            return recur(n//1000, t+1) + recur(n%1000, t)
    res = [e for e in recur(num, 0) if e]
    j = len(res) - 1
    while j > 0:
        if res[j] in unit and res[j-1] in unit:
            res.pop(j)
        j -= 1
    print(res)
    return ' '.join(res)


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
    n = len(sweetness)
    if K == n - 1: return min(sweetness)
    dp = [[[0] * (K+1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][0] = sweetness[i]
        for j in range(i+1, n):
            dp[i][j][0] += dp[i][j-1][0] + sweetness[j]
    # for i in range(n):
    #     for j in range(i, n):
    #         print(dp[i][j][0], end=' ')
    #     print()
    for k in range(1, K+1):
        for left in range(n-k):
            for right in range(left, n):
                for i in range(left, right):
                    for w in range(k):
                        dp[left][right][k] = max(dp[left][right][k], min(dp[left][i][w], dp[i+1][right][k-w-1]))
    print(dp[0][n-1][K])
    return dp[0][n-1][K]




def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    """
    1235. 规划兼职工作
    你打算利用空闲时间来做兼职工作赚些零花钱。
    这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
    给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
    注意，时间上出现重叠的 2 份工作不能同时进行。
    如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
    示例 1：
    输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    输出：120
    解释：
    我们选出第 1 份和第 4 份工作，
    时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
    示例 2：
    输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    输出：150
    解释：
    我们选择第 1，4，5 份工作。
    共获得报酬 150 = 20 + 70 + 60。
    示例 3：
    输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    输出：6
    提示：
    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4
    """
    arr = sorted(map(list, zip(startTime, endTime, profit)))
    n = len(arr)
    dp = [0] * n
    k, m = 0, 0
    res = 0
    for i in range(n):
        for j in range(k, i):
            if arr[i][0] >= arr[j][1]:
                # 保证m = max(m, dp[j])中所有的dp[j]只比较一次
                if j == k: k += 1
                m = max(m, dp[j])
        dp[i] = m + arr[i][2]
        res = max(res, dp[i])
    print(dp)
    return res


def countVowelPermutation(n: int) -> int:
    """
    1220. 统计元音字母序列的数目
    给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
    字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
    每个元音 'a' 后面都只能跟着 'e'
    每个元音 'e' 后面只能跟着 'a' 或者是 'i'
    每个元音 'i' 后面 不能 再跟着另一个 'i'
    每个元音 'o' 后面只能跟着 'i' 或者是 'u'
    每个元音 'u' 后面只能跟着 'a'
    由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
    示例 1：
    输入：n = 1
    输出：5
    解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
    示例 2：
    输入：n = 2
    输出：10
    解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
    示例 3：
    输入：n = 5
    输出：68
    提示：
    1 <= n <= 2 * 10^4
    """
    mod = 10 ** 9 + 7
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(2, n+1):
        a, e, i, o, u = (e+i+u) % mod, (i+a) % mod, (o+e) % mod, i, (i+o) % mod
    return sum((a,e,i,o,u)) % mod


if __name__ == '__main__':
    x = countVowelPermutation(5)
    print(x)
    # jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
    # maximizeSweetness([8,13,20,1,16], 3)
    # numberToWords(1000)
    pass
