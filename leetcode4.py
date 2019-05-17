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



if __name__ == '__main__':
    findSubstring("barfoothefoobarman",["foo","bar"])
    # x = construct_list_node([1,2,3,4,5,6,7,8,9])
    # r = reverseKGroup(x,3)
    # print_list_node(r)
    # print(jump([2, 3, 1, 1, 4]))
    # searchRange([1,1,2], 1)
    pass
