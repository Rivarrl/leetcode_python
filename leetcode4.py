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
    opr = []
    cur = 0
    for x in input:
        if x.isdigit():
            cur = cur * 10 + int(x)
        else:
            opr.append(cur)
            cur = 0
            opr.append(x)
    opr.append(cur)
    print(opr)
    def helper(opr):
        res = []
        if opr:
            n = len(opr)
            if n == 1:
                return res.append(n)
            else:
                for i in range(0, n-2, 2):
                    l = opr[i]
                    o = opr[i+1]
                    r = opr[i+2]
                    if o == "+":
                        s = l + r
                    elif o == "-":
                        s = l - r
                    else:
                        s = l * r
                    print(opr[:i] + opr[i + 4:])
                    for each in helper(opr[:i] + opr[i+3:]):
                        res.append(s + each)
        return res
    res = helper(opr)
    print(res)
    return res


if __name__ == '__main__':
    diffWaysToCompute("2-1-1")
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
