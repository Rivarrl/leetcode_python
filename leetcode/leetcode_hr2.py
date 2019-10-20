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

if __name__ == '__main__':
    maximizeSweetness([8,13,20,1,16], 3)
    # numberToWords(1000)
    pass
