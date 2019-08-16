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


def findPoisonedDuration(timeSeries, duration):
    """
    495. 提莫攻击
    在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。
    你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
    示例1:
    输入: [1,4], 2
    输出: 4
    原因: 在第 1 秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒钟结束。
    在第 4 秒开始时，提莫再次攻击艾希，使得艾希获得另外 2 秒的中毒时间。
    所以最终输出 4 秒。
    示例2:
    输入: [1,2], 2
    输出: 3
    原因: 在第 1 秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒钟结束。
    但是在第 2 秒开始时，提莫再次攻击了已经处于中毒状态的艾希。
    由于中毒状态不可叠加，提莫在第 2 秒开始时的这次攻击会在第 3 秒钟结束。
    所以最终输出 3。
    注意：
    你可以假定时间序列数组的总长度不超过 10000。
    你可以假定提莫攻击时间序列中的数字和提莫攻击的中毒持续时间都是非负整数，并且不超过 10,000,000。
    :param timeSeries: List[int]
    :param duration: int
    :return: int
    """
    if not timeSeries or len(timeSeries) == 0:
        return 0
    n = len(timeSeries)
    ans = duration
    for i in range(n-1):
        ans += min(timeSeries[i+1] - timeSeries[i], duration)
    return ans


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
    """
    # dfs + 剪枝 19%
    def dfs(stones, i, cur):
        if i >= len(stones) and cur >= 0:
            nonlocal ans
            ans = min(ans, cur)
            return
        if not visited[i][cur + stones[i]]:
            visited[i][cur + stones[i]] = True
            dfs(stones, i + 1, cur + stones[i])
        if not visited[i][abs(cur - stones[i])]:
            visited[i][abs(cur - stones[i])] = True
            dfs(stones, i + 1, abs(cur - stones[i]))
    ans = float("inf")
    n = len(stones)
    m = sum(stones)
    visited = [[False] * (m + 1) for _ in range(n)]
    dfs(stones, 0, 0)
    return ans
    """
    # 把所有操作的结果存到set
    dp = {0}
    sumA = sum(stones)
    for a in stones:
        dp |= {a + i for i in dp}
    return min(abs(sumA - i * 2) for i in dp)


def maxRotateFunction(A):
    """
    396. 旋转函数
    给定一个长度为 n 的整数数组 A 。
    假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：
    F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。
    计算F(0), F(1), ..., F(n-1)中的最大值。
    注意:
    可以认为 n 的值小于 105。
    示例:
    A = [4, 3, 2, 6]
    F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
    F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
    F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
    F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
    所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
    :param A: List[int]
    :return: int
    """
    # 按F函数变化过程推, F(0) -> F(1): 每个位置加一个自身后减去所有最后一位(6) -> F(1) = F(0) + sum(A) - n*A[n-1]
    n = len(A)
    if n == 0: return 0
    cur, m = 0, 0
    for i in range(n):
        cur += i * A[i]
        m += A[i]
    ans = cur
    for i in range(n-1, 0, -1):
        cur += m - (n * A[i])
        ans = max(ans, cur)
    return ans


def findFrequentTreeSum(root):
    """
    508. 出现次数最多的子树元素和
    给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。
    示例 1
    输入:
      5
     /  \
    2   -3
    返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
    示例 2
    输入:
      5
     /  \
    2   -5
    返回 [2]，只有 2 出现两次，-5 只出现 1 次。
    提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
    :param root: TreeNode
    :return: List[int]
    """
    def helper(node):
        if node:
            left = helper(node.left) if node.left else 0
            right = helper(node.right) if node.right else 0
            nonlocal res
            cur = node.val + left + right
            if not cur in res:
                res[cur] = 0
            res[cur] += 1
            return cur
    res = {}
    if not root:
        return []
    helper(root)
    mv = max(res.values())
    return [x[0] for x in list(filter(lambda x:x[1]==mv, res.items()))]


def findTargetSumWays(nums, S):
    """
    494. 目标和
    给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
    返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
    示例 1:
    输入: nums: [1, 1, 1, 1, 1], S: 3
    输出: 5
    解释:
    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    一共有5种方法让最终目标和为3。
    注意:
    数组的长度不会超过20，并且数组中的值全为正数。
    初始的数组的和不会超过1000。
    保证返回的最终结果为32位整数。
    :param nums: List[int]
    :param S: int
    :return: int
    """
    """
    # 背包问题
    n = len(nums)
    if n == 0 or abs(S) > 1000: return 0
    dp = [[0] * 1001 for _ in range(n)]
    dp[0][nums[0]] = 1 if nums[0] > 0 else 2
    for i in range(1, n):
        for j in range(1001):
            minus = 0 if abs(j - nums[i]) > 1000 else dp[i-1][abs(j-nums[i])]
            plus = 0 if j + nums[i] > 1000 else dp[i-1][j+nums[i]]
            dp[i][j] = minus + plus
    return dp[n-1][abs(S)]
    """
    """
    # dfs + memo
    def dfs(i, cur):
        if i == len(nums):
            return 1 if cur == S else 0
        if memo[i][cur+1000] != -1:
            return memo[i][cur+1000]
        res = dfs(i+1, cur + nums[i]) + dfs(i+1, cur - nums[i])
        memo[i][cur+1000] = res
        return res
    memo = [[-1] * 2001 for _ in range(len(nums))]
    return dfs(0, 0)
    """
    # 非递归dp
    n = len(nums)
    dp = {(0, 0): 1}
    for i in range(1, n + 1):
        for j in range(-sum(nums), sum(nums) + 1):
            dp[(i, j)] = dp.get((i-1, j-nums[i-1]), 0) + dp.get((i-1, j+nums[i-1]), 0)
    return dp.get((n, S), 0)


def findDiagonalOrder(matrix):
    """
    498. 对角线遍历
    给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
    示例:
    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出:  [1,2,4,7,5,3,6,8,9]
    解释: ↗ ↙ ↗ ↙ ↗
    说明:
    给定矩阵中的元素总数不会超过 100000 。
    :param matrix: List[List[int]]
    :return: List[int]
    """
    M = len(matrix)
    if M == 0: return []
    N = len(matrix[0])
    # 1是up
    direction = 1
    res = [0] * (M * N)
    i, j = 0, 0
    for k in range(M*N):
        res[k] = matrix[i][j]
        if direction:
            if i == 0 or j == N - 1:
                direction ^= 1
                if j < N - 1:
                    j += 1
                else:
                    i += 1
            else:
                j += 1
                i -= 1
        else:
            if j == 0 or i == M - 1:
                direction ^= 1
                if i < M - 1:
                    i += 1
                else:
                    j += 1
            else:
                j -= 1
                i += 1
    return res


def findSubsequences(nums):
    """
    491. 递增子序列
    给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
    示例:
    输入: [4, 6, 7, 7]
    输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
    说明:
    给定数组的长度不会超过15。
    数组中的整数范围是 [-100,100]。
    给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
    :param nums: List[int]
    :return: List[List[int]]
    """
    def recursion(nums):
        if len(nums) == 1: return [tuple(nums)]
        res = set()
        for i in range(len(nums) - 1):
            last = recursion(nums[i + 1:])
            for x in last:
                res.add(x)
                cur = (nums[i], ) + x
                if nums[i] <= x[0] and not cur in res:
                    res.add(cur)
            res.add((nums[i], ))
        return res
    return [list(x) for x in recursion(nums) if len(x) > 1]


def distributeCoins(root):
    """
    979. 在二叉树中分配硬币
    给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
    在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。
    返回使每个结点上只有一枚硬币所需的移动次数。
    示例 1：
    输入：[3,0,0]
    输出：2
    解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。
    示例 2：
    输入：[0,3,0]
    输出：3
    解释：从根结点的左子结点开始，我们将两枚硬币移到根结点上 [移动两次]。然后，我们把一枚硬币从根结点移到右子结点上。
    示例 3：
    输入：[1,0,2]
    输出：2
    示例 4：
    输入：[1,0,0,null,3]
    输出：4
    提示：
    1<= N <= 100
    0 <= node.val <= N
    :param root: TreeNode
    :return: int
    """
    """
    # abs
    def dfs(p):
        if not p: return 0
        left, right = dfs(p.left), dfs(p.right)
        nonlocal ans
        ans += abs(left) + abs(right)
        return p.val + left + right - 1
    ans = 0
    dfs(root)
    return ans
    """
    # 节点数与求和对比
    def dfs(p):
        if not p: return 0, 0
        left, right = dfs(p.left), dfs(p.right)
        cv = p.val + left[0] + right[0]
        cn = 1 + left[1] + right[1]
        nonlocal ans
        ans += abs(cn - cv)
        return cv, cn
    ans = 0
    dfs(root)
    return ans


def pathInZigZagTree(label):
    """
    1104. 二叉树寻路
    在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
    如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
    而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
    给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
                  1
              3       2
            4   5   6   7
    示例 1：
    输入：label = 14
    输出：[1,3,4,14]
    示例 2：
    输入：label = 26
    输出：[1,2,6,10,26]
    提示：
    1 <= label <= 10^6
    :param label: int
    :return: List[int]
    """
    x = 0
    while label >> x:
        x += 1
    print(x)
    res = []
    while x > 1:
        res.append(label)
        if x & 1:
            label = ((1 << (x - 2)) - 1) ^ (label // 2)
        else:
            label = (label ^ ((1 << (x - 1)) - 1)) // 2
        x -= 1
    res.append(1)
    return res[::-1]


def change(amount, coins):
    """
    518. 零钱兑换 II
    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
    示例 1:
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    示例 2:
    输入: amount = 3, coins = [2]
    输出: 0
    解释: 只用面额2的硬币不能凑成总金额3。
    示例 3:
    输入: amount = 10, coins = [10]
    输出: 1
    注意:
    你可以假设：
    0 <= amount (总金额) <= 5000
    1 <= coin (硬币面额) <= 5000
    硬币种类不超过 500 种
    结果符合 32 位符号整数
    :param amount: int
    :param coins: List[int]
    :return: int
    """

    def dfs(a, p):
        if dp[a] >= 0:
            return dp[a]
        if a == 0:
            return 1
        cur = 0
        for x in coins[::-1]:
            if x <= min(p, a):
                cur += dfs(a - x, x)
        dp[a] = cur
        return cur
    dp = [-1] * (amount+1)
    if amount == 0:
        return 1
    if coins == []:
        return 0
    ans = dfs(amount, max(coins))
    print(ans)
    print(dp)
    return ans

if __name__ == '__main__':
    change(5, [1,2,5])
    # pathInZigZagTree(14)
    # x = construct_tree_node([1,0,0,null,3])
    # a = distributeCoins(x)
    # print(a)
    # a = findSubsequences([1,3,5,7])
    # print(a)
    # findDiagonalOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])
    # findTargetSumWays([1,1,1,1,1], 3)
    # x = construct_tree_node([5,2,-5])
    # findFrequentTreeSum(x)
    # lastStoneWeightII([2,7,4,1,8,1])
    # getHint("1123", "0111")
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