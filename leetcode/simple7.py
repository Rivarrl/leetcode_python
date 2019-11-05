from typing import List

from algorithm_utils import *

def transformArray(arr: List[int]) -> List[int]:
    """
    首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。
    第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：
    假如一个元素小于它的左右邻居，那么该元素自增 1。
    假如一个元素大于它的左右邻居，那么该元素自减 1。
    首、尾元素 永不 改变。
    过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。
    示例 1：
    输入：[6,2,3,4]
    输出：[6,3,3,4]
    解释：
    第一天，数组从 [6,2,3,4] 变为 [6,3,3,4]。
    无法再对该数组进行更多操作。
    示例 2：
    输入：[1,6,3,4,3,5]
    输出：[1,4,4,4,4,5]
    解释：
    第一天，数组从 [1,6,3,4,3,5] 变为 [1,5,4,3,4,5]。
    第二天，数组从 [1,5,4,3,4,5] 变为 [1,4,4,4,4,5]。
    无法再对该数组进行更多操作。
    提示：
    1 <= arr.length <= 100
    1 <= arr[i] <= 100
    """
    n = len(arr)
    arr2 = [e for e in arr]
    def change(arr, arr2):
        for i in range(1, n-1):
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                arr2[i] += 1
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                arr2[i] -= 1
    change(arr, arr2)
    while arr2 != arr:
        arr = arr2[:]
        change(arr, arr2)
    return arr


def minimumSwap(s1: str, s2: str) -> int:
    """
    5247. 交换字符使得字符串相同
    有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
    每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
    交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
    最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。
    示例 1：
    输入：s1 = "xx", s2 = "yy"
    输出：1
    解释：
    交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。
    示例 2：
    输入：s1 = "xy", s2 = "yx"
    输出：2
    解释：
    交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
    交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
    注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
    示例 3：
    输入：s1 = "xx", s2 = "xy"
    输出：-1
    示例 4：
    输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
    输出：4
    提示：
    1 <= s1.length, s2.length <= 1000
    s1, s2 只包含 'x' 或 'y'。
    """
    from collections import Counter, defaultdict
    if len(s1) != len(s2): return -1
    d1 = Counter(s1)
    d2 = Counter(s2)
    for c in ['x', 'y']:
        if (d1[c] + d2[c]) & 1: return -1
    d = defaultdict(int)
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            d[c1] += 1
    return sum(d.values()) // 2 + int(d['x'] & 1)


def repeatedStringMatch(A: str, B: str) -> int:
    """
    686. 重复叠加字符串匹配
    给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
    举个例子，A = "abcd"，B = "cdabcdab"。
    答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
    注意:
     A 与 B 字符串的长度在1和10000区间范围内。
    """
    x = len(B) // len(A)
    if str(A*x).find(B): return x
    if str(A*(x+1)).find(B): return x+1
    if str(A*(x+2)).find(B): return x+2
    return -1


@timeit
def minDiffInBST(root: TreeNode) -> int:
    """
    783. 二叉搜索树结点最小距离
    给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
    示例：
    输入: root = [4,2,6,1,3,null,null]
    输出: 1
    解释:
    注意，root是树结点对象(TreeNode object)，而不是数组。
    给定的树 [4,2,6,1,3,null,null] 可表示为下图:
              4
            /   \
          2      6
         / \
        1   3
    最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
    注意：
    二叉树的大小范围在 2 到 100。
    二叉树总是有效的，每个节点的值都是整数，且不重复。
    """
    def dfs(p):
        if not p: return
        nonlocal last, res
        dfs(p.left)
        if last != None:
            res = min(res, p.val - last.val)
        last = p
        dfs(p.right)
    res = float('inf')
    last = None
    dfs(root)
    return res


if __name__ == '__main__':
    x = construct_tree_node([4,2,6,1,3])
    minDiffInBST(x)
    # res = minimumSwap("yyxyxxx", "xyyyxxx")
    # print(res)
    # res = transformArray([6,5,8,6,7,7,3,9,8,8,3,1,2,9,8,3])
    # print(res)
    pass