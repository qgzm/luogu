# 使用者：姜海波
# 创建时间：2022/9/4  10:59
import numpy as numpy

fx = [0, -2, -1, 1, 2, 2, 1, -1, -2]
fy = [0, 1, 2, 2, 1, -1, -2, -2, -1]
# 马可以走到的位置

f = numpy.zeros(shape=(40, 40))
s = numpy.zeros(shape=(40, 40))
# print(a)
c = input('b点位置,m点位置:').split()
bx, by, mx, my = eval(c[0]), eval(c[1]), eval(c[2]), eval(c[3])
# 坐标+2以防止越界
bx += 2
by += 2
mx += 2
my += 2
f[2][1] = 1
s[mx][my] = 1
for i in range(1, 9):
    s[mx + fx[i]][my + fy[i]] = 1
    i += 1
for i in range(2, bx + 1):
    for j in range(2, by + 1):
        if s[i][j]:
            continue
        f[i][j] = f[i - 1][j] + f[i][j - 1]
        j += 1
    i+=1
print(int(f[bx][by]))
