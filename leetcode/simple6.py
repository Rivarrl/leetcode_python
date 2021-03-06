# -*- coding: utf-8 -*-
# ======================================
# @File    : simple6.py
# @Time    : 2019/10/8 10:05
# @Author  : Rivarrl
# ======================================
import math
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
    解释: 他们唯一共同喜爱的餐厅是'Shogun'。
    示例 2:
    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    输出: ["Shogun"]
    解释: 他们共同喜爱且具有最小索引和的餐厅是'Shogun'，它有最小的索引和1(0+1)。
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


def numSmallerByFrequency(queries: List[str], words: List[str]) -> List[int]:
    """
    1170. 比较字符串最小字母出现频次
    我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
    例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
    现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。
    示例 1：
    输入：queries = ["cbd"], words = ["zaaaz"]
    输出：[1]
    解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
    示例 2：
    输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    输出：[1,2]
    解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
    提示：
    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] 都是小写英文字母
    """
    def f(s):
        for i in range(26):
            c = s.count(chr(ord('a') + i))
            if c > 0: return c
    cmp = [0] * 11
    for w in words:
        cmp[f(w)-1] += 1
    for i in range(9, -1, -1):
        cmp[i] += cmp[i+1]
    res = [0] * len(queries)
    for i, s in enumerate(queries):
        res[i] = cmp[f(s)]
    return res


def reachNumber(target: int) -> int:
    """
    754. 到达终点数字
    在一根无限长的数轴上，你站在0的位置。终点在target的位置。
    每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
    返回到达终点需要的最小移动次数。
    示例 1:
    输入: target = 3
    输出: 2
    解释:
    第一次移动，从 0 到 1 。
    第二次移动，从 1 到 3 。
    示例 2:
    输入: target = 2
    输出: 3
    解释:
    第一次移动，从 0 到 1 。
    第二次移动，从 1 到 -1 。
    第三次移动，从 -1 到 2 。
    注意:
    target是在[-10^9, 10^9]范围中的非零整数。
    """
    target = abs(target)
    n = int(math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2))
    target -= n * (n + 1) // 2
    return n if target % 2 == 0 else n + 1 + n % 2


def findSolution(customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    """
    5238. 找出给定方程的正整数解
    给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
    给定函数是严格单调的，也就是说：
    f(x, y) < f(x + 1, y)
    f(x, y) < f(x, y + 1)
    函数接口定义如下：
    interface CustomFunction {
    public:
      // Returns positive integer f(x, y) for any given positive integer x and y.
      int f(int x, int y);
    };
    如果你想自定义测试，你可以输入整数 function_id 和一个目标结果 z 作为输入，其中 function_id 表示一个隐藏函数列表中的一个函数编号，题目只会告诉你列表中的 2 个函数。  
    你可以将满足条件的 结果数对 按任意顺序返回。
    示例 1：
    输入：function_id = 1, z = 5
    输出：[[1,4],[2,3],[3,2],[4,1]]
    解释：function_id = 1 表示 f(x, y) = x + y
    示例 2：
    输入：function_id = 2, z = 5
    输出：[[1,5],[5,1]]
    解释：function_id = 2 表示 f(x, y) = x * y
    提示：
    1 <= function_id <= 9
    1 <= z <= 100
    题目保证 f(x, y) == z 的解处于 1 <= x, y <= 1000 的范围内。
    在 1 <= x, y <= 1000 的前提下，题目保证 f(x, y) 是一个 32 位有符号整数。
    """
    # 双指针
    i, j = 1, 1000
    res = []
    while i <= 1000 and j >= 1:
        cur = customfunction.f(i, j)
        if cur == z:
            res.append([i, j])
            i += 1
        elif cur < z:
            i += 1
        else:
            j -= 1
    return res


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    496. 下一个更大元素 I
    给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
    nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
    示例 1:
    输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
    输出: [-1,3,-1]
    解释:
        对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
        对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
        对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
    示例 2:
    输入: nums1 = [2,4], nums2 = [1,2,3,4].
    输出: [3,-1]
    解释:
        对于num1中的数字2，第二个数组中的下一个较大数字是3。
        对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
    注意:
    nums1和nums2中所有元素是唯一的。
    nums1和nums2 的数组大小都不超过1000。
    """
    stk = []
    d = {}
    for x in nums2:
        while stk and stk[-1] < x:
            d[stk.pop()] = x
        stk.append(x)
    return [d[e] if e in d else -1 for e in nums1]


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    """
    566. 重塑矩阵
    在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
    给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
    重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
    如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
    示例 1:
    输入:
    nums =
    [[1,2],
     [3,4]]
    r = 1, c = 4
    输出:
    [[1,2,3,4]]
    解释:
    行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
    示例 2:
    输入:
    nums =
    [[1,2],
     [3,4]]
    r = 2, c = 4
    输出:
    [[1,2],
     [3,4]]
    解释:
    没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
    注意：
    给定矩阵的宽和高范围在 [1, 100]。
    给定的 r 和 c 都是正数。
    """
    n = len(nums)
    if n == 0: return nums
    m = len(nums[0])
    if r * c != n * m: return nums
    x, y = 0, 0
    res = [[0] * c for _ in range(r)]
    for i in range(n):
        for j in range(m):
            res[x][y] = nums[i][j]
            y += 1
            if y == c:
                y = 0
                x += 1
    return res


def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    """
    598. 范围求和 II
    给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。
    操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素 M[i][j] 的值都增加 1。
    在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
    示例 1:
    输入:
    m = 3, n = 3
    operations = [[2,2],[3,3]]
    输出: 4
    解释:
    初始状态, M =
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    执行完操作 [2,2] 后, M =
    [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 0]]
    执行完操作 [3,3] 后, M =
    [[2, 2, 1],
     [2, 2, 1],
     [1, 1, 1]]
    M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
    注意:
    m 和 n 的范围是 [1,40000]。
    a 的范围是 [1,m]，b 的范围是 [1,n]。
    操作数目不超过 10000。
    """
    mx, my = float('inf'), float('inf')
    for op in ops:
        if op == [0, 0]: continue
        mx, my = min(mx, op[0]), min(my, op[1])
    return mx * my if mx != float('inf') else m * n


def countBinarySubstrings(s: str) -> int:
    """
    696. 计数二进制子串
    给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
    重复出现的子串要计算它们出现的次数。
    示例 1 :
    输入: "00110011"
    输出: 6
    解释: 有6个子串具有相同数量的连续1和0：'0011'，'01'，'1100'，'10'，'0011' 和 '01'。
    请注意，一些重复出现的子串要计算它们出现的次数。
    另外，'00110011'不是有效的子串，因为所有的0（和1）没有组合在一起。
    示例 2 :
    输入: "10101"
    输出: 4
    解释: 有4个子串：'10'，'01'，'10'，'01'，它们具有相同数量的连续1和0。
    注意：
    s.length 在1到50,000之间。
    s 只包含'0'或'1'字符。
    """
    cur, last, res = 1, 0, 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            last, cur = cur, 1
        if cur <= last: res += 1
    return res


def countCharacters(words: List[str], chars: str) -> int:
    """
    1160. 拼写单词
    给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
    假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
    注意：每次拼写时，chars 中的每个字母都只能用一次。
    返回词汇表 words 中你掌握的所有单词的 长度之和。
    示例 1：
    输入：words = ["cat","bt","hat","tree"], chars = "atach"
    输出：6
    解释：
    可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
    示例 2：
    输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    输出：10
    解释：
    可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
    提示：
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    所有字符串中都仅包含小写英文字母
    """
    from collections import defaultdict
    arr = [0] * 26
    for c in chars:
        arr[ord(c) - ord('a')] += 1
    d = defaultdict(int)
    res = 0
    for word in words:
        for letter in word:
            d[letter] += 1
        for k, v in d.items():
            if arr[ord(k) - ord('a')] < v:
                break
        else:
            res += len(word)
        d.clear()
    return res


def removeDuplicates(S: str) -> str:
    """
    1047. 删除字符串中的所有相邻重复项
    给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
    在 S 上反复执行重复项删除操作，直到无法继续删除。
    在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
    示例：
    输入："abbaca"
    输出："ca"
    解释：
    例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
    提示：
    1 <= S.length <= 20000
    S 仅由小写英文字母组成。
    """
    stk = []
    for i in range(len(S)):
        if stk and S[stk[-1]] == S[i]:
            stk.pop()
        else:
            stk.append(i)
    return ''.join([S[i] for i in stk]) if stk else ''


def gardenNoAdj(N: int, paths: List[List[int]]) -> List[int]:
    """
    1042. 不邻接植花
    有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。
    paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。
    另外，没有花园有 3 条以上的路径可以进入或者离开。
    你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。
    以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1, 2, 3, 4 表示。保证存在答案。
    示例 1：
    输入：N = 3, paths = [[1,2],[2,3],[3,1]]
    输出：[1,2,3]
    示例 2：
    输入：N = 4, paths = [[1,2],[3,4]]
    输出：[1,2,1,2]
    示例 3：
    输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    输出：[1,2,3,4]
    提示：
    1 <= N <= 10000
    0 <= paths.size <= 20000
    不存在花园有 4 条或者更多路径可以进入或离开。
    保证存在答案。
    """
    adj = [list() for _ in range(N)]
    res = [0] * N
    for x, y in paths:
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    for i in range(N):
        flowers = {1, 2, 3, 4}
        for j in adj[i]:
            if res[j] > 0:
                flowers.discard(res[j])
        res[i] = flowers.pop()
    return res


def findOcurrences(text: str, first: str, second: str) -> List[str]:
    """
    1078. Bigram 分词
    给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。
    对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
    示例 1：
    输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
    输出：["girl","student"]
    示例 2：
    输入：text = "we will we will rock you", first = "we", second = "will"
    输出：["we","rock"]
    提示：
    1 <= text.length <= 1000
    text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
    1 <= first.length, second.length <= 10
    first 和 second 由小写英文字母组成
    """
    res = []
    tl = text.split(' ')
    for i in range(2, len(tl)):
        if tl[i-1] == second:
            if tl[i-2] == first:
                res.append(tl[i])
    return res


def dominantIndex(nums: List[int]) -> int:
    """
    747. 至少是其他数字两倍的最大数
    在一个给定的数组nums中，总是存在一个最大元素 。
    查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
    如果是，则返回最大元素的索引，否则返回-1。
    示例 1:
    输入: nums = [3, 6, 1, 0]
    输出: 1
    解释: 6是最大的整数, 对于数组中的其他整数,
    6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
    示例 2:
    输入: nums = [1, 2, 3, 4]
    输出: -1
    解释: 4没有超过3的两倍大, 所以我们返回 -1.
    提示:
    nums 的长度范围在[1, 50].
    每个 nums[i] 的整数范围在 [0, 100].
    """
    if len(nums) == 1: return 0
    m1, i1, m2, i2 = -1, 0, -1, 0
    for i, x in enumerate(nums):
        if x > m1:
            m1, m2, i1, i2 = x, m1, i, i1
        elif x > m2:
            m2, i2 = x, i
    return i1 if m2 == 0 or m1 // m2 >= 2 else -1


if __name__ == '__main__':
    x = dominantIndex([1, 1])
    print(x)
    # res = gardenNoAdj(N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
    # print(res)
    # res = removeDuplicates("abbaca")
    # print(res)
    # res = countBinarySubstrings("00110011")
    # print(res)
    # res = maxCount(3, 3, [[2,2],[3,3]])
    # print(res)
    # matrixReshape([[1,2],[3,4]], 1, 4)
    # res = nextGreaterElement([4,1,2], [1,3,4,2])
    # print(res)
    # x = reachNumber(4)
    # print(x)
    # numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])
    # minCostToMoveChips([2,3,3,3,3])
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
