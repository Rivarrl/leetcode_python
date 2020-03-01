import sys
import math
# 输入圆点ox，oy，扇形中轴方向点fx，fy，扇形角度r，目标点px，py
# 问目标点是否落在扇形区域内
# 输入：0 0 1 1 90 3 5
# 输出：1

line = sys.stdin.readline().strip()
ox, oy, fx, fy, r, px, py = map(int, line.split())

fx -= ox
fy -= oy
px -= ox
py -= oy
pi2 = 2 * math.pi
if px == 0:
    a_op = 0
else:
    t = py/px
    a_op = math.atan(t)
    a_op = (a_op / pi2) * 360
if fx == 0:
    a_of = 0
else:
    a_of = math.atan(fy/fx)
    a_of = (a_of / pi2) * 360

a_ofs, a_ofe = (a_of - r/2 + 360) % 360, (a_of + r/2 + 360) % 360
if a_ofs < a_ofe:
    if a_ofs <= a_op <= a_ofe:
        print(1)
    else:
        print(0)
else:
    if 0 <= a_op <= a_ofe or a_op >= a_ofs:
        print(1)
    else:
        print(0)