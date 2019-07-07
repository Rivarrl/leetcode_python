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
    n = len(houses)
    m = len(heaters)
    houses.sort()
    heaters.sort()
    i, j = 0, 0
    ans = 0
    cur = float("inf")
    while i < n and j < m:
        while houses[i] > heaters[j]:


if __name__ == '__main__':
    findRadius([9,5,0,4,7], [5,4])
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