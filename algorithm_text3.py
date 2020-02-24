# 时间限制：C/C++ 1秒，其他语言2秒
# 空间限制：C/C++ 32M，其他语言64M
# 三维空间中有N个点，每个点可能是三种颜色的其中之一，三种颜色分别是红绿蓝，分别用'R', 'G', 'B'表示。 
# 现在要找出三个点，并组成一个三角形，使得这个三角形的面积最大。
# 但是三角形必须满足：三个点的颜色要么全部相同，要么全部不同。

# 输入描述:
# 首先输入一个正整数N三维坐标系内的点的个数.(N <= 50) 

# 接下来N行，每一行输入 c x y z，c为'R', 'G', 'B' 的其中一个。x，y，z是该点的坐标。(坐标均是0到999之间的整数)

# 输出描述:
# 输出一个数表示最大的三角形面积，保留5位小数。

# 输入例子1:
# 5
# R 0 0 0
# R 0 4 0
# R 0 0 3
# G 92 14 7
# G 12 16 8

# 输出例子1:
# 6.00000
import numpy as np
import itertools
#create point map
while True:
    pointNumber=int(input("input a number:"))
    if pointNumber <= 50:
        break
pointArr=[]
class point:
    def __init__(self,color,x,y,z):
        self.color=color
        self.x=x
        self.y=y
        self.z=z
for i in range(int(pointNumber)):
    a=input().split()#需要修改省掉a
    point.color=a[0]
    point.x=a[1]
    point.y=a[2]
    point.z=a[3]
    pointArr.append(point)
triangleARR=[]
for i in range(1,len(pointArr)+1):
    iter = itertools.combinations(pointArr,i)
    triangleARR.append(list(iter))


def triangle_area(triangleArr):
    def point_range(point1,point2):
        Range=np.sqrt((np.power(point1.x-point2.x,2)+np.power(point1.y-point2.y,2)+np.power(point1.z-point2.z,2)))
        return Range
    triangleRange1 = point_range(triangleArr[0],triangleArr[1])
    triangleRange2 = point_range(triangleArr[2], triangleArr[1])
    triangleRange3 = point_range(triangleArr[0], triangleArr[2])
    Range123=triangleRange1+triangleRange2+triangleRange3
    area=np.sqrt(Range123*(Range123-triangleRange1)*(Range123-triangleRange2)*(Range123-triangleRange3))
    return area