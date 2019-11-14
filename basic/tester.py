from algorithm_utils import *

@timeit
def init_array(n, m):
    # 二维数组m和n值相差很大的时候，影响时间的是第二个维度，第二个维度其实是建立m个一维数组，反复开空间耗时，所以m大的耗时
    x = [[0x3fffff] * n for _ in range(m)]


@timeit
def carrots(x, n):
    """
    拔萝卜，1-n编号的萝卜围成一圈，从1开始每次数x个萝卜就拔掉一个萝卜，输出拔萝卜编号的顺序
    """
    arr = [i+1 for i in range(n)]
    i, r = 0, n
    while r > 0:
        last, i = i, (i - 1 + x) % r
        for j in range(i, r-1):
            arr[j], arr[j+1] = arr[j+1], arr[j]
        r -= 1
    return arr[::-1]


@timeit
def carrots2(x, n):
    arr = [i+1 for i in range(n)]
    arr = [0] + arr
    r = n + 1
    i, res = 1, []
    while r > 1:
        i += x - 1
        if i >= r: i = (i + x//r + 1) % r
        res.append(arr.pop(i))
        r -= 1
    return res


@timeit
def carrots3():
    all_radish = [1, 2, 3, 4, 5, 6, 7]
    count = 0
    answer = []
    radish = 0
    while all_radish:
        n = len(all_radish)
        radish %= n
        while radish < n:
            count += 1
            if count == 3:
                answer.append(all_radish[radish])
                count = 0
                del all_radish[radish]
                n -= 1
            else:
                radish += 1
    return answer


# 分别尝试非递归遍历(n=3)"a-c"的所有组合，按长度从小到大输出
# 组合内的每个字符从左到右都是字典序，比如："ab"算，"ba"不算
# 例如：abc，输出：a,b,c,ab,ac,bc,abc
# 相同长度的字符之间可以无序，如abc还可以输出：b,c,a,ac,bc,ab,abc
def dict_collections(n):
    """
    bfs位运算
    """
    def to_str(bi, s):
        r = ""
        i = 0
        while bi >> i:
            if (bi >> i) & 1:
                r += s[i]
            i += 1
        return r
    s = ''
    for i in range(n):
        s += chr(ord('a') + i)
    up = 1 << n
    stk = [1]
    while stk:
        i = stk.pop()
        while i < up:
            print(to_str(i, s))
            i <<= 1
            stk.insert(0, i + 1)


if __name__ == '__main__':
    # carrots3()
    # carrots(3, 7)
    carrots2(3, 7)
    # dict_collections(5)
    # init_array(10, 600000)
    # init_array(600000, 10)
    pass