# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 简单题 4

def numberOfBoomerangs(points):
    """
    447. 回旋镖的数量
    给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
    找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。
    示例:
    输入:
    [[0,0],[1,0],[2,0]]
    输出:
    2
    解释:
    两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
    :param points: List[List[int]]
    :return: int
    """
    """
    # 终极暴力，超时
    n = len(points)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            x1 = abs(points[i][0] - points[j][0])
            y1 = abs(points[i][1] - points[j][1])
            z1 = x1 ** 2 + y1 ** 2
            for k in range(n):
                if i == k or j == k: continue
                x2 = abs(points[i][0] - points[k][0])
                y2 = abs(points[i][1] - points[k][1])
                z2 = x2**2 + y2**2
                if z1 == z2: ans += 1
    print(ans)
    return ans
    """
    # 优化：以每个点作为中心点记录与其他点的距离，存入哈希表中，C(2,n)中每两步之间相差2n， n*(n+1) = (n-1)*n + 2n
    n = len(points)
    ans = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x = abs(points[i][0] - points[j][0])
                y = abs(points[i][1] - points[j][1])
                z = x**2 + y**2
                if not z in d:
                    d[z] = 1
                else:
                    ans += d[z] * 2
                    d[z] += 1
        d = {}
    return ans


def canConstruct(ransomNote, magazine):
    """
    383. 赎金信
    给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
    (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
    注意：
    你可以假设两个字符串均只含有小写字母。
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
    :param ransomNote: str
    :param magazine: str
    :return: bool
    """
    d = [0] * 26
    for x in magazine:
        d[ord(x) - ord('a')] += 1
    for x in ransomNote:
        if d[ord(x) - ord('a')] == 0:
            return False
        d[ord(x) - ord('a')] -= 1
    return True


def longestPalindrome(s):
    """
    409. 最长回文串
    给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
    在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
    注意:
    假设字符串的长度不会超过 1010。
    示例 1:
    输入:
    "abccccdd"
    输出:
    7
    解释:
    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
    :param s: str
    :return: int
    """
    """
    # 计数, A在前, a在后  30%
    d = [0] * 52
    a, z, A, Z = ord('a'), ord('z'), ord('A'), ord('Z')
    for x in s:
        if A <= ord(x) <= Z:
            d[ord(x)-A] += 1
        else:
            d[26 + ord(x)-a] += 1
    ans = 0
    flag = False
    for x in d:
        if x % 2 == 1:
            ans += x - 1
            flag = True
        else:
            ans += x
    ans += (not not flag)
    print(d)
    print(ans)
    return ans
    """
    # 使用set, x出现过就执行ans+2, 删掉x  30%
    d = set()
    ans = 0
    for x in s:
        if x in d:
            ans += 2
            d.remove(x)
        else:
            d.add(x)
    ans += (not not d)
    print(ans)
    return ans


def firstUniqChar(s):
    """
    387. 字符串中的第一个唯一字符
    给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    案例:
    s = "leetcode"
    返回 0.
    s = "loveleetcode",
    返回 2.
    注意事项：您可以假定该字符串只包含小写字母。
    :param s: str
    :return: int
    """
    """
    # 哈希表存字符对应位置，重复值置-1 30%
    d = {}
    n = len(s)
    for i in range(n):
        if not s[i] in d:
            d[s[i]] = i
        else:
            d[s[i]] = -1
    for v in d.values():
        if v >= 0: return v
    return -1
    """
    # 按小写字母顺序遍历，用左查找 = 右查找且查找值不为-1来确定有且只有一个该字符 88%
    n = len(s)
    m = n
    for i in range(26):
        x = chr(ord('a') + i)
        if s.find(x) >= 0 and s.find(x) == s.rfind(x):
            j = s.index(x)
            if j < m: m = j
    return -1 if m == n else m


def toHex(num):
    """
    405. 数字转换为十六进制数
    给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
    注意:
    十六进制中所有字母(a-f)都必须是小写。
    十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
    给定的数确保在32位有符号整数范围内。
    不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
    示例 1：
    输入:
    26
    输出:
    "1a"
    示例 2：
    输入:
    -1
    输出:
    "ffffffff"
    :param num: int
    :return: str
    """
    """
    # 利用python的数字取值范围64位，加2^32不会越界 73%
    if num == 0: return "0"
    hexs = "0123456789abcdef"
    res = []
    if num < 0: num += 2**32
    while num > 0:
        cur = num % 16
        res.append(hexs[cur])
        num //= 16
    return ''.join(res[::-1])
    """
    # 利用位运算, 用0xf从低到高4位4位与取值, 右移左边补位: 正数补0，负数补1 27%
    if num == 0: return "0"
    hexs = "0123456789abcdef"
    res = []
    while num and len(res) < 8:
        res.append(hexs[num & 0xf])
        num >>= 4
    return ''.join(res[::-1])


def diameterOfBinaryTree(root):
    """
    543. 二叉树的直径
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
    示例 :
    给定二叉树
          1
         / \
        2   3
       / \
      4   5
    返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
    注意：两结点之间的路径长度是以它们之间边的数目表示。
    :param root: TreeNode
    :return: int
    """
    def helper(p):
        if not p: return -1
        left = helper(p.left)
        right = helper(p.right)
        cur = left + right + 2
        if cur > ans[0]:
            ans[0] = cur
        return max(left, right) + 1

    ans = [0]
    helper(root)
    return ans[0]


def isUnivalTree(root):
    """
    965. 单值二叉树
    如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
    只有给定的树是单值二叉树时，才返回 true；否则返回 false。
    示例 1：
    输入：[1,1,1,1,1,null,1]
    输出：true
    示例 2：
    输入：[2,2,2,5,2]
    输出：false
    提示：
    给定树的节点数范围是 [1, 100]。
    每个节点的值都是整数，范围为 [0, 99] 。
    :param root: TreeNode
    :return: bool
    """
    def helper(p):
        if not p: return
        helper(p.left)
        helper(p.right)
        s.add(p.val)
    s = set()
    helper(root)
    return len(s) == 1


def findAnagrams(s, p):
    """
    438. 找到字符串中所有字母异位词
    给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
    字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
    说明：
    字母异位词指字母相同，但排列不同的字符串。
    不考虑答案输出的顺序。
    示例 1:
    输入:
    s: "cbaebabacd" p: "abc"
    输出:
    [0, 6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
    示例 2:
    输入:
    s: "abab" p: "ab"
    输出:
    [0, 1, 2]
    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
    :param s: str
    :param p: str
    :return: List[int]
    """
    def helper(d):
        for k, v in d.items():
            if v != 0: return False
        return True
    n = len(p)
    ns = len(s)
    if ns < n: return []
    res = []
    d = {chr(i+ord('a')):0 for i in range(26)}
    for i in range(n):
        d[s[i]] += 1
        d[p[i]] -= 1
    if helper(d):
        res.append(0)
    for i in range(n, len(s)):
        d[s[i]] += 1
        d[s[i-n]] -= 1
        if helper(d):
            res.append(i-n+1)
    return res


def rotateString(A, B):
    """
    796. 旋转字符串
    给定两个字符串, A 和 B。
    A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
    示例 1:
    输入: A = 'abcde', B = 'cdeab'
    输出: true
    示例 2:
    输入: A = 'abcde', B = 'abced'
    输出: false
    :param A: str
    :param B: str
    :return: bool
    """
    return len(A) == len(B) and B in A + A


def numMovesStones(a, b, c):
    """
    1033. 移动石子直到连续三枚石子放置在数轴上，位置分别为 a，b，c。
    每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。
    当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
    要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
    示例 1：
    输入：a = 1, b = 2, c = 5
    输出：[1, 2]
    解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
    示例 2：
    输入：a = 4, b = 3, c = 2
    输出：[0, 0]
    解释：我们无法进行任何移动。
    提示：
    1 <= a <= 100
    1 <= b <= 100
    1 <= c <= 100
    a != b, b != c, c != a
    :param a: int
    :param b: int
    :param c: int
    :return: List[int]
    """
    x, y, z = sorted([a,b,c])
    xy = y - x - 1
    yz = z - y - 1
    M = xy + yz
    m = 2
    if x == y - 2 or z == y + 2:
        m -= 1
    else:
        if x == y - 1:
            m -= 1
        if z == y + 1:
            m -= 1
    return [m,M]


def search(nums, target):
    """
    704. 二分查找
    给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
    示例 1:
    输入: nums = [-1,0,3,5,9,12], target = 9
    输出: 4
    解释: 9 出现在 nums 中并且下标为 4
    示例 2:
    输入: nums = [-1,0,3,5,9,12], target = 2
    输出: -1
    解释: 2 不存在 nums 中因此返回 -1
    提示：
    你可以假设 nums 中的所有元素是不重复的。
    n 将在 [1, 10000]之间。
    nums 的每个元素都将在 [-9999, 9999]之间。
    :param nums: List[int]
    :param target: int
    :return: int
    """
    ans = -1
    i, j = 0, len(nums) - 1
    while i <= j:
        m = i + (j - i >> 1)
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            ans = m
            break
    return ans


def findMaxConsecutiveOnes(nums):
    """
    485. 最大连续1的个数
    给定一个二进制数组， 计算其中最大连续1的个数。
    示例 1:
    输入: [1,1,0,1,1,1]
    输出: 3
    解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
    注意：
    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。
    :param nums: List[int]
    :return: int
    """
    ans, cur = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cur += 1
        else:
            ans = max(cur, ans)
            cur = 0
    return ans


def checkPerfectNumber(num):
    """
    507. 完美数
    对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
    给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
    示例：
    输入: 28
    输出: True
    解释: 28 = 1 + 2 + 4 + 7 + 14
    注意:
    输入的数字 n 不会超过 100,000,000. (1e8)
    :param num: int
    :return: bool
    """
    if num <= 1: return False
    x = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            x += i + num // i
    return x == num


def findRelativeRanks(nums):
    """
    506. 相对名次
    给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
    (注：分数越高的选手，排名越靠前。)
    示例 1:
    输入: [5, 4, 3, 2, 1]
    输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
    余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
    提示:
    N 是一个正整数并且不会超过 10000。
    所有运动员的成绩都不相同。
    :param nums: List[int]
    :return: List[str]
    """
    n = len(nums)
    res = ["1"] * n
    d = {"1":"Gold Medal", "2":"Silver Medal", "3":"Bronze Medal"}
    idx_nums = sorted([(nums[i], i) for i in range(n)], reverse=True)
    rk = 1
    for x, i in idx_nums:
        res[i] = str(rk) if not str(rk) in d else d[str(rk)]
        rk += 1
    return res


def findRadius(houses, heaters):
    """
    475. 供暖器
    冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
    现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
    所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
    说明:
    给出的房屋和供暖器的数目是非负数且不会超过 25000。
    给出的房屋和供暖器的位置均是非负数且不会超过10^9。
    只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
    所有供暖器都遵循你的半径标准，加热的半径也一样。
    示例 1:
    输入: [1,2,3],[2]
    输出: 1
    解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
    示例 2:
    输入: [1,2,3,4],[1,4]
    输出: 1
    解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
    :param houses: List[int]
    :param heaters: List[int]
    :return: int
    """
    """
    # 相关标签提到的二分查找，思路是预设答案的上下界0，和max(houses)，二分查找着正确答案，如果当前x值满足供暖需求，正确答案就在0~x之间，否则在x~max之间 5%
    def can_heat(x):
        i, j = 0, 0
        while i < n and j < m:
            l, r = heaters[j] - x, heaters[j] + x
            while i < n and l <= houses[i] <= r:
                i += 1
            j += 1
        return i == n

    n = len(houses)
    m = len(heaters)
    houses.sort()
    heaters.sort()
    i, j = 0, max(max(houses), max(heaters))
    while i<j:
        mid = i + (j - i >> 1)
        if can_heat(mid):
            j = mid
        else:
            i = mid + 1
    return j
    """
    # 在暴力的基础上优化，heaters用指针 74%
    ans = 0
    j = 0
    houses.sort()
    heaters.sort()
    for i in range(len(houses)):
        cur = abs(houses[i] - heaters[j])
        while j < len(heaters) - 1 and abs(heaters[j + 1] - houses[i]) <= cur:
            cur = abs(heaters[j+1] - houses[i])
            j += 1
        ans = max(cur, ans)
    return ans


def thirdMax(nums):
    """
    414. 第三大的数
    给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
    示例 1:
    输入: [3, 2, 1]
    输出: 1
    解释: 第三大的数是 1.
    示例 2:
    输入: [1, 2]
    输出: 2
    解释: 第三大的数不存在, 所以返回最大的数 2 .
    示例 3:
    输入: [2, 2, 3, 1]
    输出: 1
    解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
    存在两个值为2的数，它们都排第二。
    :param nums: List[int]
    :return: int
    """
    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    for num in nums:
        if num > max1:
            max3, max2 = max2, max1
            max1 = num
        elif max2 < num < max1:
            max3 = max2
            max2 = num
        elif max3 < num < max2:
            max3 = num
    return max1 if max3 == float('-inf') else max3


def transpose(A):
    """
    867. 转置矩阵
    给定一个矩阵 A， 返回 A 的转置矩阵。
    矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
    示例 1：
    输入：[[1,2,3],[4,5,6],[7,8,9]]
    输出：[[1,4,7],[2,5,8],[3,6,9]]
    示例 2：
    输入：[[1,2,3],[4,5,6]]
    输出：[[1,4],[2,5],[3,6]]
    提示：
    1 <= A.length <= 1000
    1 <= A[0].length <= 1000
    :param A: List[int]
    :return: List[int]
    """
    n = len(A)
    if n == 0: return A
    m = len(A[0])
    B = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            B[i][j] = A[j][i]
    return B


def surfaceArea(grid):
    """
    892. 三维形体的表面积
    在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
    每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
    请你返回最终形体的表面积。
    示例 1：
    输入：[[2]]
    输出：10
    示例 2：
    输入：[[1,2],[3,4]]
    输出：34
    示例 3：
    输入：[[1,0],[0,2]]
    输出：16
    示例 4：
    输入：[[1,1,1],[1,0,1],[1,1,1]]
    输出：32
    示例 5：
    输入：[[2,2,2],[2,1,2],[2,2,2]]
    输出：46
    提示：
    1 <= N <= 50
    0 <= grid[i][j] <= 50
    :param grid: List[List[int]]
    :return: int
    """
    n = len(grid)
    if n == 0: return 0
    m = len(grid[0])
    each_sum = lambda x: 0 if x == 0 else 4 * x + 2
    es, cs = 0, 0
    for i in range(n):
        for j in range(m):
            es += each_sum(grid[i][j])
            down = 0 if i == n - 1 else min(grid[i][j], grid[i+1][j])
            right = 0 if j == m - 1 else min(grid[i][j], grid[i][j+1])
            cs += right + down
    ans = es - cs * 2
    return ans


def singleNumber(nums):
    """
    136. 只出现一次的数字
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    示例 1:
    输入: [2,2,1]
    输出: 1
    示例 2:
    输入: [4,1,2,1,2]
    输出: 4
    :param nums: List[int]
    :return: int
    """
    ans = 0
    for x in nums:
        ans ^= x
    return ans


def relativeSortArray(arr1, arr2):
    """
    1122. 数组的相对排序
    给你两个数组，arr1 和 arr2，
    arr2 中的元素各不相同
    arr2 中的每个元素都出现在 arr1 中
    对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
    示例：
    输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    输出：[2,2,2,1,4,3,3,9,6,7,19]
    提示：
    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    arr2 中的元素 arr2[i] 各不相同
    arr2 中的每个元素 arr2[i] 都出现在 arr1 中
    :param arr1: List[int]
    :param arr2: List[int]
    :return: List[int]
    """
    d = {}
    tail = []
    for i, x in enumerate(arr2):
        d[x] = [i, 0]
    for i, x in enumerate(arr1):
        if x in d:
            d[x][1] += 1
        else:
            tail.append(x)
    res = []
    for i, x in enumerate(arr2):
        res += [x] * d[x][1]
    tail.sort()
    return res + tail


def findTilt(root):
    """
    563. 二叉树的坡度
    给定一个二叉树，计算整个树的坡度。
    一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
    整个树的坡度就是其所有节点的坡度之和。
    示例:
    输入:
             1
           /   \
          2     3
    输出: 1
    解释:
    结点的坡度 2 : 0
    结点的坡度 3 : 0
    结点的坡度 1 : |2-3| = 1
    树的坡度 : 0 + 0 + 1 = 1
    注意:
    任何子树的结点的和不会超过32位整数的范围。
    坡度的值不会超过32位整数的范围。
    :param root: TreeNode
    :return: int
    """
    def helper(node):
        if not node:
            return 0, 0
        left = helper(node.left)
        right = helper(node.right)
        tilt = abs(left[1] - right[1])
        nonlocal ans
        ans += tilt
        return tilt, left[1] + right[1] + node.val
    ans = 0
    helper(root)
    return ans


def findLUSlength(a, b):
    """
    521. 最长特殊序列 Ⅰ
    给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
    子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
    输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。
    示例 :
    输入: "aba", "cdc"
    输出: 3
    解析: 最长特殊序列可为 "aba" (或 "cdc")
    说明:
    两个字符串长度均小于100。
    字符串中的字符仅含有 'a'~'z'。
    :param a: str
    :param b: str
    :return: int
    """
    return -1 if a == b else max(len(a), len(b))


def checkRecord(s):
    """
    551. 学生出勤记录 I
    给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
    'A' : Absent，缺勤
    'L' : Late，迟到
    'P' : Present，到场
    如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
    你需要根据这个学生的出勤记录判断他是否会被奖赏。
    示例 1:
    输入: "PPALLP"
    输出: True
    示例 2:
    输入: "PPALLL"
    输出: False
    :param s: str
    :return: bool
    """
    return s.count('A') <= 1 and s.count('LL') == 0


def intersect(quadTree1, quadTree2):
    """
    558. 四叉树交集
    四叉树是一种树数据，其中每个结点恰好有四个子结点：topLeft、topRight、bottomLeft 和 bottomRight。四叉树通常被用来划分一个二维空间，递归地将其细分为四个象限或区域。
    我们希望在四叉树中存储 True/False 信息。四叉树用来表示 N * N 的布尔网格。对于每个结点, 它将被等分成四个孩子结点直到这个区域内的值都是相同的。每个节点都有另外两个布尔属性：isLeaf 和 val。当这个节点是一个叶子结点时 isLeaf 为真。val 变量储存叶子结点所代表的区域的值。
    例如，下面是两个四叉树 A 和 B：
    A:
    +-------+-------+   T: true
    |       |       |   F: false
    |   T   |   T   |
    |       |       |
    +-------+-------+
    |       |       |
    |   F   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight: T
    bottomLeft: F
    bottomRight: F
    B:
    +-------+---+---+
    |       | F | F |
    |   T   +---+---+
    |       | T | T |
    +-------+---+---+
    |       |       |
    |   T   |   F   |
    |       |       |
    +-------+-------+
    topLeft: T
    topRight:
         topLeft: F
         topRight: F
         bottomLeft: T
         bottomRight: T
    bottomLeft: T
    bottomRight: F
    你的任务是实现一个函数，该函数根据两个四叉树返回表示这两个四叉树的逻辑或(或并)的四叉树。
    A:                 B:                 C (A or B):
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       | F | F |  |       |       |
    |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
    |       |       |  |       | T | T |  |       |       |
    +-------+-------+  +-------+---+---+  +-------+-------+
    |       |       |  |       |       |  |       |       |
    |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
    |       |       |  |       |       |  |       |       |
    +-------+-------+  +-------+-------+  +-------+-------+
    提示：
    A 和 B 都表示大小为 N * N 的网格。
    N 将确保是 2 的整次幂。
    如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。
    逻辑或的定义如下：如果 A 为 True ，或者 B 为 True ，或者 A 和 B 都为 True，则 "A 或 B" 为 True。
    :param quadTree1: QuadNode
    :param quadTree2: QuadNode
    :return: QuadNode
    """
    if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and not quadTree2.val):
        return quadTree1
    elif (quadTree1.isLeaf and not quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
        return quadTree2
    else:
        tl = intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = intersect(quadTree1.topRight, quadTree2.topRight)
        bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        return QuadNode(True, True, None, None, None, None) if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val and tr.val and bl.val and br.val else QuadNode(False, False, tl, tr, bl, br)


def addStrings(num1, num2):
    """
    415. 字符串相加
    给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
    注意：
    num1 和num2 的长度都小于 5100.
    num1 和num2 都只包含数字 0-9.
    num1 和num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库，也不能直接将输入的字符串转换为整数形式。
    :param num1: str
    :param num2: str
    :return: str
    """
    digit_plus = False
    n1, n2 = len(num1), len(num2)
    if n1 < n2:
        num1, num2 = num2, num1
        n1, n2 = n2, n1
    i, j = n1 - 1, n2 - 1
    res = []
    while i >= 0:
        c1 = ord(num1[i]) - ord('0')
        c2 = 0 if j < 0 else ord(num2[j]) - ord('0')
        cur = c1 + c2 + digit_plus
        if cur > 9:
            cur -= 10
            digit_plus = 1
        else:
            digit_plus = 0
        res.insert(0, str(cur))
        i -= 1
        j -= 1
    ans = ''.join(res)
    return '1' + ans if digit_plus else ans


def defangIPaddr(address):
    """
    1108. IP 地址无效化
    给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
    所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
    示例 1：
    输入：address = "1.1.1.1"
    输出："1[.]1[.]1[.]1"
    示例 2：
    输入：address = "255.100.50.0"
    输出："255[.]100[.]50[.]0"
    提示：
    给出的 address 是一个有效的 IPv4 地址
    :param address: str
    :return: str
    """
    res = ""
    for i, x in enumerate(address):
        if address[i] == '.':
            res = "%s[.]" % res
        else:
            res = "%s%s" % (res, address[i])
    return res


def duplicateZeros(arr):
    """
    1089. 复写零
    给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
    注意：请不要在超过该数组长度的位置写入元素。
    要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。
    示例 1：
    输入：[1,0,2,3,0,4,5,0]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
    示例 2：
    输入：[1,2,3]
    输出：null
    解释：调用函数后，输入的数组将被修改为：[1,2,3]
    提示：
    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
    :param arr: List[int]
    :return: None
    """
    """
    # 36%
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            arr.pop()
            arr.insert(i, 0)
            i += 1
        i += 1
    print(arr)
    """
    # 100%
    tmp = [x for x in arr]
    i = 0
    for x in tmp:
        if x == 0:
            if i < len(arr):
                arr[i] = 0
                i += 1
        if i < len(arr):
            arr[i] = x
            i += 1


def countSegments(s):
    """
    434. 字符串中的单词数
    统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
    请注意，你可以假定字符串里不包括任何不可打印的字符。
    示例:
    输入: "Hello, my name is John"
    输出: 5
    :param s: str
    :return: int
    """
    # 一行
    # return len(list(filter(lambda x: x.strip() != '', s.split(' '))))
    # 常规
    b, ans = False, 0
    for i in range(len(s)):
        if s[i] == ' ':
            if b:
                ans += 1
            b = False
        else:
            b = True
    print(ans)
    return ans + (not not b)


def getMinimumDifference(root):
    """
    530. 二叉搜索树的最小绝对差
    给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
    示例 :
    输入:
       1
        \
         3
        /
       2
    输出:
    1
    解释:
    最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
    注意: 树中至少有2个节点。
    :param root: TreeNode
    :return: int
    """
    """
    # 中序遍历并记录
    def helper(node):
        if node.left:
            helper(node.left)
        nonlocal ans, last
        ans, last = min(ans, node.val - last), node.val
        if node.right:
            helper(node.right)
    last, ans = -float("inf"), float("inf")
    if root:
        helper(root)
    return ans if ans != float("inf") else 0
    """
    # 二叉搜索树 离当前节点的值最近的值在左子的最右子和右子的最左子中
    def get_deepest_right(node):
        while node.right:
            node = node.right
        return node.val
    def get_deepest_left(node):
        while node.left:
            node = node.left
        return node.val
    def helper(node):
        if not node: return INF
        left_right = get_deepest_right(node.left) if node.left else -INF
        right_left = get_deepest_left(node.right) if node.right else INF
        return min(node.val - left_right, right_left - node.val, helper(node.left), helper(node.right))

    INF = float("inf")
    ans = helper(root)
    return ans


def findPairs(nums, k):
    """
    532. 数组中的K-diff数对
    给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.
    示例 1:
    输入: [3, 1, 4, 1, 5], k = 2
    输出: 2
    解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
    尽管数组中有两个1，但我们只应返回不同的数对的数量。
    示例 2:
    输入:[1, 2, 3, 4, 5], k = 1
    输出: 4
    解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
    示例 3:
    输入: [1, 3, 1, 5, 4], k = 0
    输出: 1
    解释: 数组中只有一个 0-diff 数对，(1, 1)。
    注意:
    数对 (i, j) 和数对 (j, i) 被算作同一数对。
    数组的长度不超过10,000。
    所有输入的整数的范围在 [-1e7, 1e7]。
    :param nums: List[int]
    :param k: int
    :return: int
    """
    """
    # 0的情况单独处理
    ans = 0
    if k < 0: return 0
    if k == 0:
        d = {}
        for x in nums:
            if not x in d:
                d[x] = 0
            else:
                d[x] += 1
                if d[x] == 1:
                    ans += 1
    else:
        nums = set(nums)
        for x in nums:
            if x - k in nums:
                ans += 1
    return ans
    """
    # 将0的情况简化
    if k < 0: return 0
    d = {}
    inf = float("inf")
    for x in nums:
        if x - k in d:
            d[x-k] = x
        if x + k in d:
            d[x] = x + k
        if not x in d:
            d[x] = -inf
    return len(list(filter(lambda x: x != -inf, d.values())))


def reverseStr(s, k):
    """
    541. 反转字符串 II
    给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
    示例:
    输入: s = "abcdefg", k = 2
    输出: "bacdfeg"
    要求:
    该字符串只包含小写的英文字母。
    给定字符串的长度和 k 在[1, 10000]范围内。
    :param s: str
    :param k: int
    :return: str
    """
    res = []
    n = len(s)
    i = 0
    k = min(n, k)
    last, cur = 0, k
    while i < n:
        j = cur - i + last - 1 if last <= i < cur else i
        res.append(s[j])
        i += 1
        if i == cur:
            last = min(n, last + 2 * k)
            cur = min(n, cur + 2 * k)
    a = "".join(res)
    return a


def isSubtree(s, t):
    """
    572. 另一个树的子树
    给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
    示例 1:
    给定的树 s:
         3
        / \
       4   5
      / \
     1   2
    给定的树 t：
       4
      / \
     1   2
    返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
    示例 2:
    给定的树 s：
         3
        / \
       4   5
      / \
     1   2
        /
       0
    给定的树 t：
       4
      / \
     1   2
    返回 false。
    :param s: TreeNode
    :param t: TreeNode
    :return: bool
    """
    """
    # 递归判断 73%
    def helper(s, t):
        if not s and not t: return True
        if s and t:
            return helper(s.left, t.left) and helper(s.right, t.right) and s.val == t.val
        return False
    def inner(s):
        if not s: return False
        if helper(s, t): return True
        return inner(s.left) or inner(s.right)
    return inner(s)
    """
    # t的先序遍历的结果包含在s先序遍历的结果中 100%
    def helper(node, res):
        if not node:
            res.append("#")
            return
        res.append("$"+str(node.val))
        helper(node.left, res)
        helper(node.right, res)
    sr, tr = [], []
    helper(s, sr)
    helper(t, tr)
    ss, ts = "".join(sr), "".join(tr)
    return ss.find(ts) >= 0


if __name__ == '__main__':
    x = construct_tree_node([3,4,5,1,2,null,null,null,null,0])
    y = construct_tree_node([4,1,2])
    print(isSubtree(x, y))
    # reverseStr("abcdefgh", 3)
    # findPairs([-1,-2,-3], 1)
    # x = construct_tree_node([1,null,3,null,null,2])
    # getMinimumDifference(x)
    # countSegments("        ")
    # addStrings("9", "99")
    # x = construct_tree_node([1,2,3])
    # findTilt(x)
    # relativeSortArray([26,21,11,20,50,34,1,18], [21,11,26,20])
    # surfaceArea([[2,2,2],[2,1,2],[2,2,2]])
    # transpose([[1,2,3],[4,5,6]])
    # findRadius([1,5], [10])
    # findRelativeRanks([10,3,8,9,4])
    # checkPerfectNumber(28)
    # numMovesStones(1,5,2)
    # print(rotateString("abcde", "cdeab"))
    # findAnagrams("abaacbabc", "abc")
    # x = construct_tree_node([1, 1, 1, 1, 1, null, null])
    # print(isUnivalTree(x))
    # x = construct_tree_node([1, 2, 3, 4, 5, null, null])
    # print(diameterOfBinaryTree(x))
    # x = -1
    # toHex(x)
    # a = "leetcode"
    # firstUniqChar(a)
    # longestPalindrome(a)
    # numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
    pass