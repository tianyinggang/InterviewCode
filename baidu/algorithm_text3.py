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
from itertools import combinations,permutations 
from sys import stdin

class point:
    def __init__(self,color,a):
        self.color=a[0]
        self.x = int(a[1])
        self.y = int(a[2])
        self.z = int(a[3])
        
class solution():
    def __init__(self,l):
        self.l = l
    pointArr = []
    def main(self,pointNumber):
        max = 0
        for i in range(pointNumber):
            for j in range(i+1,pointNumber):
                for k in range(j+1,pointNumber):
                    if self.IsSan(i,j,k) and self.color_choose(i,j,k):
                        area = self.triangle_area(i,j,k)
                        if max < area:
                            max = area
        return max
    def point_length(self,point1,point2):
        return ((self.pointArr[point1].x-self.pointArr[point2].x)**2+(self.pointArr[point1].y-self.pointArr[point2].y)**2+(self.pointArr[point1].z-self.pointArr[point2].z)**2)**0.5
    def IsSan(self,point1,point2,point3):
        a = self.point_length(point1,point2)
        b = self.point_length(point1,point3)
        c = self.point_length(point3,point2)
        if a<b+c and b<a+c and c<a+b :
            return True
        return False

    # Calculate triangular area
    def triangle_area(self,point1,point2,point3):
        a = self.point_length(point1,point2)
        b = self.point_length(point1,point3)
        c = self.point_length(point3,point2)
        p = 0.5*(a+b+c)
        area = (p*(p-a)*(p-b)*(p-c))**0.5
        return area
    def color_choose(self,i,j,k):
        ci = self.pointArr[i].color
        cj = self.pointArr[j].color
        ck = self.pointArr[k].color
        if ci == cj == ck or (ci!=cj and ci!=ck and cj!=ck):
            return True
        return False
        
if __name__=='__main__':
    while True:
        pointNumber=int(input("input a number:"))
        if pointNumber <= 50:
            break
        Arr=[]
        for i in range(pointNumber):
            point_str = readline().strip().split()
            node = point(point_str)
            Arr.append(node)
        Max=solution(Arr)
        print("%.5f"%s.main(pointNumber))
            
