# -*- coding:utf-8 -*-
from algorithm_utils import *


# leetcode 简单题

def mergeTrees(t1, t2):
    """
    617. 合并二叉树
    给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
    你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
    输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
    输出:
    合并后的树:
             3
            / \
           4   5
          / \   \
         5   4   7
    :param t1: TreeNode
    :param t2: TreeNode
    :return: TreeNode
    """
    if t1 == None and t2 == None:
        return None
    v = (0 if t1 == None else t1.val) + (0 if t2 == None else t2.val)
    p = TreeNode(v)
    l = mergeTrees(None if t1 == None else t1.left, None if t2 == None else t2.left)
    r = mergeTrees(None if t1 == None else t1.right, None if t2 == None else t2.right)
    p.left = l
    p.right = r
    return p


def uniqueMorseRepresentations(words):
    """
    804. 唯一摩尔斯密码词
    国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如: "a" 对应 ".-", "b" 对应 "-...", "c" 对应 "-.-.", 等等。
    为了方便，所有26个英文字母对应摩尔斯密码表如下：
    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，"cab" 可以写成 "-.-..--..."，(即 "-.-." + "-..." + ".-"字符串的结合)。我们将这样一个连接过程称作单词翻译。
    返回我们可以获得所有词不同单词翻译的数量。
    例如:
    输入: words = ["gin", "zen", "gig", "msg"]
    输出: 2
    解释:
    各单词翻译如下:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    共有 2 种不同翻译, "--...-." 和 "--...--.".
    :param words: List[str]
    :return: int
    """
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.",
             "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    a = ord('a')
    d = []
    for word in words:
        x = ""
        for letter in word:
            x = "%s%s" % (x, morse[ord(letter) - a])
        d.append(x)
    return len(set(d))


def sortedSquares(A):
    """
    977. 有序数组的平方
    给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
    示例 1：
    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    示例 2：
    输入：[-7,-3,2,3,11]
    输出：[4,9,9,49,121]
    提示：
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A 已按非递减顺序排序。
    :param A: List[int]
    :return: List[int]
    """
    l = len(A)
    i, j, k = 0, l - 1, l - 1
    res = [0] * l
    while i <= j:
        if abs(A[i]) >= abs(A[j]):
            res[k] = A[i] ** 2
            i += 1
            k -= 1
        else:
            res[k] = A[j] ** 2
            j -= 1
            k -= 1
    return res


def diStringMatch(S):
    """
    942. 增减字符串匹配
    给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
    返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
    如果 S[i] == "I"，那么 A[i] < A[i+1]
    如果 S[i] == "D"，那么 A[i] > A[i+1]
    示例 1：
    输入："IDID"
    输出：[0,4,1,3,2]
    示例 2：
    输入："III"
    输出：[0,1,2,3]
    示例 3：
    输入："DDI"
    输出：[3,2,0,1]
    :param S: str
    :return: List[int]
    """
    l = S.__len__()
    res = [0] * (l + 1)
    k, p = 0, l
    for i in range(l):
        if S[i] == "D":
            res[i] = p
            p -= 1
        if S[i] == "I":
            res[i] = k
            k += 1
    res[-1] = S.replace("D", "").__len__()
    return res


def deleteNode(node):
    """
    237. 删除链表中的节点
    请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
    现有一个链表 -- head = [4,5,1,9]，它可以表示为: 4->5->1->9
    示例 1:
    输入: head = [4,5,1,9], node = 5
    输出: [4,1,9]
    解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
    示例 2:
    输入: head = [4,5,1,9], node = 1
    输出: [4,5,9]
    解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
    说明:
    链表至少包含两个节点。
    链表中所有节点的值都是唯一的。
    给定的节点为非末尾节点并且一定是链表中的一个有效节点。
    不要从你的函数中返回任何结果。
    :param node: ListNode
    :return: None
    """
    node.val = node.next.val
    node.next = node.next.next

def removeOuterParentheses(S):
    """
    1021. 删除最外层的括号
    有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
    如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
    给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
    对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。
    示例 1：
    输入："(()())(())"
    输出："()()()"
    解释：
    输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
    删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
    示例 2：
    输入："(()())(())(()(()))"
    输出："()()()()(())"
    解释：
    输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
    删除每隔部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
    示例 3：
    输入："()()"
    输出：""
    解释：
    输入字符串为 "()()"，原语化分解得到 "()" + "()"，
    删除每个部分中的最外层括号后得到 "" + "" = ""。
    :param S: str
    :return: str
    """
    stack = ["*"]
    l = len(S)
    res = [x for x in S]
    i, j = 0, l - 1
    while i <= j:
        if res[i] == "(":
            stack.append(i)
        elif stack[-1] != "*" and res[i] == ")":
            k = stack.pop(-1)
            if stack[-1] == "*":
                res.pop(i)
                res.pop(k)
                i -= 2
                j -= 2
        i += 1
    return "".join(res)


def invertTree(root):
    """
    226. 翻转二叉树
    翻转一棵二叉树。
    示例：
    输入：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    输出：
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
    :param root: TreeNode
    :return: TreeNode
    """
    if root:
        l = root.left
        root.left = root.right
        root.right = l
        invertTree(root.left)
        invertTree(root.right)
    return root


def findComplement(num):
    """
    476. 数字的补数
    给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
    注意:
    给定的整数保证在32位带符号整数的范围内。
    你可以假定二进制数不包含前导零位。
    示例 1:
    输入: 5
    输出: 2
    解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
    示例 2:
    输入: 1
    输出: 0
    解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
    :param num: int
    :return: int
    """
    n = num
    x = 2
    while n // x > 0:
        x *= 2
    return num^(x-1)


def selfDividingNumbers(left, right):
    """
    728. 自除数
    自除数 是指可以被它包含的每一位数除尽的数。
    例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
    还有，自除数不允许包含 0 。
    给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
    示例 1：
    输入：
    上边界left = 1, 下边界right = 22
    输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    注意：
    每个输入参数的边界满足 1 <= left <= right <= 10000。
    :param left: int
    :param right: int
    :return: List[int]
    """
    def inner(x):
        s = list(set(a for a in str(x)))
        for a in s:
            a = int(a)
            if a == 0:
                return False
            if x % a > 0:
                return False
        return True
    res = []
    for x in range(left, right + 1):
        if inner(x):
            res.append(x)
    return res


def preorder(root):
    """
    589. N叉树的前序遍历
    递归法
    :param root: Node
    :return: List[int]
    """
    def inner(root):
        if root:
            res.append(root.val)
            for child in root.children:
                inner(child)
    res = []
    inner(root)
    return res


def preorder2(root):
    """
    589. N叉树的前序遍历
    迭代法
    :param root: Node
    :return: List[int]
    """
    if not root:
        return []
    st = []
    res = []
    st.append(root)
    while st:
        top = st.pop()
        res.append(top.val)
        for c in top.children[::-1]:
            st.append(c)
    return res


def postorder(root):
    """
    590. N叉树的后序遍历
    递归法
    :param root: Node
    :return: List[int]
    """
    def inner(root):
        if root:
            for child in root.children:
                inner(child)
            res.append(root.val)
    res = []
    inner(root)
    return res


def postorder2(root):
    """
    590. N叉树的后序遍历
    迭代法
    :param root: Node
    :return: List[int]
    """
    res = []
    if root:
        stack = []
        stack.append([root, 0])
        while stack:
            p = stack[-1]
            if p[1] == 0 and len(p[0].children) > 0:
                stack[-1] = [p[0], 1]
                for child in p[0].children[::-1]:
                    stack.append([child, 0])
            else:
                res.append(p[0].val)
                stack.pop()
    return res

def levelOrder(root):
    """
    429. N叉树的层序遍历
    :param root: Node
    :return: List[List[int]]
    """
    def inner(root, level):
        if root:
            if level > len(res) - 1:
                res.append([])
            res[level].append(root.val)
            level += 1
            for child in root.children:
                inner(child, level)
    res = []
    inner(root, 0)
    return res


def repeatedNTimes(A):
    """
    961. 重复 N 次的元素
    在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
    返回重复了 N 次的那个元素。
    示例 1：
    输入：[1,2,3,3]
    输出：3
    示例 2：
    输入：[2,1,2,5,3,2]
    输出：2
    示例 3：
    输入：[5,1,5,2,5,3,5,4]
    输出：5
    提示：
    4 <= A.length <= 10000
    0 <= A[i] < 10000
    A.length 为偶数
    思路:
    1. 排序之后结果必在A[len//2]和A[len//2-1]之间
    如果两值相等直接返回，不等则证明A[:len//2-1]与A[len//2:]的其中一个都是相等的值,用A[len//2-1]与A[0]相比相等返回A[len//2-1]否则返回A[len//2]
    2. 已知有len/2的数字相等，那么存在两种情况，一种是重复数a存在相邻情况，如xyaaza，这种情况直接for循环比较得出
    另一种是axayaz或zayaxa这种相间排列的，这种情况返回A[0]或A[-1]，进一步观察如果A[0] = A[-1] or A[-2]时返回A[0]否则返回A[-1]
    :param A: List[int]
    :return: int
    """
    l = len(A)
    for i in range(1, l):
        if A[i] == A[i - 1]:
            return A[i]
    return A[0] if A[0] == A[-1] or A[0] == A[-2] else A[-1]


def searchBST(root, val):
    """
    700. 二叉搜索树中的搜索
    给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
    :param root: TreeNode
    :param val: int
    :return: TreeNode
    """
    if root == None:
        return None
    if root.val == val:
        return root
    elif root.val < val:
        return searchBST(root.right, val)
    else:
        return searchBST(root.left, val)


def minDeletionSize(A):
    """
    944. 删列造序
    给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
    选取一个删除索引序列，对于 A 中的每个字符串，删除对应每个索引处的字符。 所余下的字符串行从上往下读形成列。
    比如，有 A = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。（形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。
    假设，我们选择了一组删除索引 D，那么在执行删除操作之后，A 中所剩余的每一列都必须是 非降序 排列的，然后请你返回 D.length 的最小可能值。
    示例 1：
    输入：["cba", "daf", "ghi"]
    输出：1
    解释：
    当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
    若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
    示例 2：
    输入：["a", "b"]
    输出：0
    解释：D = {}
    示例 3：
    输入：["zyx", "wvu", "tsr"]
    输出：3
    解释：D = {0, 1, 2}
    :param A: List[str]
    :return: int
    """
    asc = [[ord(x) for x in a] for a in A]
    l = len(A)
    res = 0
    if l > 0:
        wl = len(A[0])
        for i in range(wl):
            for j in range(1, l):
                if asc[j][i] < asc[j-1][i]:
                    res += 1
                    break
    return res


def peakIndexInMountainArray(A):
    """
    852. 山脉数组的峰顶索引
    我们把符合下列属性的数组 A 称作山脉：
    A.length >= 3
    存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
    示例 1：
    输入：[0,1,0]
    输出：1
    示例 2：
    输入：[0,2,1,0]
    输出：1
    提示：
    3 <= A.length <= 10000
    0 <= A[i] <= 10^6
    A 是如上定义的山脉
    :param A:
    :return:
    """
    l, r = 0, len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[m-1] >= A[m]:
            r = m - 1
        else:
            if A[m] > A[m+1]:
                return m
            else:
                l = m + 1
    return l


def isPalindrome(s):
    """
    125. 验证回文串
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。
    输入: "A man, a plan, a canal: Panama"
    输出: true
    :param s: str
    :return: bool
    """
    import re
    s = re.sub("[^a-zA-Z0-9]", "", s).lower()
    return s == s[::-1]


def isPalindrome2(s):
    """
    125. 验证回文串
    不用正则
    :param s: str
    :return: bool
    """
    s = ''.join([chr(ord(x) - ord('a') + ord('A')) if 'a'<=x<='z' else x if 'A'<=x<='Z' or '0'<=x<='9' else '' for x in s])
    return s == s[::-1]


def generate(numRows):
    """
    118. 杨辉三角
    给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。
    示例:
    输入: 5
    输出:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    :param numRows: int
    :return: List[List[int]]
    """
    res = []
    for i in range(numRows):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = last[j] + last[j-1]
        last = res[-1]
        res.append(row)
    return res


def generate2(numRows):
    """
    118. 杨辉三角
    map, 错位补0相加
    :param numRows: int
    :return: List[List[int]]
    """
    if numRows == 0: return []
    res = [[1]]
    while numRows > 1:
        res.append(list(map(lambda l, r: l + r, [0] + res[-1], res[-1] + [0])))
        numRows -= 1
    return res


def isHappy(n):
    """
    202. 快乐数
    编写一个算法来判断一个数是不是“快乐数”。
    一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
    示例:
    输入: 19
    输出: true
    解释:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    :param n: int
    :return: bool
    """
    rs = {}
    while n != 1 and n not in rs:
        rs[n] = 1
        m = 0
        while n > 0:
            m += (n%10)**2
            n //= 10
        n = m
    return n == 1


def plusOne(digits):
    """
    66. 加一
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。
    输入: [1,2,3]
    输出: [1,2,4]
    解释: 输入数组表示数字 123。
    :param digits:
    :return:
    """
    # 一行
    # return [int(x) for x in str(int(''.join([str(e) for e in digits])) + 1)]

    i = len(digits)
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        digits.insert(0, 0)
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        digits[i] += 1
    return digits if digits[0] != 0 else digits[1:]


def containsDuplicate(nums):
    """
    217. 存在重复元素
    给定一个整数数组，判断是否存在重复元素。
    如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
    示例 1:
    输入: [1,2,3,1]
    输出: true
    示例 2:
    输入: [1,2,3,4]
    输出: false
    :param nums: List[int]
    :return: bool
    """
    return len(set(nums)) == nums


def removeElements(head, val):
    """
    203. 移除链表元素
    删除链表中等于给定值 val 的所有节点。
    示例:
    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5
    :param head: ListNode
    :param val: int
    :return: ListNode
    """
    if head:
        p = head
        while p:
            if p.next and p.next.val == val:
                if p.next.next:
                    p.next = p.next.next
                else:
                    p.next = None
                    break
            else:
                p = p.next
    if head and head.val == val:
        if head.next:
            head = head.next
        else:
            head = None
    return head


def countPrimes(n):
    """
    204. 计数质数
    统计所有小于非负整数 n 的质数的数量。
    示例:
    输入: 10
    输出: 4
    解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
    (暴力法和除质数法都超时，需要用厄拉多塞筛法)
    :param n: int
    :return: int
    """
    """
    超时
    if n < 3: return 0
    primes = [2]
    for i in range(3, n):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes.__len__()
    """
    if n < 3: return 0
    dp = [1] * n
    for i in range(2):
        dp[i] = 0
    for i in range(2, int(n**0.5) + 1):
        if dp[i] == 1:
            x = i*i
            while x < n:
                dp[x] = 0
                x += i
    # print(dp)
    return sum(dp)


def isIsomorphic(s, t):
    """
    205. 同构字符串
    给定两个字符串 s 和 t，判断它们是否是同构的。
    如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
    所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
    示例 1:
    输入: s = "egg", t = "add"
    输出: true
    示例 2:
    输入: s = "foo", t = "bar"
    输出: false
    示例 3:
    输入: s = "paper", t = "title"
    输出: true
    说明:
    你可以假设 s 和 t 具有相同的长度。
    思路1：(太慢，只能击败6%)
    同构说明同时遍历两个字符串，分别以相同规则统一赋值后的字符串是相等的，这里使用下标
    例如：
    abbc = "1224" = gffd
    cvbndjfker = "12345678910"
    思路2：
    在思路1基础上发现，只要对比当前部分，发现不一致就return False，进一步发现，只要对比当前字符的下表编号就可以。
    :param s: str
    :param t: str
    :return: bool
    """
    # 解一
    # l = len(s)
    # # x, y = "", ""
    # x, y = [0] * l, [0] * l
    # xd, yd = {}, {}
    # for i in range(l):
    #     if s[i] not in xd:
    #         xd[s[i]] = i
    #     if t[i] not in yd:
    #         yd[t[i]] = i
    #     if xd[s[i]] != yd[t[i]]: return False
    #     x[i] = xd[s[i]]
    #     y[i] = yd[t[i]]
    #     # x = "%s%d"%(x, xd[s[i]])
    #     # y = "%s%d"%(y, yd[t[i]])
    #     # if x != y: return False
    # return x == y

    # 解二
    l = len(s)
    xd, yd = {}, {}
    for i in range(l):
        if s[i] not in xd:
            xd[s[i]] = i
        if t[i] not in yd:
            yd[t[i]] = i
        if xd[s[i]] != yd[t[i]]: return False
    return True


def buddyStrings(A, B):
    """
    859. 亲密字符串
    给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
    示例 1：
    输入： A = "ab", B = "ba"
    输出： true
    示例 2：
    输入： A = "ab", B = "ab"
    输出： false
    示例 3:
    输入： A = "aa", B = "aa"
    输出： true
    示例 4：
    输入： A = "aaaaaaabc", B = "aaaaaaacb"
    输出： true
    示例 5：
    输入： A = "", B = "aa"
    输出： false
    提示：
    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A 和 B 仅由小写字母构成。
    :param A: str
    :param B: str
    :return: bool
    """
    la = len(A)
    lb = len(B)
    if la != lb or la < 2: return False
    sa = set(A).__len__()
    if sa != set(B).__len__(): return False
    if A == B and la == sa: return False
    da, db = {}, {}
    c = 0
    for i in range(la):
        if A[i] != B[i]:
            c += 1
            if A[i] not in da:
                da[A[i]] = 0
            da[A[i]] += 1
            if B[i] not in db:
                db[B[i]] = 0
            db[B[i]] += 1
    print(da, db)
    return da.__len__() == sum(da.values()) and sorted(da.keys()) == sorted(db.keys()) and c < 3


def mySqrt(x):
    """
    LC69
    x的平方根
    手写sqrt函数
    思路:
    牛顿迭代法求平方根下限整数
    https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
    :param x: int
    :return: int
    """
    if x <= 1:
        return x
    r = x
    while r > x / r:
        r = (r + x / r) // 2
    return int(r)


def removeElement(nums, val):
    """
    27. 移除元素
    给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    示例 1:
    给定 nums = [3,2,2,3], val = 3,
    函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
    你不需要考虑数组中超出新长度后面的元素。
    :param nums: List[int]
    :param val: int
    :return: int
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums.pop(i)
            j -= 1
        elif nums[j] == val:
            nums.pop()
            j -= 1
        else:
            i += 1
    return j + 1


def addBinary(a, b):
    """
    给定两个二进制字符串，返回他们的和（用二进制表示）。
    输入为非空字符串且只包含数字 1 和 0。
    示例 1:
    输入: a = "11", b = "1"
    输出: "100"
    示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"
    :param a: str
    :param b: str
    :return: str
    """
    i, j = len(a) - 1, len(b) - 1
    # a >= b
    if i < j:
        i, j = j, i
        a, b = b, a
    k, nx = 0, 0
    c = [x for x in a]
    z = ["0", "1"]
    while k <= j:
        p, q = i - k, j - k
        if a[p] == "1" and b[q] == "1":
            c[p] = z[nx]
            nx = 1
        elif a[p] == "0" and b[q] == "0":
            c[p] = z[nx]
            nx = 0
        else:
            c[p] = z[-1-nx]
        k += 1
    while k <= i:
        p = i - k
        if nx == 1:
            if a[p] == "1":
                c[p] = "0"
            else:
                c[p] = "1"
                nx = 0
        else:
            c[p] = a[p]
        k += 1
    res = "".join(c)
    return res if nx == 0 else "1" + res


def largestSumAfterKNegations(A, K):
    """
    1005. K 次取反后最大化的数组和
    给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
    以这种方式修改数组后，返回数组可能的最大和。
    示例 1：
    输入：A = [4,2,3], K = 1
    输出：5
    解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
    示例 2：
    输入：A = [3,-1,0,2], K = 3
    输出：6
    解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
    示例 3：
    输入：A = [2,-3,-1,5,-4], K = 2
    输出：13
    解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
    提示：
    1 <= A.length <= 10000
    1 <= K <= 10000
    -100 <= A[i] <= 100
    :param A: List[int]
    :param K: int
    :return: int
    """
    c = 0
    neg, pos = [], []
    for a in A:
        if a < 0:
            neg.append(a)
        elif a > 0:
            pos.append(a)
        else:
            c += 1
    neg.sort()
    pos.sort()
    ln = len(neg)
    res = 0
    if ln > 0:
        if K > ln:
            n = K - ln
            if c > 0:
                res += sum(pos)
                res -= sum(neg)
            else:
                if n % 2 == 0:
                    res += sum(pos)
                    res -= sum(neg)
                else:
                    res += sum(pos[1:])
                    res -= sum(neg[:-1])
                    res += max(-neg[-1], pos[0])
                    res += max(-pos[0], neg[-1])
        elif K == ln:
            res += sum(pos)
            res -= sum(neg)
        else:
            res += sum(pos)
            res += sum(neg[K:])
            res -= sum(neg[:K])
    else:
        res += sum(pos[1:])
        if K % 2 == 1:
            res -= pos[0]
        else:
            res += pos[0]
    return res


def letterCasePermutation(S):
    """
    784. 字母大小写全排列
    给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
    示例:
    输入: S = "a1b2"
    输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
    输入: S = "3z4"
    输出: ["3z4", "3Z4"]
    输入: S = "12345"
    输出: ["12345"]
    :param S: str
    :return: List[str]
    """
    res = [S]
    l = len(S)
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    for i in range(l):
        s = ord(S[i])
        if a <= s <= z:
            res.extend([r[:i] + chr(ord(r[i]) - a + A) + r[i+1:] for r in res])
        elif A <= s <= Z:
            res.extend([r[:i] + chr(ord(r[i]) + a - A) + r[i+1:] for r in res])
    return res


def hammingWeight(n):
    """
    191. 位1的个数
    编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
    示例 1：
    输入：00000000000000000000000000001011
    输出：3
    解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
    :param n: int
    :return: int
    """
    res = 0
    while n > 0:
        res = res + 1 if n & 1 else res
        n >>= 1
    return res


def reverseBits(n):
    """
    190. 颠倒二进制位
    颠倒给定的 32 位无符号整数的二进制位。
    示例 1：
    输入: 00000010100101000001111010011100
    输出: 00111001011110000010100101000000
    解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
          因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
    :param n: int
    :return: int
    """
    res = 0
    cmp = 1
    for i in range(32):
        if i > 0:
            res <<= 1
        if n & cmp:
            res += 1
        cmp <<= 1
    return res


def trailingZeroes(n):
    """
    172. 阶乘后的零
    给定一个整数 n，返回 n! 结果尾数中零的数量。
    示例 1:
    输入: 3
    输出: 0
    解释: 3! = 6, 尾数中没有零。
    示例 2:
    输入: 5
    输出: 1
    解释: 5! = 120, 尾数中有 1 个零.
    说明: 你算法的时间复杂度应为 O(log n) 。
    :param n: int
    :return: int
    """
    # c = ['0'] * 200
    # for q in range(200):
    #     i = 1
    #     l = 1
    #     while i <= q:
    #         l *= i
    #         i += 1
    #     x = str(l)
    #     c[q] = len(x) - len(x.rstrip("0"))
    #     if q > 0 and c[q] != c[q-1]:
    #         print(q, q//5, c[q])
    res = 0
    while n > 1:
        res += n // 5
        n //= 5
    return res


def readBinaryWatch(num):
    """
    401. 二进制手表
    二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
    每个 LED 代表一个 0 或 1，最低位在右侧。
    例如，上面的二进制手表读取 “3:25”。
    给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
    案例:
    输入: n = 1
    返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
    :param num: int
    :return: List[str]
    """
    pass


def minDepth(root):
    """
    111. 二叉树的最小深度
    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    给定二叉树 [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回它的最小深度  2.
    :param root: TreeNode
    :return: int
    """
    if not root:
        return 0
    l = minDepth(root.left)
    r = minDepth(root.right)
    return min(l, r) + 1 if l * r > 0 else l + r + 1


def convertBST(root):
    """
    538. 把二叉搜索树转换为累加树
    给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
    例如：
    输入: 二叉搜索树:
              5
            /   \
           2     13
    输出: 转换为累加树:
             18
            /   \
          20     13
    :param root: TreeNode
    :return: TreeNode
    """
    cur = [0]
    def inner(root):
        if not root:
            return
        inner(root.right)
        root.val += cur[-1]
        cur.append(root.val)
        inner(root.left)
    p = root
    inner(p)
    return root


def isAnagram(s, t):
    """
    242. 有效的字母异位词
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
    示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:
    输入: s = "rat", t = "car"
    输出: false
    说明:
    你可以假设字符串只包含小写字母。
    进阶:
    如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
    :param s: str
    :param t: str
    :return: bool
    """
    if len(s) != len(t): return False
    for x in set(s):
        s = s.replace(x, '')
        t = t.replace(x, '')
        if len(s) != len(t): return False
    return True


def bitwiseComplement(N):
    """
    1009. 十进制整数的反码
    每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。注意，除 N = 0 外，任何二进制表示中都不含前导零。
    二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。
    给定十进制数 N，返回其二进制表示的反码所对应的十进制整数。
    示例 1：
    输入：5
    输出：2
    解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。
    示例 2：
    输入：7
    输出：0
    解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。
    示例 3：
    输入：10
    输出：5
    解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。
    提示：
    0 <= N < 10^9
    :param N: int
    :return: int
    """
    i, j = 0, 31
    if N == 0: return 0
    while i < j:
        mid = (i + j) >> 1
        if N >= 2 ** mid:
            i = mid + 1
        if N < 2 ** mid:
            j = mid
    return N ^ ((2 ** j) - 1)


def findLHS(nums):
    """
    594. 最长和谐子序列
    和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
    现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
    示例 1:
    输入: [1,3,2,2,5,2,3,7]
    输出: 5
    原因: 最长的和谐数组是：[3,2,2,2,3].
    说明: 输入的数组长度最大不超过20,000.
    :param nums: List[int]
    :return: int
    """
    d = {}
    l = len(nums)
    m = 0
    for i in range(l):
        if nums[i] not in d:
            d[nums[i]] = 0
        d[nums[i]] += 1
    for n in nums:
        if n - 1 in d:
            m = max(m, d[n] + d[n - 1])
    return m


def getSum(a, b):
    """
    371. 两整数之和
    不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
    :param a: int
    :param b: int
    :return: int
    """
    upbound = 0xffffffff
    while b!=0:
        print(a, b)
        a, b = (a ^ b) & upbound, (a & b) << 1
    return a if a <= 0x7fffffff else ~(a ^ upbound)


def numberOfLines(widths, S):
    """
    806. 写字符串需要的行数
    我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。
    现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
    示例 1:
    输入:
    widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrstuvwxyz"
    输出: [3, 60]
    解释:
    所有的字符拥有相同的占用单位10。所以书写所有的26个字母，
    我们需要2个整行和占用60个单位的一行。
    注：
    字符串 S 的长度在 [1, 1000] 的范围。
    S 只包含小写字母。
    widths 是长度为 26的数组。
    widths[i] 值的范围在 [2, 10]。
    :param widths: List[int]
    :param S: str
    :return: List[int]
    """
    a = ord('a')
    r, x = 0, 0
    for xs in S:
        s = ord(xs)
        if x + widths[s - a] > 100:
            x = widths[s - a]
            r += 1
        else:
            x += widths[s - a]
    return [r, x]


def longestWord(words):
    """
    720. 词典中最长的单词
    给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
    若无答案，则返回空字符串。
    示例 1:
    输入:
    words = ["w","wo","wor","worl", "world"]
    输出: "world"
    解释:
    单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
    :param words: List[str]
    :return: str
    """
    d = {}
    l = len(words)
    words.sort()
    for i in range(l):
        if len(words[i]) == 1:
            Trie(words[i])



def fizzBuzz(n):
    """
    412. Fizz Buzz
    写一个程序，输出从 1 到 n 数字的字符串表示。
    1. 如果 n 是3的倍数，输出“Fizz”；
    2. 如果 n 是5的倍数，输出“Buzz”；
    3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
    示例：
    n = 15,
    返回:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    :param n: int
    :return: List[str]
    """
    return ["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1, n + 1)]


def numSpecialEquivGroups(A):
    """
    893. 特殊等价字符串组
    一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，并且交换 S[j] 和 S [i]。
    现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。
    返回 A 中特殊等价字符串组的数量。
    示例 1：
    输入：["a","b","c","a","c","c"]
    输出：3
    解释：3 组 ["a","a"]，["b"]，["c","c","c"]
    示例 2：
    输入：["aa","bb","ab","ba"]
    输出：4
    解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]
    示例 3：
    输入：["abc","acb","bac","bca","cab","cba"]
    输出：3
    解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
    示例 4：
    输入：["abcd","cdab","adcb","cbad"]
    输出：1
    解释：1 组 ["abcd","cdab","adcb","cbad"]
    提示：
    1 <= A.length <= 1000
    1 <= A[i].length <= 20
    所有 A[i] 都具有相同的长度。
    所有 A[i] 都只由小写字母组成。
    :param A: List[str]
    :return: int
    """
    def strsort(x):
        return ''.join(sorted([a for a in x]))
    d = {}
    r = 0
    for a in A:
        x = a[::2]
        y = a[1::2]
        k = strsort(x) + strsort(y)
        print(k)
        if k not in d:
            d[k] = 1
            r += 1
    return r


if __name__ == '__main__':
    pass
    # print(longestWord(["a","banana","app","appl","ap","apply","apple"]))
    print(numSpecialEquivGroups(["abcd","cdab","adcb","cbad"]))
    # print(getSum(-2,1))
    # print(findLHS([1,2,2,1]))
    # print(bitwiseComplement(5))
    # print(hammingWeight(0b00000000000000000000000000001011))
    # print(reverseBits(0b00000010100101000001111010011100))
    # print(trailingZeroes(50))
    # words = ["gin", "zen", "gig", "msg"]
    # print(uniqueMorseRepresentations(words))
    # x = [-4, -1, 0, 3, 10]
    # print(sortedSquares(x))
    # print(diStringMatch("IDID"))
    # print(removeOuterParentheses("(()())(())(()(()))"))
    # print(findComplement(13))
    # print(selfDividingNumbers(1,22))
    # print(repeatedNTimes([9,5,3,3]))
    # print(peakIndexInMountainArray([0,2,3,4,3]))
    # a = Node(1, [Node(3, [Node(5, []), Node(6, [])]),Node(2, []),Node(4, [])])
    # postorder2(a)
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    # print(generate(5))
    # print(isHappy(2))
    # print(plusOne([9,9,9]))
    # x = ListNode(0)
    # p = x
    # for i in [1,1,1]:
    #     p.next = ListNode(i)
    #     p = p.next
    # removeElements(x.next, 1)
    # print(countPrimes(10))
    # print(isIsomorphic("papxr", "title"))
    # print(buddyStrings("ab", "ab"))
    # print(removeElement([1,3,4,5,2,1,2,3,2,3], 2))
    # print(addBinary("101111", "10"))
    # print(largestSumAfterKNegations([8,-7,-3,-9,1,9,-6,-9,3], 8))
    # print(letterCasePermutation("a1b2"))