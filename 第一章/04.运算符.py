# 算术运算符
# print(10+4)#加法
# print(10-4)#减法
# print(10*4)#乘法
# print(10/4)#除法-->小数（float）
# print(10%4)#取模
# print(10**4)#幂
# print(10//4)#整除
#运算优先级  { ** > // / % > - + }0.
#案例1
# a=float(input("请输入数字a："))
# b=float(input("请输入数字b："))
# c=a+b
# print('a - b = ',a - b)
# print('a+b = ',c)
#注意： 由于计算机是二进制计算，所以会出现0.1+0.2!=0.3的情况，二进制精度无法准确表示所有小数，此类问题称之为精度缺失（例如：0.5-0.4=0.09999999999999998）
#案例2
# print('请输入三个整数：')
# a=int(input('a:'))
# b=int(input('b:'))
# c=int(input('c:'))
# sum=a+b+c
# print('三个整数平均数为 :',sum/3)
#案例3
# height=float(input("请输入身高："))
# weight=float(input("请输入体重："))
# BMI=weight/height*height
# print('BMI指数为：',BMI)
# 赋值运算符--> += ， -= ， *= ， /= ， %= ， //= ， **=
# 比较运算符（判断数值）--> == ， != ， > ， < ， >= ， <=
# 逻辑运算符（判断/布尔）--> and ， or ， not（取反）
#案例4
# num=float(input('请输入一个数字：'))
# print(f"{num}在10~20之间：",num<=20 and num>=10)--(简化版)-->print(f"{num}在10~20之间：", 20 >= num >= 10)