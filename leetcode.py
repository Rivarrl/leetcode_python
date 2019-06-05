# -*- coding utf-8 -*-
import re
from queue import Queue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Axis:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RainNode:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def __lt__(self, other):
        return int(self.h) < int(other.h)


class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        return '\\'.join(longUrl.split('/'))

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return '/'.join(shortUrl.split('\\'))


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self._stack)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        length = len(nums)
        if length == 0:
            self.record = [0]
        else:
            self.record = [nums[0]]
            for i in range(1, length):
                self.record.append(nums[i] + self.record[i - 1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0 or j == 0:
            return self.record[max(i, j)]
        else:
            return self.record[j] - self.record[i - 1] if i < j else self.record[i] - self.record[j - 1]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            try:
                return [i, nums.index(target - n, i + 1)]
            except Exception as e:
                pass

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        st = 0
        r = []
        while l1 or l2:
            if l1 and l2:
                l1v, l2v = l1.val, l2.val
            else:
                l1v = l1.val if l1 else 0
                l2v = l2.val if l2 else 0
            r.append((l1v + l2v + st) % 10)
            st = 0 if l1v + l2v + st < 10 else 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if st == 1:
            r.append(st)
        return self.reverse(r)

    def reverse(self, ls):
        x = None
        for l in ls[::-1]:
            r = ListNode(l)
            r.next = x
            x = r
        return x

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_dist = {}
        begin, i_len = 0, 0
        l = len(s)
        for i in range(l):
            if s[i] in c_dist.keys():
                index = c_dist[s[i]] + 1
                [c_dist.pop(s[x]) for x in range(begin, index)]
                i_len = i - begin if i - begin > i_len else i_len
                begin = index
            c_dist[s[i]] = i
        c_len = c_dist.values().__len__()
        if i_len < c_len:
            i_len = c_len
        return i_len

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        aa = []
        aba = []
        l = len(s) - 1
        left, right = 0, 0
        for i, x in enumerate(s):
            if i > 0:
                if s[i] == s[i - 1]:
                    aa.append((2 * i - 1) / 2)
                if i > 1:
                    if s[i] == s[i - 2]:
                        aba.append(i - 1)

        for e in aa:
            st = int(e - 0.5)
            ed = int(e + 0.5)
            r = int(e + 0.5) if l - e > e else int(l - e + 0.5)
            for i in range(r):
                if s[st] == s[ed]:
                    if ed - st > right - left:
                        left, right = st, ed
                else:
                    break
                st = st - 1
                ed = ed + 1

        for e in aba:
            st, ed = e, e
            r = e if l - e > e else l - e
            for i in range(r):
                st = st - 1
                ed = ed + 1
                if s[st] == s[ed]:
                    if ed - st > right - left:
                        left, right = st, ed
                else:
                    break
        return s[left:right + 1]

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1]) if len(s.replace(" ", "")) > 0 else 0

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        for s in S:
            total = total + 1 if s in J else total
        return total

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid)
        hor = [max([gg for gg in g]) for g in grid]
        ver = [max([grid[i][j] for i in range(l)]) for j in range(l)]
        print(hor)
        print(ver)
        total = 0
        for i in range(l):
            for j in range(i, l):
                mini = min(hor[i], ver[j])
                if grid[i][j] < mini:
                    total += mini - grid[i][j]
                if i != j:
                    mini2 = min(hor[j], ver[i])
                    if grid[j][i] < mini2:
                        total += mini2 - grid[j][i]
        print(total)
        return total

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}
        for email in emails:
            dic[email.split("@")[0].split("+")[0].replace(".", "") + email.split("@")[-1]] = 1
        return dic.__len__()

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        a = ord('a')
        A = ord('A')
        Z = ord('Z')
        x = a - A
        for s in str:
            if A <= ord(s) <= Z:
                str = str.replace(s, chr(ord(s) + x))
        return str

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 1:
            return TreeNode(nums[0])
        q = TreeNode("&")
        p = q
        self.partition_sort_remix(nums, p, 0)
        return q.left

    def partition_sort_remix(self, nums, q, direction):
        mx = max(nums)
        idx = nums.index(mx)
        lnums = nums[:idx]
        rnums = nums[idx + 1:]
        ll = len(lnums)
        lr = len(rnums)
        if direction == 0:
            q.left = TreeNode(mx)
            q = q.left
        if direction == 1:
            q.right = TreeNode(mx)
            q = q.right
        if ll > 0:
            self.partition_sort_remix(lnums, q, 0)
        if lr > 0:
            self.partition_sort_remix(rnums, q, 1)

    def addTwoNumbersv2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        p = ret
        shift_add = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            add = shift_add + x + y
            shift_add = add // 10
            p.next = ListNode(add % 10)
            p = p.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if shift_add > 0:
            p.next = ListNode(shift_add)
        return ret.next

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        aa, ab = [], []
        for a in A:
            if a % 2 == 0:
                aa.append(a)
            else:
                ab.append(a)
        aa.extend(ab)
        return aa

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[ab ^ 1 for ab in a[::-1]] for a in A]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [0] * (n + 1)
        l[0] = 1
        l[1] = 1
        if n == 1:
            return l[1]
        else:
            for i in range(2, n + 1):
                l[i] = l[i - 1] + l[i - 2]
        return l[n]

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y
        count = 0
        while a != 0:
            count += a % 2
            a = a // 2
        return count

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return False if (moves.count("U") != moves.count("D") or moves.count("L") != moves.count("R")) else True

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        aa, ab = [], []
        for a in A:
            if a % 2 == 0:
                aa.append(a)
            else:
                ab.append(a)
        aba = []
        for a, b in zip(aa, ab):
            aba.append(a)
            aba.append(b)
        return aba

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        j = len(S) - 1
        R = list(S)
        while i < j:
            if not self.isLetter(S[i]):
                i += 1
            if not self.isLetter(S[j]):
                j -= 1
            if self.isLetter(S[i]) and self.isLetter(S[j]):
                R[i], R[j] = R[j], R[i]
                i += 1
                j -= 1
        return "".join(R)

    def isLetter(self, q):
        return q >= 'a' and q <= 'z' or q >= 'A' and q <= 'Z'

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        import re
        pattern = "(^[qwertyuiop]+$)|(^[asdfghjkl]+$)|(^[zxcvbnm]+$)"
        return [word for word in words if re.fullmatch(pattern, word.lower())]

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.extend([0] * 2)
        n = len(nums)
        r = [-1] * (n + 2)
        return self.recallRob(n - 1, nums, r)

    def recallRob(self, n, nums, r):
        if r[n] >= 0:
            return r[n]
        if n == 0 or n == 1:
            q = nums[n]
        elif n == 2:
            q = nums[n] + self.recallRob(n - 2, nums, r)
        else:
            q = max(self.recallRob(n - 2, nums, r), self.recallRob(n - 3, nums, r)) + nums[n]
        r[n] = q
        return q

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        memo = 0
        m = "狗"
        for i, p in enumerate(prices):
            m = min(m, p) if m != "狗" else p
            memo = max(p - m if m != "狗" else p, memo)
        return memo

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        record: list(list(int)) = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    record[i][j] = 1
                else:
                    record[i][j] = record[i - 1][j] + record[i][j - 1]
        return record[m][n]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        # 保证word1是较长的一个
        if l1 < l2:
            l1, l2 = l2, l1
            word1, word2 = word2, word1
        record: list(list(int)) = [[l1 + 1 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for i in range(0, l1 + 1):
            record[0][i] = i
        for j in range(1, l2 + 1):
            record[j][0] = j
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                q = 0 if word1[j - 1] == word2[i - 1] else 1
                record[i][j] = min(record[i - 1][j] + 1, record[i][j - 1] + 1, record[i - 1][j - 1] + q)
        return record[l2][l1]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        l = len(cost)
        if l > 3:
            l_2, l_1 = cost[0], cost[1]
            for c in range(2, l):
                l_2, l_1 = l_1, min(l_1, l_2) + cost[c]
            return l_1
        else:
            return min(cost[:-1])

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, s = nums[0], nums[0]
        for num in nums[1:]:
            m = max(m + num, num)
            s = max(m, s)
        return s

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0
        val = root.val
        left, right = 0, 0
        if val < L:
            right = self.rangeSumBST(root.right, L, R)
            val = 0
        elif val > R:
            left = self.rangeSumBST(root.left, L, R)
            val = 0
        else:
            right = self.rangeSumBST(root.right, L, R)
            left = self.rangeSumBST(root.left, L, R)
        return val + left + right

    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        if len(deck) <= 2:
            return deck
        for i in range(2, n):
            deck.insert(n - i, deck[-1])
            deck.pop()
        return deck

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height) - 1
        m = 0
        last = 0
        while l > m:
            minimum = min(height[l], height[m])
            sq = (l - m) * minimum
            last = max(sq, last)
            if height[m] == minimum:
                m += 1
            else:
                l -= 1
        return last

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        row = len(matrix)
        if row == 0:
            return res
        col = len(matrix[0])
        c, total = 0, row * col
        i, j, x, y = 0, 0, 1, 0
        while c < total:
            res.append(matrix[i][j])
            matrix[i][j] = 0
            c += 1
            if matrix[(i + y) % row][(j + x) % col] == 0:
                x, y = -y, x
            i += y
            j += x
        return res

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res: list(list(int)) = [[0 for _ in range(n)] for _ in range(n)]
        c = 1
        i, j, x, y = 0, 0, 1, 0
        while c <= n ** 2:
            res[i][j] = c
            if res[(i + y) % n][(j + x) % n] != 0:
                x, y = -y, x
            i += y
            j += x
            c += 1
        return res

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height) - 1
        if l < 2:
            return 0
        m = max(height)
        idx = height.index(m)
        return self.trapR(height[:idx + 1], -1, m) + self.trapR(height[idx:], 0, m)

    def trapR(self, h, idx, m):
        l = len(h) - 1
        temp, h[idx] = h[idx], -1
        m2 = max(h)
        idx2 = h.index(m2)
        h[idx] = temp
        res = 0
        # 如果次大值不在两侧则进行递归
        if 0 < idx2 < l:
            res = self.trapR(h[:idx2 + 1], -1, m2) + self.trapR(h[idx2:], 0, m2)
        else:
            # 最简接水结构，左右两侧分别是最大和次大
            for i in range(1, l):
                res += min(m2, m) - h[i]
        return res

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        stx = str(x)
        flag = 0
        if stx[0] == '-':
            flag = 1
            stx = stx[1:]
        stl = stx.split()[::-1]
        print(stl)
        sty = ''.join(stl)
        y = int(sty) if flag == 0 else -int(sty)
        y = y if -2 ** 31 < y < 2 ** 31 - 1 else 0
        return y

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        x, y, n = 0, 1, 1
        if N == 0:
            return x
        while n < N:
            x, y = y, x + y
            n += 1
        return y

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.__len__() % 2 == 1:
            return False
        while s.__len__() > 0:
            q = s.replace("{}", "").replace("[]", "").replace("()", "")
            if q.__len__() == s.__len__():
                return False
            s = q
        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        m = ""
        while i < 2 ** 10:
            try:
                n = strs[0][i]
                for each in strs[1:]:
                    if each[i] != n:
                        return m
                m += n
                i += 1
            except:
                break
        return m

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root != None else 0

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        i = 1
        m = 0
        while i < l:
            x = prices[i] - prices[i - 1]
            if x >= 0:
                m += x
            i += 1
        return m

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in range(1 << n)]

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = 0
        for i, x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)):
                res += int(x) * int(y) * (10 ** i) * (10 ** j)
        return str(res)

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 0
        lh = []
        if not head:
            return None
        if k == 0:
            return head
        while head != None:
            lh.append(head.val)
            head = head.next
            i += 1
        if i == 1:
            return ListNode(lh[0])
        k = k % i
        rh = [lh[(j + i - k) % i] for j in range(i)]
        res = ListNode(rh[-1])
        for r in rh[i - 2::-1]:
            tmp = ListNode(r)
            tmp.next = res
            res = tmp
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return [nums]
        i = 0
        res = []
        while i < l:
            if i == 0:
                res.append([nums[0]])
            else:
                tmp = []
                for r in res:
                    for j in range(len(r) + 1):
                        ar = [q for q in r]
                        ar.insert(j, nums[i])
                        tmp.append(ar)
                res = tmp
            i += 1
        return res

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split(" ")])

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1] if k < len(nums) // 2 else heapq.nsmallest(len(nums) + 1 - k, nums)[-1]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums.__len__() == 0:
            return [nums]
        res = [[nums[0]]]

        def subsetsR(i):
            restmp = []
            for each in res:
                tmp = [e for e in each]
                tmp.append(i)
                restmp.append(tmp)
            res.extend(restmp)
            res.append([i])

        for i in nums[1:]:
            subsetsR(i)
        res.append([])
        return res

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        while len(nums) > 1:
            if nums[-1] == nums[-2]:
                nums.pop()
                nums.pop()
            else:
                return nums[-1]
        return nums[-1]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 1
        m = nums[0]
        l = len(nums)
        z = l // 2
        nums.sort()
        i = 0
        for j in range(1, l):
            if nums[i] != nums[j]:
                if j - i > z:
                    return nums[i]
                i = j
        if l - i > z:
            return nums[i]
        return

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = heightMap.__len__()
        if m < 3:
            return 0
        n = heightMap[0].__len__()
        if n < 3:
            return 0
        area, h, x, y = 0, 0, 0, 1
        from queue import PriorityQueue
        pq = PriorityQueue()
        visit = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    pq.put(RainNode(i, j, heightMap[i][j]))
                    visit[i][j] = True
        while not pq.empty():
            f = pq.queue[0]
            if h < f.h:
                h += 1
            else:
                pq.get()
                for k in range(4):
                    i, j = f.x + x, f.y + y
                    x, y = -y, x
                    if i >= 0 and i < m and j >= 0 and j < n and visit[i][j] == False:
                        hh = heightMap[i][j]
                        print(i, j)
                        if hh < h:
                            area += h - hh
                        pq.put(RainNode(i, j, hh))
                        visit[i][j] = True
        return area

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rmd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        i, l = 0, len(s)
        while i < l:
            if i < l - 1 and rmd[s[i]] < rmd[s[i + 1]]:
                res += rmd[s[i + 1]] - rmd[s[i]]
                i += 1
            else:
                res += rmd[s[i]]
            i += 1
        return res

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rmd = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k, v in rmd.items():
            while num >= k:
                res += v
                num -= k
        return res

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        l = s.__len__()
        for i in range(numRows):
            j = 2 * (numRows - i) - 2
            q = 2 * i
            x = 1
            t = i
            if j <= 0 or q <= 0 or j == q:
                d = max(j, q)
                while t < l:
                    res += s[t]
                    print(t, s[t])
                    t += d
            else:
                while t < l:
                    res += s[t]
                    t = t + j if x else t + q
                    x ^= 1
        return res

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            return nums2[(n - 1) // 2] / 1.0 if n & 1 else (nums2[(n - 1) // 2] + nums2[(n - 1) // 2 + 1]) / 2.0
        t = (m + n + 1) // 2
        begin, end = 0, m
        while begin <= end:
            i = (begin + end) // 2
            j = t - i
            if i > 0 and j < n and nums1[i - 1] > nums2[j]:
                end = i - 1
            elif j > 0 and i < m and nums2[j - 1] > nums1[i]:
                begin = i + 1
            else:
                if i == 0:
                    left = nums2[j - 1]
                elif j == 0:
                    left = nums1[i - 1]
                else:
                    left = max(nums1[i - 1], nums2[j - 1])
                if i == m:
                    right = nums2[j]
                elif j == n:
                    right = nums1[i]
                else:
                    right = min(nums1[i], nums2[j])
                return left / 1.0 if (m + n) & 1 else (left + right) / 2.0
        return 0.0

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 用动态规划解决
        ls = len(s) + 1
        lp = len(p) + 1
        dp = [[False for _ in range(ls)] for _ in range(lp)]
        dp[0][0] = True
        for i in range(1, lp):
            for j in range(0, ls):
                if p[i - 1] == '.':
                    if i >= 2 and p[i - 2] == '*' and j == 0:
                        dp[i][j] = False
                    if j >= 1 and dp[i - 1][j - 1] is True:
                        dp[i][j] = True
                elif p[i - 1] == '*':
                    if dp[i - 1][j] is True:
                        dp[i][j] = True
                    elif dp[i][j - 1] is True and p[i - 2] == '.':
                        dp[i][j] = True
                    elif dp[i - 2][j] is True:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] is True and (p[i - 2] == s[j - 1] or
                                                       p[i - 2] == '.'):
                        dp[i][j] = True
                elif j >= 1 and dp[i - 1][j - 1] is True and p[i - 1] == s[j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]

    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        la = A.__len__()
        alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
        bstr = ''
        for bb in B:
            if self.wordSubsetsT(bstr, bb):
                continue
            tmp = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                   'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                   'y': 0, 'z': 0}
            for b in bb:
                tmp[b] += 1
                if tmp[b] > alphabet[b]:
                    alphabet[b] = tmp[b]
                    bstr += b
        i, j = 0, 0
        while i < la:
            if not self.wordSubsetsT(A[i], bstr):
                A.remove(A[i])
                la -= 1
                continue
            i += 1
        return A

    def wordSubsetsT(self, a, b):
        c = a
        l = c.__len__()
        for bs in b:
            c = c.replace(bs, '', 1)
            if l == c.__len__(): return False
            l = c.__len__()
        return True

    # 旋转数组
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            a = nums.pop()
            nums.insert(0, a)
            k -= 1

    def containsDuplicate(self, nums: list) -> bool:
        return set(nums).__len__() < nums.__len__()

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = nums1.__len__()
        l2 = nums2.__len__()
        if l2 < l1:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        while l1 > 0:
            i = l1 - 1
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
            else:
                nums1.pop(i)
            l1 -= 1
        return nums1

if __name__ == '__main__':
    s = Solution()
    # x = [4,7,9,7,6,7]
    # y = [5,0,0,6,1,6,2,2,4]
    # ans = s.intersect(x, y)
    ans = s.toLowerCase("Hello")
    print(ans)
    # A = [2]
    # B = [5,7,10,12]
    # rs = s.findMedianSortedArrays(A, B)
    # print(rs)
    # s1 = TreeNode(1)
    # s2 = TreeNode(2)
    # s3 = TreeNode(3)
    # s4 = TreeNode(4)
    # s5 = TreeNode(5)
    # s6 = TreeNode(6)
    # s7 = TreeNode(7)
    # s8 = TreeNode(8)
    # s9 = TreeNode(9)
    # s10 = TreeNode(10)
    # s11 = TreeNode(11)
    # s12 = TreeNode(12)
    # s13 = TreeNode(13)
    # s14 = TreeNode(14)
    # s15 = TreeNode(15)
    # s16 = TreeNode(16)
    # s17 = TreeNode(17)
    # s18 = TreeNode(18)
    # s19 = TreeNode(19)
    # s20 = TreeNode(20)
    # s20.left = s15
    # s20.right = s7
    # s3.left = s9
    # s3.right = s20
    # l0 = ListNode(0)
    # l1 = ListNode(1)
    # l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    # l6 = ListNode(6)
    # l7 = ListNode(7)
    # l8 = ListNode(8)
    # l9 = ListNode(9)
    # ll1 = ListNode(1)
    # l4.next = l5
    # l3.next = l4
    # l2.next = l3
    # l1.next = l2
