# -*- coding:utf-8 -*-
from algorithm_utils import TreeNode


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


if __name__ == '__main__':
    # words = ["gin", "zen", "gig", "msg"]
    # print(uniqueMorseRepresentations(words))
    # x = [-4, -1, 0, 3, 10]
    # print(sortedSquares(x))
    print(diStringMatch("IDID"))
