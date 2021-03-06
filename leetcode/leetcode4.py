from algorithm_utils import *

# leetcode 4

def jump(nums):
    """
    45. 跳跃游戏 II
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    说明:
    假设你总是可以到达数组的最后一个位置。
    :param nums: List[int]
    :return: int
    """
    """
    # 超时
    l = len(nums)
    if l < 2: return 0
    dp = [l for _ in range(l)]
    dp[0] = 0
    dp[1] = 1
    for i in range(l):
        for j in range(i):
            if i - j <= nums[j]:
                dp[i] = min(dp[i], dp[j] + 1)
    # print(dp)
    return dp[-1]
    """
    l = len(nums)
    if l < 2: return 0
    ans, i, r, n = 0, 0, 0, nums[0]
    for i in range(l):
        n = max(i + nums[i], n)
        if n >= l - 1: return ans + 1
        if i == r:
            ans += 1
            r = n
    return ans


def searchRange(nums, target):
    """
    34. 在排序数组中查找元素的第一个和最后一个位置
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    l = len(nums)
    if l == 0: return [-1, -1]
    i, j = 0, l - 1
    while i < j:
        m = (i + j) >> 1
        if nums[m] > target:
            j = m - 1
        elif nums[m] < target:
            i = m + 1
        else:
            i = j = m
    # print(i, j)
    if nums[i] != target and nums[j] != target:
        return [-1, -1]
    pi, pj = False, False
    while i >= 0 and nums[i] == target:
        i -= 1
        pi = True
    while j < l and nums[j] == target:
        j += 1
        pj = True
    i = i + 1 if pi else i
    j = j - 1 if pj else j
    # print(i, j)
    return [i, j]


def reverseKGroup(head, k):
    """
    25. k个一组翻转链表
    给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
    示例 :
    给定这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5
    说明 :
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    :param head: ListNode
    :param k: int
    :return: ListNode
    """
    """
    # 头插法
    if not head or not head.next: return head
    p, l = head, 0
    while p:
        p = p.next
        l += 1
    def helper(head, l):
        if l < k:
            return head
        p, r = head, head
        for i in range(k-1):
            q = p.next
            p.next = None if not p.next.next else p.next.next
            q.next = r
            r = q
        if l > k:
            p.next = helper(p.next, l - k)
        return r
    return helper(head, l)
    """
    # 尾插法
    if k <= 1: return head
    dummy = ListNode(0)
    curr, last = dummy, None
    count = 0
    p = head
    # k组翻转
    while p:
        if count == k:
            count = 0
            curr = last
        tmp = curr.next
        curr.next = p
        p = p.next
        curr.next.next = tmp
        if count == 0:
            last = curr.next
        count += 1
    # 把小于k长的尾部翻回来
    if count < k:
        p, q = ListNode(0), curr.next
        while q:
            r = p.next
            p.next = q
            p.next.next = r
        curr.next = p.next
    return dummy.next


def findSubstring(s, words):
    """
    30. 串联所有单词的子串 (超时)
    给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
    注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
    示例 1：
    输入：
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    输出：[0,9]
    解释：
    从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
    输出的顺序不重要, [9,0] 也是有效答案。
    示例 2：
    输入：
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    输出：[]
    :param s: str
    :param words: List[str]
    :return: List[int]
    """
    """
    # 回溯拼接words所有可能，暴力找，超时
    l = words.__len__()
    if l == 0 or s.__len__() == "": return []
    def helper(words):
        res = []
        if words == []: res.append('')
        for i, word in enumerate(words):
            for x in helper(words[:i] + words[i+1:]):
                if not word + x in res:
                    res.append(word + x)
        return res
    res = []
    for posibility in helper(words):
        idx = s.find(posibility)
        while idx >= 0:
            res.append(idx)
            idx = s.find(posibility, idx + 1)
    return res
    """
    """
    # 哈希表 + 滑动窗口寻找模式串组合 59%
    l = words.__len__()
    ls = s.__len__()
    if l == 0 or ls == 0: return []
    lw = words[0].__len__()
    lws = l * lw
    dw = {}
    for word in words:
        if not word in dw:
            dw[word] = 0
        dw[word] += 1
    res = []
    for i in range(ls - lws + 1):
        tmp = {k: v for k, v in dw.items()}
        flag = True
        for j in range(i, i+lws, lw):
            print(s[j:j+lw])
            if not s[j:j+lw] in tmp or tmp[s[j:j+lw]] == 0:
                flag = False
                break
            tmp[s[j:j+lw]] -= 1
        if flag:
            res.append(i)
    print(res)
    return res
    """
    # 滑动窗口 + 哈希表 + 双指针 100%
    if not s or not words:
        return []
    lens, len_word, len_subs, times = len(s), len(words[0]), 0, {}
    times = {}
    for word in words:
        len_subs += len_word
        times[word] = times.get(word) + 1 if times.get(word) else 1
    res = []
    for i in range(len_word):
        start = i
        cur = {}
        while i + len_subs <= lens:
            word = s[start:start + len_word]
            start += len_word
            if word not in times:
                i = start
                cur.clear()
            else:
                if word in cur:
                    cur[word] += 1
                else:
                    cur[word] = 1
                while cur[word] > times[word]:
                    cur[s[i:i + len_word]] -= 1
                    i += len_word
                if start - i == len_subs:
                    res.append(i)
    return res


def fullJustify(words, maxWidth):
    """
    68. 文本左右对齐
    给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
    你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
    要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
    文本的最后一行应为左对齐，且单词之间不插入额外的空格。
    说明:
    单词是指由非空格字符组成的字符序列。
    每个单词的长度大于 0，小于等于 maxWidth。
    输入单词数组 words 至少包含一个单词。
    示例:
    输入:
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    输出:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    示例 2:
    输入:
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    输出:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
         因为最后一行应为左对齐，而不是左右两端对齐。
         第二行同样为左对齐，这是因为这行只包含一个单词。
    示例 3:
    输入:
    words = ["Science","is","what","we","understand","well","enough","to","explain",
             "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    输出:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]
    :param words: List[str]
    :param maxWidth: int
    :return: List[str]
    """
    l = len(words)
    cur = 0
    res = []
    i, j = 0, -1
    while i < l:
        t = cur + len(words[i])
        j += 1
        if t + i - j <= maxWidth:
            cur = t
            i += 1
            j -= 1
        else:
            max_blanks = maxWidth - cur
            s = i - j - 1
            this_row = ""
            if s > 0:
                e = max_blanks // s
                y = max_blanks % s
                for k in range(j, i):
                    p = k - j
                    if p < y:
                        this_row += words[k] + " " * (e+1)
                    else:
                        if k < i - 1:
                            this_row += words[k] + " " * e
                        else:
                            this_row += words[k]
            else:
                this_row = words[j] + " " * max_blanks
            res.append(this_row)
            cur = 0
            j = i - 1
    last_row = " ".join(words[j + 1:])
    last_row += " " * (maxWidth - len(last_row))
    res.append(last_row)
    print(res)
    return res


def calculate(s):
    """
    224. 基本计算器
    实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
    示例 1:
    输入: "1 + 1"
    输出: 2
    示例 2:
    输入: " 2-1 + 2 "
    输出: 3
    示例 3:
    输入: "(1+(4+5+2)-3)+(6+8)"
    输出: 23
    说明：
    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。
    :param s: str
    :return: int
    """
    """
    # 慢，20%
    s = s.replace(" ", "")
    n = len(s)
    num_range = range(ord("0"), ord("0") + 10)
    opa, opr = [], []
    cur = 0
    for i in range(n):
        if ord(s[i]) in num_range:
            cur *= 10
            cur += int(s[i])
            if i == n - 1 or ord(s[i+1]) not in num_range:
                opa.append(cur)
        else:
            cur = 0
            if s[i] == ")":
                print(opa, opr)
                o = opr.pop()
                tmp, tmpr = [opa.pop()], []
                while opa and opr and o != "(":
                    tmp.append(opa.pop())
                    tmpr.append(o)
                    o = opr.pop()
                l = tmp.pop()
                while tmp and tmpr:
                    if tmpr.pop() == "+":
                        l += tmp.pop()
                    else:
                        l -= tmp.pop()
                opa.append(l)
            else:
                opr.append(s[i])
    print(opa, opr)
    l = opa[0]
    for i in range(len(opr)):
        r = opa[i+1]
        o = opr[i]
        if o == "+":
            l += r
        if o == "-":
            l -= r
    print(l)
    return l
    """
    # 99%
    stack = []
    res = 0
    num = 0
    sign = 1
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif c in '+-':
            res += sign * num
            num = 0
            sign = 1 if c == '+' else -1
        elif c == ')':
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + sign * num


def calculate2(s):
    """
    227. 基本计算器 II
    实现一个基本的计算器来计算一个简单的字符串表达式的值。
    字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
    示例 1:
    输入: "3+2*2"
    输出: 7
    示例 2:
    输入: " 3/2 "
    输出: 1
    示例 3:
    输入: " 3+5 / 2 "
    输出: 5
    说明：
    你可以假设所给定的表达式都是有效的。
    请不要使用内置的库函数 eval。
    :param s: str
    :return: int
    """
    """
        # 28%
    s = s.replace(" ", "")
    n = len(s)
    opr, opa = [], []
    cur = 0
    sign = 1
    for i in range(n):
        if s[i].isdigit():
            cur *= 10
            cur += int(s[i]) * sign
            if i == n - 1 or not s[i+1].isdigit():
                if opr and opr[-1] in "*/":
                    if opr[-1] == "*":
                        opa[-1] *= cur
                    if opr[-1] == "/":
                        if opa[-1] // cur < 0:
                            opa[-1] = -(abs(opa[-1]) // abs(cur))
                        else:
                            opa[-1] = opa[-1] // cur
                else:
                    opa.append(cur)
        else:
            if s[i] == "-":
                sign = -1
                opr.append("+")
            else:
                sign = 1
                opr.append(s[i])
            cur = 0
    r = opa.pop()
    while opa:
        r += opa.pop()
    print(r)
    return r
    """
    # 100% 用sign保存上一个符号，stk中迭代更新加和值，最终stk中存的是先经过乘除运算后的一轮结果
    s += '+'
    n = 0
    sign = '+'
    stk = []
    for c in s:
        if c.isdigit():
            n = 10 * n + ord(c) - 48
        elif c != ' ':
            if sign == '+':
                stk.append(n)
            elif sign == '-':
                stk.append(-n)
            elif sign == '*':
                stk.append(stk.pop() * n)
            elif sign == '/':
                stk.append(int(stk.pop() / n))
            sign = c
            n = 0
    print(stk)
    return sum(stk)


def brokenCalc(X, Y):
    """
    991. 坏了的计算器
    在显示着数字的坏计算器上，我们可以执行以下两种操作：
    双倍（Double）：将显示屏上的数字乘 2；
    递减（Decrement）：将显示屏上的数字减 1 。
    最初，计算器显示数字 X。
    返回显示数字 Y 所需的最小操作数。
    示例 1：
    输入：X = 2, Y = 3
    输出：2
    解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
    示例 2：
    输入：X = 5, Y = 8
    输出：2
    解释：先递减，再双倍 {5 -> 4 -> 8}.
    示例 3：
    输入：X = 3, Y = 10
    输出：3
    解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.
    示例 4：
    输入：X = 1024, Y = 1
    输出：1023
    解释：执行递减运算 1023 次
    提示：
    1 <= X <= 10^9
    1 <= Y <= 10^9
    :param X: int
    :param Y: int
    :return: int
    """
    ans = 0
    while X < Y:
        if Y % 2 == 0:
            Y //= 2
            ans += 1
        else:
            Y = (Y + 1) // 2
            ans += 2
    print(ans + X - Y)
    return ans + X - Y


def diffWaysToCompute(input):
    """
    241. 为运算表达式设计优先级
    给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
    示例 1:
    输入: "2-1-1"
    输出: [0, 2]
    解释:
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    示例 2:
    输入: "2*3-4*5"
    输出: [-34, -14, -10, -10, 10]
    解释:
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    :param input: str
    :return: List[int]
    """
    res = []
    for i, x in enumerate(input):
        if not x.isdigit():
            lres, rres = diffWaysToCompute(input[:i]), diffWaysToCompute(input[i+1:])
            for l in lres:
                for r in rres:
                    if x == "+":
                        res.append(l + r)
                    elif x == "-":
                        res.append(l - r)
                    elif x == "*":
                        res.append(l * r)
    if res == []:
        res.append(int(input))
    return res


def restoreIpAddresses(s):
    """
    93. 复原IP地址
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
    示例:
    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]
    :param s: str
    :return: List[str]
    """
    def helper(s, dot):
        res = []
        n = len(s)
        if n == 0 and dot > 0: return []
        if dot == 0:
            if n == 0 or n > 3 or (2 <= n <= 3 and s[0] == '0') or int(s) > 255:
                return []
            if int(s) <= 255:
                res.append(s)
        else:
            for i in range(3):
                for x in helper(s[i+1:], dot - 1):
                    if int(s[:i+1]) <= 255 and len(x) > 0:
                        res += [s[:i+1] + '.' + x]
                if s[0] == '0':
                    break
        return res
    res = helper(s, 3)
    print(res)
    return res


def combine(n, k):
    """
    77. 组合
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
    示例:
    输入: n = 4, k = 2
    输出:
    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    :param n: int
    :param k: int
    :return: List[List[int]]
    """
    res = []
    if k == 1:
        for x in range(n):
            res.append([x+1])
    else:
        for i in range(n, 1, -1):
            for x in combine(i-1, k-1):
                res += [x + [i]]
    return res


def combinationSum3(k, n):
    """
    216. 组合总和 III
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
    说明：
    所有数字都是正整数。
    解集不能包含重复的组合。
    示例 1:
    输入: k = 3, n = 7
    输出: [[1,2,4]]
    示例 2:
    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]
    :param k: int
    :param n: int
    :return: List[List[int]]
    """
    if k > 9 or k < 1: return []
    if n > 45 or n < 1: return []
    def helper(j, n, k):
        if n < k: return []
        res = []
        if k == 1 and 0 < n < 10:
            res.append([n])
        for i in range(j, min(10, n+1)):
            for x in helper(i + 1, n - i, k - 1):
                sx = sorted([i] + x)
                if not i in x and not sx in res:
                    res.append(sx)
        return res
    res = helper(1, n, k)
    return res


def countArrangement(N):
    """
    526. 优美的排列
    假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
    第 i 位的数字能被 i 整除
    i 能被第 i 位上的数字整除
    现在给定一个整数 N，请问可以构造多少个优美的排列？
    示例1:
    输入: 2
    输出: 2
    解释:
    第 1 个优美的排列是 [1, 2]:
      第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
      第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
    第 2 个优美的排列是 [2, 1]:
      第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
      第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
    说明:
    N 是一个正整数，并且不会超过15。
    :param N: int
    :return: int
    """
    def dfs(visited, N, idx):
        if idx > N:
            ans[0] += 1
            return
        for i in range(1, N+1):
            if not visited[i] and (i % idx == 0 or idx % i == 0):
                visited[i] = True
                dfs(visited, N, idx + 1)
                visited[i] = False
    visited = [False] * (N + 1)
    ans = [0]
    dfs(visited, N, 1)
    print(ans[0])
    return ans[0]


def canJump(nums):
    """
    55. 跳跃游戏
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。
    示例 1:
    输入: [2,3,1,1,4]
    输出: true
    解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
    示例 2:
    输入: [3,2,1,0,4]
    输出: false
    解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
    :param nums: List[int]
    :return: bool
    """
    """
    # 方法一: 倒着走
    n = len(nums)
    if n <= 1: return 0
    i, r = n - 2, n - 1
    while i >= 0:
        if nums[i] >= r - i:
            r = i
        i -= 1
    return r == 0
    """
    # 方法二: 记录当前还可以走的最大步数
    n = len(nums)
    step = 0
    for i in range(n - 1):
        step = max(nums[i], step)
        if step == 0: return False
        step -= 1
    return True


def sortColors(nums):
    """
    75. 颜色分类
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    注意:
    不能使用代码库中的排序函数来解决这道题。
    示例:
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]
    进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？
    :param nums: List[int]
    :return: None
    """
    """
    # 把0放左边2放右边
    i, j = 0, len(nums) - 1
    while i < j:
        while i<j and nums[i] != 2:
            i += 1
        while i<j and nums[j] == 2:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    i, j = 0, len(nums) - 1
    while i < j:
        while i<j and nums[j] != 0:
            j -= 1
        while i<j and nums[i] == 0:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    print(nums)
    """
    # 简化版，三路快排
    i, j, k = 0, len(nums) - 1, 0
    while i <= j:
        if nums[i] < 1:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k += 1
        elif nums[i] > 1:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    print(nums)
    

def totalNQueens(n):
    """
    52. N皇后 II
    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回 n 皇后不同的解决方案的数量。
    示例:
    输入: 4
    输出: 2
    解释: 4 皇后问题存在如下两个不同的解法。
    [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    思路: 每行有且仅有一个Q，所以可以使用一维数组，下标代表行号，数值代表列号，那么判断第k行的Q在第几列时，不符合条件即为a[i] == a[k] (列) 或者 abs(a[i] - a[k]) = k - i (斜线)
    :param n: int
    :return: int
    """
    # 迭代
    def check(a, k):
        for i in range(1, k):
            if abs(a[i] - a[k]) == k - i or a[i] == a[k]:
                return False
        return True

    ctr = 0
    a = [0] * (n + 1)
    k = 1
    while k > 0:
        a[k] += 1
        # 第k行的摆放
        while a[k] <= n and not check(a, k):
            a[k] += 1
        # 可以摆放
        if a[k] <= n:
            # 是最后一行，说明是一种情况
            if k == n:
                ctr += 1
            else:
                # 继续搜索下一行
                k += 1
                # 从1开始搜索
                a[k] = 0
        # 不可摆放，回溯到上一行，继续进行下一列的迭代
        else:
            k -= 1
    return ctr


def solveNQueens(n):
    """
    51. N皇后
    n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
    给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
    每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    示例:
    输入: 4
    输出: [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],
     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    解释: 4 皇后问题存在两个不同的解法。
    思路: 每行有且仅有一个Q，所以可以使用一维数组
    :param n: int
    :return: List[List[str]]
    """
    # 递归
    def construct(a):
        queens = []
        for x in a:
            tmp = ""
            for i in range(1, n+1):
                if i == x:
                    tmp += "Q"
                else:
                    tmp += "."
            queens.append(tmp)
        return queens

    def check(a, k):
        for i in range(1, k):
            if abs(a[i] - a[k]) == k - i or a[i] == a[k]:
                return False
        return True

    def solve(r):
        if r > n:
            res.append(construct(a[1:]))
        else:
            for i in range(1, n+1):
                a[r] = i
                if check(a, r):
                    solve(r+1)

    a = [0] * (n + 1)
    res = []
    solve(1)
    for each in res:
        for x in each:
            print(x)
        print()
    return res


def merge(intervals):
    """
    56. 合并区间
    给出一个区间的集合，请合并所有重叠的区间。
    示例 1:
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    示例 2:
    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    :param intervals: List[List[int]]
    :return: List[List[int]]
    """
    n = len(intervals)
    if n <= 1: return intervals
    intervals.sort(key=lambda x:x[0])
    res = []
    stk = [intervals[0][0]]
    last = intervals[0][1]
    for i in range(1, n):
        l, r = intervals[i][0], intervals[i][1]
        if l <= last:
            last = max(r, last)
        else:
            stk.append(last)
            res.append(stk)
            stk = [l]
            last = r
    stk.append(last)
    res.append(stk)
    return res


def canFinish(numCourses, prerequisites):
    """
    207. 课程表
    现在你总共有 n 门课需要选，记为 0 到 n-1。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
    给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
    示例 1:
    输入: 2, [[1,0]]
    输出: true
    解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
    示例 2:
    输入: 2, [[1,0],[0,1]]
    输出: false
    解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
    说明:
    输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
    你可以假定输入的先决条件中没有重复的边。
    提示:
    这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
    通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
    拓扑排序也可以通过 BFS 完成。
    a[0]: 入度, a[1]: 出度
    :param numCourses: int
    :param prerequisites: List[List[int]]
    :return: bool
    """
    """
    # 拓扑排序，用邻接表代替遍历整个数组
    d_in = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for tail, head in prerequisites:
        d_in[tail] += 1
        adj[head].append(tail)
    stk = []
    for i in range(numCourses):
        if d_in[i] == 0:
            stk.append(i)
    ctr = 0
    while stk:
        i = stk.pop()
        ctr += 1
        d_in[i] -= 1
        for j in adj[i]:
            d_in[j] -= 1
            if d_in[j] == 0:
                stk.append(j)
    return ctr == numCourses
    """
    # 深度优先搜索，visited记录节点访问状态，0是未访问，1是正在被本次dfs中访问，2是已访问
    def is_cycle(cur):
        if visited[cur] == 1:
            return True
        if visited[cur] == 2:
            return False
        visited[cur] = 1
        for sub in adj[cur]:
            if is_cycle(sub):
                return True
        visited[cur] = 2
        return False

    if len(prerequisites) <= 1: return True
    d_in = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    for tail, head in prerequisites:
        d_in[tail] += 1
        adj[head].append(tail)
    for i in range(numCourses):
        if is_cycle(i): return False
    return True


def getPermutation(n, k):
    """
    60. 第k个排列
    给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    给定 n 和 k，返回第 k 个排列。
    说明：
    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。
    示例 1:
    输入: n = 3, k = 3
    输出: "213"
    示例 2:
    输入: n = 4, k = 9
    输出: "2314"
    :param n: int
    :param k: int
    :return: str
    """
    """
    # 回溯 官方标签误导人，血妈超时
    def helper(cur, flag):
        if len(res) == k:
            return False
        if len(cur) == n:
            res.append(cur)
        for i in range(n):
            if not flag[i]:
                flag[i] = True
                if not helper(cur + str(i+1), flag):
                    break
                flag[i] = False
        return True
    res = []
    flag = [False] * n
    helper("", flag)
    return res[-1]
    """
    # 找规律
    a = [str(x + 1) for x in range(n)]
    t = [1] * (n + 1)
    for i in range(1, n + 1):
        t[i] = t[i - 1] * i
    res = ""
    for i in range(n - 1, -1, -1):
        p = (k - 1) // t[i]
        x = a.pop(p)
        res += x
        k %= t[i]
    return res


def subsetsWithDup(nums):
    """
    90. 子集 II
    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    示例:
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
    :param nums: List[int]
    :return: List[List[int]]
    """
    """
    # 回溯 慢
    nums.sort()
    n = len(nums)
    res = [[]]
    for i in range(n):
        for x in subsetsWithDup(nums[i+1:]):
            if not [nums[i]] in res:
                res.append([nums[i]])
            sx = [nums[i]] + x
            if not sx in res:
                res.append(sx)
    return res
    """
    # dfs
    nums.sort()
    res, n = list(), len(nums)
    def subsets_dfs(lst, pos):
        num = None
        res.append(lst[:])
        for i in range(pos, n):
            if nums[i] != num:
                lst.append(nums[i])
                subsets_dfs(lst, i + 1)
                num = lst.pop()
    subsets_dfs([], 0)
    return res


if __name__ == '__main__':
    # getPermutation(4, 9)
    print(subsetsWithDup([2, 1, 2]))
    # print(canFinish(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))
    # merge([[1,3],[2,6],[15,18],[8,10]])
    # solveNQueens(4)
    # sortColors([1,2,0])
    # canJump([0])
    # countArrangement(5)
    # print(combinationSum3(2, 10))
    # print(combine(4, 2))
    # restoreIpAddresses("010010")
    # print(diffWaysToCompute("2*3-4*5"))
    # brokenCalc(3,10)
    # print(eval("14-3//2+2-3*2+15//4"))
    # calculate2("14-3/2+2-3*2+15/4")
    # calculate("1-(3+5-2+(3+19-(3-1-4+(9-4-(4-(1+(3)-2)-5)+8-(3-5)-1)-4)-5)-4+3-9)-4-(3+2-5)-10")
    # fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    # findSubstring("barfoothefoobarman",["foo","bar"])
    # x = construct_list_node([1,2,3,4,5,6,7,8,9])
    # r = reverseKGroup(x,3)
    # print_list_node(r)
    # print(jump([2, 3, 1, 1, 4]))
    # searchRange([1,1,2], 1)
    pass
