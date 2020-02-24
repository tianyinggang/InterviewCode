# 时间限制：C/C++ 1秒，其他语言2秒
# 空间限制：C/C++ 32M，其他语言64M
# 度度熊想去商场买一顶帽子，商场里有N顶帽子，有些帽子的价格可能相同。度度熊想买一顶价格第三便宜的帽子，问第三便宜的帽子价格是多少？

# 输入描述:
# 首先输入一个正整数N（N <= 50），接下来输入N个数表示每顶帽子的价格（价格均是正整数，且小于等于1000）

# 输出描述:
# 如果存在第三便宜的帽子，请输出这个价格是多少，否则输出-1

# 输入例子1:
# 10
# 10 10 10 10 20 20 30 30 40 40

# 输出例子1:
# 30
while True:
    HatNumber = int(input ("input a Number:"))
    if HatNumber>0 and HatNumber<=50:
        break
HatPrice=[]    
while True:
    HatPriceRaw = input ().split ()
    if len(HatPriceRaw) > HatNumber:
        print ("input error")
    else:
        break 
for i in range (HatNumber):
    if HatPriceRaw[i] in HatPrice:
        continue
    else:
        HatPrice.append (HatPriceRaw[i])
HatPrice.sort()
if len (HatPrice) > 2:
    print (HatPrice[2])
else:
    print ("-1")

