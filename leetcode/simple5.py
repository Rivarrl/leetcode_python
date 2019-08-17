# -*- coding:utf-8 -*-
from algorithm_utils import *


# leetcode 简单题 5

def leafSimilar(root1, root2):
    """
    872. 叶子相似的树
    请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
          3
       5     1
      6 2   9 8
       7 4
    举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
    如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
    如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
    提示：
    给定的两颗树可能会有 1 到 100 个结点。
    :param root1: TreeNode
    :param root2: TreeNode
    :return: bool
    """

    def helper(node):
        if node:
            if not node.left and not node.right:
                yield node.val
            else:
                yield from helper(node.left)
                yield from helper(node.right)

    for x, y in zip(helper(root1), helper(root2)):
        if x != y:
            return False
    return True


def tribonacci(n):
    """
    1137. 第 N 个泰波那契数
    泰波那契序列 Tn 定义如下： 
    T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
    给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
    示例 1：
    输入：n = 4
    输出：4
    解释：
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4
    示例 2：
    输入：n = 25
    输出：1389537
    提示：
    0 <= n <= 37
    答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
    :param n: int
    :return: int
    """
    t0, t1, t2 = 0, 1, 1
    if n < 3:
        return [t0, t1, t2][n]
    for i in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t2


def distributeCandies(candies, num_people):
    """
    1103. 分糖果 II
    排排坐，分糖果。
    我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。
    给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。
    然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。
    重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。
    返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。
    示例 1：
    输入：candies = 7, num_people = 4
    输出：[1,2,3,1]
    解释：
    第一次，ans[0] += 1，数组变为 [1,0,0,0]。
    第二次，ans[1] += 2，数组变为 [1,2,0,0]。
    第三次，ans[2] += 3，数组变为 [1,2,3,0]。
    第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
    示例 2：
    输入：candies = 10, num_people = 3
    输出：[5,2,3]
    解释：
    第一次，ans[0] += 1，数组变为 [1,0,0]。
    第二次，ans[1] += 2，数组变为 [1,2,0]。
    第三次，ans[2] += 3，数组变为 [1,2,3]。
    第四次，ans[0] += 4，最终数组变为 [5,2,3]。
    提示：
    1 <= candies <= 10^9
    1 <= num_people <= 1000
    :param candies: int
    :param num_people: int
    :return: List[int]
    """
    n = 1
    while n * (n + 1) < 2 * candies:
        n += 1
    res = [0] * num_people
    for j in range(n):
        i = j % num_people
        cur = min(j + 1, candies)
        res[i] += cur
        candies -= j + 1
    return res


def lastStoneWeight(stones):
    """
    1046. 最后一块石头的重量
    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
    提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
    :param stones: List[int]
    :return: int
    """
    while len(stones) > 1:
        stones.sort()
        s1 = stones.pop()
        s2 = stones.pop()
        while stones and s2 + stones[-1] <= s1:
            s2 += stones.pop()
        s3 = s1 - s2
        stones.append(s3)
    return stones[0]


def rotatedDigits(N):
    """
    788. 旋转数字
    我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。
    如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
    现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？
    示例:
    输入: 10
    输出: 4
    解释:
    在[1, 10]中有四个好数： 2, 5, 6, 9。
    注意 1 和 10 不是好数, 因为他们在旋转之后不变。
    注意:
    N 的取值范围是 [1, 10000]。
    :param N: int
    :return: int
    """
    correct = [0, 1, 2, 5, 6, 8, 9]
    exp = [0, 1, 8]
    ans, dec = 0, 0
    s = [int(x) for x in str(N)]
    n = len(s)
    for j in range(n):
        i = n - 1 - j
        x = s[j]
        plus = 0
        if not x in correct:
            for q in range(len(correct)):
                if correct[q] > x:
                    plus = q
                    break
            ans += plus * (7 ** i)
            break
        else:
            plus = correct.index(x)
            plus = plus + 1 if i == 0 else plus
            ans += plus * (7 ** i)
    print(ans)
    for j in range(n):
        i = n - 1 - j
        x = s[j]
        minus = 9
        if not x in exp:
            for q in range(len(exp)-1, -1, -1):
                if exp[q] < x:
                    minus = q + 1
                    break
            ans -= minus * (3 ** i)
            break
        else:
            minus = exp.index(x)
            minus = minus + 1 if i == 0 else minus
            ans -= minus * (3 ** i)
    print(ans)
    return ans


def maxDepth(root):
    """
    559. N叉树的最大深度
    给定一个 N 叉树，找到其最大深度。
    最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
    例如，给定一个 3叉树 :
            1
        3   2   4
      5   6
    我们应返回其最大深度，3。
    说明:
    树的深度不会超过 1000。
    树的节点总不会超过 5000。
    :param root: Node
    :return: int
    """
    if not root: return 0
    cur = 0
    for x in root.children:
        cur = max(maxDepth(x), cur)
    return cur + 1


def largestTriangleArea(points):
    """
    812. 最大三角形面积
    给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
    示例:
    输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    输出: 2
    解释:
    这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
    注意:
    3 <= points.length <= 50.
    不存在重复的点。
     -50 <= points[i][j] <= 50.
    结果误差值在 10^-6 以内都认为是正确答案。
    :param points: List[List[int]]
    :return: float
    """
    # 三层暴力 + 向量求平行四边形面积/2 or 海伦公式 p = (a+b+c)/2  area=sqrt(p*(p-a)*(p-b)*(p-c))
    area = 0
    for i in range(len(points) - 2):
        for k in range(i + 1, len(points) - 1):
            for m in range(k + 1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[k][0]
                y2 = points[k][1]
                x3 = points[m][0]
                y3 = points[m][1]
                area = max(area, abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)))
    return (area / 2)


def minMoves(nums):
    """
    453. 最小移动次数使数组元素相等
    给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
    示例:
    输入:
    [1,2,3]
    输出:
    3
    解释:
    只需要3次移动（注意每次移动会增加两个元素的值）：
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    :param nums: List[int]
    :return: int
    """
    # n-1加1分等价于1减1分
    m = min(nums)
    ans = 0
    for x in nums:
        ans += x - m
    return ans


def constructRectangle(area):
    """
    492. 构造矩形
    作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
    1. 你设计的矩形页面必须等于给定的目标面积。
    2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。
    3. 长度 L 和宽度 W 之间的差距应当尽可能小。
    你需要按顺序输出你设计的页面的长度 L 和宽度 W。
    示例：
    输入: 4
    输出: [2, 2]
    解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
    但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
    说明:
    给定的面积不大于 10,000,000 且为正整数。
    你设计的页面的长度和宽度必须都是正整数。
    :param area: int
    :return: List[int]
    """
    # 先开平方, 再从中间向两侧找因子对
    x = int(area ** 0.5)
    while x > 0 and area % x != 0:
        x -= 1
    return [area // x, x]


def dayOfYear(date):
    """
    1154. 一年中的第几天
    给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
    通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
    示例 1：
    输入：date = "2019-01-09"
    输出：9
    示例 2：
    输入：date = "2019-02-10"
    输出：41
    示例 3：
    输入：date = "2003-03-01"
    输出：60
    示例 4：
    输入：date = "2004-03-01"
    输出：61
    提示：
    date.length == 10
    date[4] == date[7] == '-'，其他的 date[i] 都是数字。
    date 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日。
    :param date: str
    :return: int
    """
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y, m, d = [int(x.lstrip('0')) for x in date.split("-")]
    p = 1 if y % 4 == 0 and y % 100 != 0 and m > 2 else 0
    res = sum(month_days[:m]) + d + p
    return res


def isLongPressedName(name, typed):
    """
    925. 长按键入
    你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
    你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
    示例 1：
    输入：name = "alex", typed = "aaleex"
    输出：true
    解释：'alex' 中的 'a' 和 'e' 被长按。
    示例 2：
    输入：name = "saeed", typed = "ssaaedd"
    输出：false
    解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
    示例 3：
    输入：name = "leelee", typed = "lleeelee"
    输出：true
    示例 4：
    输入：name = "laiden", typed = "laiden"
    输出：true
    解释：长按名字中的字符并不是必要的。
    提示：
    name.length <= 1000
    typed.length <= 1000
    name 和 typed 的字符都是小写字母。
    :param name: str
    :param typed: str
    :return: bool
    """
    i, j = 0, 0
    n = len(name)
    t = len(typed)
    while i < n and j < t:
        a, b = i, j
        while i < n - 1 and name[i] == name[i+1]:
            i += 1
        while j < t - 1 and typed[j] == typed[j+1]:
            j += 1
        if name[i] != typed[j] or i - a > j - b:
            return False
        if i == n - 1 and j == t - 1:
            return True
        i += 1
        j += 1
    return False


def fairCandySwap(A, B):
    """
    888. 公平的糖果交换
    爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。
    因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
    返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。
    如果有多个答案，你可以返回其中任何一个。保证答案存在。
    示例 1：
    输入：A = [1,1], B = [2,2]
    输出：[1,2]
    示例 2：
    输入：A = [1,2], B = [2,3]
    输出：[1,2]
    示例 3：
    输入：A = [2], B = [1,3]
    输出：[2,3]
    示例 4：
    输入：A = [1,2,5], B = [2,4]
    输出：[5,4]
    提示：
    1 <= A.length <= 10000
    1 <= B.length <= 10000
    1 <= A[i] <= 100000
    1 <= B[i] <= 100000
    保证爱丽丝与鲍勃的糖果总量不同。
    答案肯定存在。
    :param A: List[int]
    :param B: List[int]
    :return: List[int]
    """
    a, b = sum(A), sum(B)
    c = (a + b) // 2
    d = c - a
    B = set(B)
    for x in A:
        if x + d in B:
            return [x, x + d]



if __name__ == '__main__':
    print(fairCandySwap([35, 17, 4, 24, 10], [63, 21]))
    # print(isLongPressedName("saeedi", "ssaaeediixxxiii"))
    # ans = constructRectangle(6)
    # print(ans)
    # largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
    # rotatedDigits(9)
    # lastStoneWeight([2,7,4,1,8,1])
    # distributeCandies(10, 3)
    # tribonacci(25)
    # x, y = construct_tree_node([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]), construct_tree_node([2, 3, 5, 6, 1, 9, 8, null, null, 7, 0])
    # leafSimilar(x, y)
    pass
