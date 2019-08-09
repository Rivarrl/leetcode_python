# -*- coding:utf-8 -*-
from algorithm_utils import *
# leetcode 中等题

def reverseBetween(head, m, n):
    """
    92. 反转链表 II
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    说明:
    1 ≤ m ≤ n ≤ 链表长度。
    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
    :param head: ListNode
    :param m: int
    :param n: int
    :return: ListNode
    """
    """
    # 78% 定位两个临界点后再降反转部分反转 O(len(head)+n)
    i = 0
    p = ListNode(0)
    p.next, q = head, p
    while i + 1 < m:
        p = p.next
        i += 1
    p1, p2 = p, p.next
    j = i + 1
    while i <= n:
        p = p.next
        i += 1
    p3 = p
    p = p2
    t = None
    i = j
    while i <= n:
        r = p.next
        p.next = t
        t = p
        if r == None or i == n:
            break
        p = r
        i += 1
    p2.next = p3
    p1.next = p
    return q.next
    """
    # O(n)
    p = ListNode(0)
    p.next = head
    pre = p
    for i in range(1, m):
        pre = pre.next
    head = pre.next
    for j in range(m, n):
        q = head.next
        head.next = q.next
        q.next = pre.next
        pre.next = q
    return p.next


def minSteps(n):
    """
    650. 只有两个键的键盘
    最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
    Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
    Paste (粘贴) : 你可以粘贴你上一次复制的字符。
    给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
    示例 1:
    输入: 3
    输出: 3
    解释:
    最初, 我们只有一个字符 'A'。
    第 1 步, 我们使用 Copy All 操作。
    第 2 步, 我们使用 Paste 操作来获得 'AA'。
    第 3 步, 我们使用 Paste 操作来获得 'AAA'。
    说明:
    n 的取值范围是 [1, 1000] 。
    :param n: int
    :return: int
    """
    if n == 1: return 0
    ans = 0
    i = 2
    while n > 1:
        while n % i == 0:
            ans += i
            n /= i
        i += 1
    return ans


def nthSuperUglyNumber(n, primes):
    """
    313. 超级丑数
    编写一段程序来查找第 n 个超级丑数。
    超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
    示例:
    输入: n = 12, primes = [2,7,13,19]
    输出: 32
    解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
    说明:
    1 是任何给定 primes 的超级丑数。
     给定 primes 中的数字以升序排列。
    0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
    第 n 个超级丑数确保在 32 位有符整数范围内。
    :param n: int
    :param primes: List[int]
    :return: int
    """
    """
    # 多指针法 40%
    m = len(primes)
    rec = [0] * m
    res = [1]
    for i in range(n-1):
        res.append(min(primes[j] * res[rec[j]] for j in range(m)))
        for j in range(m):
            if primes[j] * res[rec[j]] == res[-1]:
                rec[j] += 1
    print(res)
    return res[-1]
    """
    # 优先队列 100%
    import heapq
    heap, res, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
    res[0] = 1
    for index, val in enumerate(primes):
        heapq.heappush(heap, (val, index))
    for i in range(1, n):
        res[i], k = heapq.heappop(heap)
        ugly_by_last_prime[i] = k
        idx[k] += 1
        while ugly_by_last_prime[idx[k]] > k:
            idx[k] += 1
        heapq.heappush(heap, (primes[k] * res[idx[k]], k))
    return res[-1]


def pathSum(root, sum):
    """
    113. 路径总和 II
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    给定如下二叉树，以及目标和 sum = 22，
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    返回:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
    :param root: TreeNode
    :param sum: int
    :return: List[List[int]]
    """
    def dfs(node, cur, path):
        if not node: return
        if not node.left and not node.right:
            if cur == node.val:
                nonlocal res
                res.append(path + [node.val])
                return
        if node.left:
            dfs(node.left, cur - node.val, path + [node.val])
        if node.right:
            dfs(node.right, cur - node.val, path + [node.val])

    res = []
    dfs(root, sum, [])
    return res


def sortedListToBST(head):
    """
    109. 有序链表转换二叉搜索树
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
    给定的有序链表： [-10, -3, 0, 5, 9],
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5
    :param head: ListNode
    :return: TreeNode
    """
    # 由于链表查找中点的复杂度比数组高, 可以转成数组再操作
    # 快慢指针找中点
    def helper(node):
        if not node: return None
        if not node.next: return TreeNode(node.val)
        last, slow, fast = node, node.next, node.next.next
        while fast and fast.next:
            last, slow, fast = last.next, slow.next, fast.next.next
        last.next = None
        root = TreeNode(slow.val)
        root.left = helper(node)
        root.right = helper(slow.next)
        return root

    return helper(head)


def maxProduct(words):
    """
    318. 最大单词长度乘积
    给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
    示例 1:
    输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
    输出: 16
    解释: 这两个单词为 "abcw", "xtfn"。
    示例 2:
    输入: ["a","ab","abc","d","cd","bcd","abcd"]
    输出: 4
    解释: 这两个单词为 "ab", "cd"。
    示例 3:
    输入: ["a","aa","aaa","aaaa"]
    输出: 0
    解释: 不存在这样的两个单词。
    :param words: List[str]
    :return: int
    """
    """
    # 隐含线索：判断两个字符串是否出现共同字母时，每个字符串中字母出现的个数对解题无关紧要，ab = abb，即只需记录字符串中的某字母出现与否
    # 状态值只有两个，而且字符串中只有26个小写字母
    # 所以可以使用26位的二进制数来记录每个字符串的状态值
    # 最终两个字符串与运算后为0则说明不包含共同字母
    n = len(words)
    d = []
    for i in range(n):
        a = 0
        for c, j in enumerate(words[i]):
            tmp = 1
            for _ in range(ord(j) - ord('a')):
                tmp <<= 1
            if c == 0:
                a = tmp
            else:
                a |= tmp
        d.append(a)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if d[i] and d[j] and d[i] & d[j] == 0:
                ans = max(len(words[i]) * len(words[j]), ans)
    return ans
    """
    # 排名靠前的，上述思路优化版
    d = {}
    for w in words:
        mask = 0
        for c in set(w):
            mask |= (1 << (ord(c) - 97))
        d[mask] = max(d.get(mask, 0), len(w))
    return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


def oddEvenList(head):
    """
    328. 奇偶链表
    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
    示例 1:
    输入: 1->2->3->4->5->NULL
    输出: 1->3->5->2->4->NULL
    示例 2:
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL
    说明:
    应当保持奇数节点和偶数节点的相对顺序。
    链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
    :param head: ListNode
    :return: ListNode
    """
    if not head or not head.next:
        return head
    p1, p2, p3 = head, head.next, head.next
    while p1.next and p2.next:
        p1.next = p2.next
        p1 = p1.next
        p2.next = p1.next
        p2 = p2.next
    p1.next = p3
    return head


def lastStoneWeightII(stones):
    """
    1049. 最后一块石头的重量 II
    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
    示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
    :param stones: List[int]
    :return: int
    """
    pass


def findDuplicates(nums):
    """
    442. 数组中重复的数据
    给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
    找到所有出现两次的元素。
    你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
    示例：
    输入:
    [4,3,2,7,8,2,3,1]
    输出:
    [2,3]
    :param nums: List[int]
    :return: List[int]
    """
    # 交换与下标不对应的数字，遇到nums[i] == nums[nums[i]]时则重复
    res = set()
    for i, x in enumerate(nums):
        while nums[i] != i + 1:
            if nums[i] == nums[nums[i] - 1]:
                res.add(nums[i])
                break
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    return list(res)


def hIndex(citations):
    """
    274. H指数
    给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。
    h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”
    示例:
    输入: citations = [3,0,6,1,5]
    输出: 3
    解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
         由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
    说明: 如果 h 有多种可能的值，h 指数是其中最大的那个。
    :param citations: List[int]
    :return: int
    """
    """
    # 直接sort, 弟弟做法 55%
    citations.sort()
    n = len(citations)
    ans = 0
    for i in range(n):
        j = n - i
        if citations[i] >= j:
            ans = j
            break
    return ans
    """
    # 用nums存储每个下标位置对应引用次数的数量, 超出部分放到nums[n]里
    n = len(citations)
    nums = [0] * (n + 1)
    for i in citations:
        if i >= n:
            nums[n] += 1
        else:
            nums[i] += 1
    ans = 0
    for i in range(n, 0, -1):
        if ans + nums[i] >= i:
            return i
        else:
            ans += nums[i]
    return 0


def hIndex2(citations):
    """
    275. H指数 II
    给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。
    h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
    示例:
    输入: citations = [0,1,3,5,6]
    输出: 3
    解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
         由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
    说明:
    如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
    进阶：
    这是 H指数 的延伸题目，本题中的 citations 数组是保证有序的。
    你可以优化你的算法到对数时间复杂度吗？
    :param citations: List[int]
    :return: int
    """
    n = len(citations)
    i, j = 0, n - 1
    ans = 0
    while i <= j:
        m = i + (j - i) // 2
        ans = n - m
        if citations[m] >= n - m:
            j = m - 1
        else:
            i = m + 1
            ans -= 1
    return ans


def getHint(secret, guess):
    """
    299. 猜数字游戏
    你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。
    请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。
    请注意秘密数字和朋友的猜测数都可能含有重复数字。
    示例 1:
    输入: secret = "1807", guess = "7810"
    输出: "1A3B"
    解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
    示例 2:
    输入: secret = "1123", guess = "0111"
    输出: "1A1B"
    解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
    说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。
    :param secret: str
    :param guess: str
    :return: str
    """
    """
    # 第一大佬的思路, 先算A的, 再算所有的, 再减
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)
    """
    # 先查找值和位置都相等的pop掉, 再排序, 在双指针查找剩下相同的, 80%
    A, B = 0, 0
    ss = [x for x in secret]
    gs = [x for x in guess]
    n = len(secret)
    i = 0
    while i < n:
        if ss[i] == gs[i]:
            ss.pop(i)
            gs.pop(i)
            n -= 1
            A += 1
        else:
            i += 1
    ss.sort()
    gs.sort()
    m = len(ss)
    i, j = 0, 0
    while i < m and j < m:
        if ss[i] < gs[j]:
            i += 1
        elif ss[i] > gs[j]:
            j += 1
        else:
            B += 1
            i += 1
            j += 1
    return "%dA%dB" % (A, B)


if __name__ == '__main__':
    getHint("1123", "0111")
    # hIndex2([0,1,3,5,6])
    # hIndex([3,0,6,1,5])
    # findDuplicates([4,3,2,7,8,2,3,1])
    # x = construct_list_node([1,2,3,4,5])
    # oddEvenList(x)
    # maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"])
    # x = construct_list_node([-10,-3,0,5,9])
    # y = sortedListToBST(x)
    # print(deconstruct_tree_node(y))
    # x = construct_tree_node([5,4,8,11,null,13,4,7,2,null,null,null,null,5,1])
    # pathSum(x, 22)
    # nthSuperUglyNumber(12,[2,7,13,19])
    # a = minSteps(100)
    # print(a)
    # x = construct_list_node([1,2,3,4,5])
    # a = reverseBetween(x, 2, 4)
    # print_list_node(a)
    pass