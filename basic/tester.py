from algorithm_utils import *

@timeit
def init_array(n, m):
    x = [[0x3fffff] * n for _ in range(m)]


if __name__ == '__main__':
    # init_array(10, 100000)
    # init_array(100000, 10)
    s = {1, 3}
    s.update({3})
    print(s)
    pass