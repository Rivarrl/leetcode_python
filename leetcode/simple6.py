# -*- coding: utf-8 -*-
# ======================================
# @File    : simple6.py
# @Time    : 2019/10/8 10:05
# @Author  : Rivarrl
# ======================================
from typing import List

from algorithm_utils import *


def numPrimeArrangements(n):
    """
    1175. 质数排列
    请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
    让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
    由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
    示例 1：
    输入：n = 5
    输出：12
    解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。
    示例 2：
    输入：n = 100
    输出：682289015
    提示：
    1 <= n <= 100
    :param n: int
    :return: int
    """

    def f(x):
        ans = 1
        for i in range(1, x + 1):
            ans = (ans * i) % mod
        return ans

    prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    mod = 10 ** 9 + 7
    p = 0
    for i in range(1, n + 1):
        if i in prime:
            p += 1
    return (f(n - p) * f(p)) % mod


def robotSim(commands, obstacles):
    """
    874. 模拟行走机器人
    机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
    -2：向左转 90 度
    -1：向右转 90 度
    1 <= x <= 9：向前移动 x 个单位长度
    在网格上有一些格子被视为障碍物。
    第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
    如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
    返回从原点到机器人的最大欧式距离的平方。
    示例 1：
    输入: commands = [4,-1,3], obstacles = []
    输出: 25
    解释: 机器人将会到达 (3, 4)
    示例 2：
    输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
    输出: 65
    解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
    提示：
    0 <= commands.length <= 10000
    0 <= obstacles.length <= 10000
    -30000 <= obstacle[i][0] <= 30000
    -30000 <= obstacle[i][1] <= 30000
    答案保证小于 2 ^ 31
    :param commands: List[int]
    :param obstacles: List[List[int]]
    :return: int
    """
    from collections import defaultdict
    def turn(s, c):
        if s == -1:
            if c[0] != 0:
                c[0] *= -1
        else:
            if c[1] != 0:
                c[1] *= -1
        c[0], c[1] = c[1], c[0]

    n = [0, 0]
    d = [0, 1]
    ans = 0
    od = defaultdict(list)
    odr = defaultdict(list)
    for o in obstacles:
        od[o[0]].append(o[1])
        odr[o[1]].append(o[0])
    for c in commands:
        if c in {-1, -2}:
            turn(c, d)
        elif 1 <= c <= 9:
            if d[0] == 0:
                # 上下
                dst = n[1] + d[1] * c
                if od[n[0]]:
                    for e in od[n[0]]:
                        if d[1] == 1:
                            # 上
                            if e > n[1]:
                                dst = min(e - 1, dst)
                        else:
                            # 下
                            if e < n[1]:
                                dst = max(e + 1, dst)
                n[1] = dst
            else:
                # 左右
                dst = n[0] + d[0] * c
                if odr[n[1]]:
                    for e in odr[n[1]]:
                        if d[0] == 1:
                            # 右
                            if e > n[0]:
                                dst = min(e - 1, dst)
                        else:
                            # 左
                            if e < n[0]:
                                dst = max(e + 1, dst)
                n[0] = dst
            ans = max(n[0] ** 2 + n[1] ** 2, ans)
    return ans


def uniqueOccurrences(arr):
    """
    1207. 独一无二的出现次数
    给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
    如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
    示例 1：
    输入：arr = [1,2,2,1,1,3]
    输出：true
    解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
    示例 2：
    输入：arr = [1,2]
    输出：false
    示例 3：
    输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
    输出：true
    提示：
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
    :param arr: List[int]
    :return: bool
    """
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    return len(d.values()) == len(set(d.values()))


def powerfulIntegers(x, y, bound):
    """
    970. 强整数
    给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
    返回值小于或等于 bound 的所有强整数组成的列表。
    你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
    示例 1：
    输入：x = 2, y = 3, bound = 10
    输出：[2,3,4,5,7,9,10]
    解释：
    2 = 2^0 + 3^0
    3 = 2^1 + 3^0
    4 = 2^0 + 3^1
    5 = 2^1 + 3^1
    7 = 2^2 + 3^1
    9 = 2^3 + 3^0
    10 = 2^0 + 3^2
    示例 2：
    输入：x = 3, y = 5, bound = 15
    输出：[2,4,6,8,10,14]
    提示：
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
    :param x: int
    :param y: int
    :param bound: int
    :return: List[int]
    """
    i = 0
    res = []
    while y ** i <= bound:
        j = 0
        while x ** j + y ** i <= bound:
            res.append(x ** j + y ** i)
            if x == 1:
                break
            j += 1
        if y == 1:
            break
        i += 1
    return list(set(res))


def hasGroupsSizeX(deck):
    """
    914. 卡牌分组
    给定一副牌，每张牌上都写着一个整数。
    此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。
    仅当你可选的 X >= 2 时返回 true。
    示例 1：
    输入：[1,2,3,4,4,3,2,1]
    输出：true
    解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
    示例 2：
    输入：[1,1,1,2,2,2,3,3]
    输出：false
    解释：没有满足要求的分组。
    示例 3：
    输入：[1]
    输出：false
    解释：没有满足要求的分组。
    示例 4：
    输入：[1,1]
    输出：true
    解释：可行的分组是 [1,1]
    示例 5：
    输入：[1,1,2,2,2,2]
    输出：true
    解释：可行的分组是 [1,1]，[2,2]，[2,2]
    提示：
    1 <= deck.length <= 10000
    0 <= deck[i] < 10000
    :param deck: List[int]
    :return: bool
    """
    from collections import defaultdict
    d = defaultdict(int)
    for c in deck:
        d[c] += 1

    def gcd(x, y):
        return y if x == 0 else gcd(y % x, x)

    s = -1
    for i, v in enumerate(d.values()):
        if s == -1:
            s = v
        else:
            s = gcd(s, v)
    return s > 1


def isMonotonic(A):
    """
    896. 单调数列
    如果数组是单调递增或单调递减的，那么它是单调的。
    如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
    当给定的数组 A 是单调数组时返回 true，否则返回 false。
    示例 1：
    输入：[1,2,2,3]
    输出：true
    示例 2：
    输入：[6,5,4,4]
    输出：true
    示例 3：
    输入：[1,3,2]
    输出：false
    示例 4：
    输入：[1,2,4,5]
    输出：true
    示例 5：
    输入：[1,1,1]
    输出：true
    提示：
    1 <= A.length <= 50000
    -100000 <= A[i] <= 100000
    :param A: List[int]
    :return: bool
    """
    d, i = False, False
    for j in range(1, len(A)):
        if A[j] < A[j - 1]:
            d = True
        elif A[j] > A[j - 1]:
            i = True
    return not (d and i)


def findErrorNums(nums):
    """
    645. 错误的集合
    集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
    给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
    示例 1:
    输入: nums = [1,2,2,4]
    输出: [2,3]
    注意:
    给定数组的长度范围是 [2, 10000]。
    给定的数组是无序的。
    :param nums: List[int]
    :return: List[int]
    """
    n = len(nums)
    arr = [0] * (n + 1)
    arr[0] = -1
    res = []
    for i in nums:
        arr[i] += 1
        if arr[i] == 2:
            res.append(i)
    res.append(arr.index(0))
    return res


def judgeSquareSum(c):
    """
    633. 平方数之和
    给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
    示例1:
    输入: 5
    输出: True
    解释: 1 * 1 + 2 * 2 = 5
    示例2:
    输入: 3
    输出: False
    :param c: int
    :return: bool
    """
    """
    # 双指针法
    import math
    i, j = 0, int(math.sqrt(c))
    while i <= j:
        x = i ** 2 + j ** 2
        if x > c:
            j -= 1
        elif x < c:
            i += 1
        else:
            return True
    return False
    """
    # 费马平方和
    # 引理1：形如4k+3的自然数不能表示成2个整数的平方和
    # 引理2：正整数n可被表示为两整数平方和的充要条件为n的一切形如4k+3形状的质因子的幂次均为偶数
    # 素因数
    if c <= 2:
        return True
    while c % 2 == 0:
        c = c // 2
    p = 3
    while p * p <= c:
        index = 0
        while c % p == 0:
            index += 1
            c = c // p
        if (p % 4 == 3) and (index % 2 == 1):
            return False
        p += 2
    return c % 4 == 1


def findUnsortedSubarray(nums):
    """
    581. 最短无序连续子数组
    给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
    你找到的子数组应是最短的，请输出它的长度。
    示例 1:
    输入: [2, 6, 4, 8, 10, 9, 15]
    输出: 5
    解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
    说明 :
    输入的数组长度范围在 [1, 10,000]。
    输入的数组可能包含重复元素 ，所以升序的意思是<=。
    :param nums: List[int]
    :return: int
    """
    """
    # 排序 + 双指针
    a = sorted(nums)
    p, q = 0, len(a) - 1
    while p <= q and a[p] == nums[p]:
        p += 1
    while q >= p and a[q] == nums[q]:
        q -= 1
    return q - p + 1
    """
    # 单调栈
    stk1, stk2 = [], []
    p, q = len(nums) - 1, 0
    for i in range(len(nums)):
        while stk1 and nums[i] < nums[stk1[-1]]:
            p = min(stk1.pop(), p)
        stk1.append(i)
    if len(stk1) == len(nums): return 0
    for i in range(len(nums) - 1, -1, -1):
        while stk2 and nums[i] > nums[stk2[-1]]:
            q = max(stk2.pop(), q)
        stk2.append(i)
    return q - p + 1


def maximumProduct(nums):
    """
    628. 三个数的最大乘积
    给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
    示例 1:
    输入: [1,2,3]
    输出: 6
    示例 2:
    输入: [1,2,3,4]
    输出: 24
    注意:
    给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
    输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
    :param nums: List[int]
    :return: int
    """
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


def findRestaurant(list1, list2):
    """
    599. 两个列表的最小索引总和
    假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
    你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
    示例 1:
    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    输出: ["Shogun"]
    解释: 他们唯一共同喜爱的餐厅是“Shogun”。
    示例 2:
    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    输出: ["Shogun"]
    解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
    提示:
    两个列表的长度范围都在 [1, 1000]内。
    两个列表中的字符串的长度将在[1，30]的范围内。
    下标从0开始，到列表的长度减1。
    两个列表都没有重复的元素。
    :param list1: List[str]
    :param list2: List[str]
    :return: List[str]
    """
    s2 = set(list2)
    d = {}
    m = float('inf')
    for i, e in enumerate(list1):
        if e in s2:
            d[e] = i + list2.index(e)
            m = min(m, d[e])
    res = []
    for k, v in d.items():
        if v == m:
            res.append(k)
    return res


def missingNumber(arr):
    """
    5088. 等差数列中缺失的数字
    有一个数组，其中的值符合等差数列的数值规律，也就是说：
    在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。
    我们会从该数组中删除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。
    给你这个缺值的数组 arr，请你帮忙找出被删除的那个数。
    示例 1：
    输入：arr = [5,7,11,13]
    输出：9
    解释：原来的数组是 [5,7,9,11,13]。
    示例 2：
    输入：arr = [15,13,12]
    输出：14
    解释：原来的数组是 [15,14,13,12]。
    提示：
    3 <= arr.length <= 1000
    0 <= arr[i] <= 10^5
    :param arr: List[int]
    :return: int
    """
    for i in range(1, len(arr) + 1):
        last = arr[i] - arr[i - 1]
        cur = arr[i + 1] - arr[i]
        if last == 2 * cur:
            return arr[i] - cur
        if cur == 2 * last:
            return arr[i] + last


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    """
    5230. 缀点成线
    在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
    请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true 否则返回false
    提示：
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates 中不含重复的点
    """
    n = len(coordinates)
    if n <= 2: return True
    coordinates.sort()
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    k = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
    for i in range(2, n):
        x1, y1, x2, y2 = x2, y2, coordinates[i][0], coordinates[i][1]
        k1 = (y2 - y1) / (x2 - x1) if x2 != x1 else float('inf')
        if k != k1: return False
    return True


def balancedStringSplit(s: str) -> int:
    """
    1221. 分割平衡字符串
    在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
    给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
    返回可以通过分割得到的平衡字符串的最大数量。
    示例 1：
    输入：s = "RLRRLLRLRL"
    输出：4
    解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
    示例 2：
    输入：s = "RLLLLRRRLR"
    输出：3
    解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
    示例 3：
    输入：s = "LLLLRRRR"
    输出：1
    解释：s 只能保持原样 "LLLLRRRR".
    提示：
    1 <= s.length <= 1000
    s[i] = 'L' 或 'R'
    :param s: str
    :return: int
    """
    ctr, res = [0, 0], 0
    n = len(s)
    for i in range(n):
        ctr['RL'.index(s[i])] += 1
        if ctr[0] == ctr[1]:
            res += 1
    return res


def minCostToMoveChips(chips: List[int]) -> int:
    """
    1217. 玩筹码
    数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
    你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
    将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
    将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
    最开始的时候，同一位置上也可能放着两个或者更多的筹码。
    返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
    示例 1：
    输入：chips = [1,2,3]
    输出：1
    解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。
    示例 2：
    输入：chips = [2,2,2,3,3]
    输出：2
    解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。
    提示：
    1 <= chips.length <= 100
    1 <= chips[i] <= 10^9
    """
    r = [0, 0]
    for c in chips:
        r[c&1] += 1
    return min(r)


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    """
    1200. 最小绝对差
    给你个整数数组 arr，其中每个元素都 不相同。
    请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
    示例 1：
    输入：arr = [4,2,1,3]
    输出：[[1,2],[2,3],[3,4]]
    示例 2：
    输入：arr = [1,3,6,10,15]
    输出：[[1,3]]
    示例 3：
    输入：arr = [3,8,-10,23,19,-4,-14,27]
    输出：[[-14,-10],[19,23],[23,27]]
    提示：
    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6
    """
    """
    arr.sort()
    res = []
    m = float('inf')
    for i in range(1, len(arr)):
        m = min(m, arr[i] - arr[i-1])
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == m:
            res.append([arr[i-1], arr[i]])
    return res
    """
    # 不sort的方法, 复杂度随最小间距变化
    s = set(arr)
    res = []
    d = 0
    while not res:
        d += 1
        res = [e for e in s if e + d in s]
    return [[e, e+d] for e in sorted(res)]


if __name__ == '__main__':
    minCostToMoveChips([2,3,3,3,3])
    # checkStraightLine([[-1, 1], [-6, -4], [-6, 2], [2, 0], [-1, -2], [0, -4]])
    # maximumProduct([1,2,3,4])
    # isMonotonic([6,5,4,4])
    # x = [26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]
    # uniqueOccurrences(x)
    # a = [-2,-1,8,9,6]
    # b = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
    # robotSim(a, b)
    # x = numPrimeArrangements(5)
    # print(x)
    pass
