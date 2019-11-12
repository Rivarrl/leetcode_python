from algorithm_utils import *

@timeit
def init_array(n, m):
    x = [[0x3fffff] * n for _ in range(m)]


# 分别尝试递归/非递归遍历(n=3)"a-c"的所有组合，按长度从小到大输出
# 组合内的每个字符从左到右都是字典序，比如："ab"算，"ba"不算
# 例如：abc，输出：a,b,c,ab,ac,bc,abc
# 相同长度的字符之间可以无序，如abc还可以输出：b,c,a,ac,bc,ab,abc
def dict_collections(n):
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
    dict_collections(5)
    # init_array(10, 600000)
    # init_array(600000, 10)
    pass