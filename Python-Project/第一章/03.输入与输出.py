#获取键盘信息-->input（）
# name = input("What's your name:")
# age = input("How old are you:")
#
# print(f"Hello,{name}\nYou are {age} years old")

#案例1
# toal = 1000
# m = input("请输入密码：")
# if m == "123456":
#     print("密码正确")
# else:
#     print("密码错误,请重新输入")
#
# l = input("请输入取款金额：")#input() 输出内容为str不可参与计算，需要转型--->int（）
# print(f"您的存款原有{toal}元,现已取出{l},卡内剩余{toal - int(l)}元")

#案例2
# num1 = input("请输入数字1：")
# num2 = input("请输入数字2：")
# #print(f"结果为：{num1}+{num2}={num1 + num2}")
# # --->输出结果为24，，原因是input()输出类型是str，必须使用转义符int()转换数据类型
# print(f"结果为：{num1}+{num2}={int(num1)+int(num2)}")

#运算符
# print(10+4)#加法
# print(10-4)#减法
# print(10*4)#乘法
# print(10/4)#除法-->小数（float）
# print(10%4)#取模
# print(10**4)#幂
# print(10//4)#整除
#运算优先级  { ** > // / % > - + }
#案例1
a=float(input("请输入数字a："))
b=float(input("请输入数字b："))
c=a+b
print('a - b = ',a - b)
print('a+b = ',c)
#注意： 由于计算机是二进制计算，所以会出现0.1+0.2!=0.3的情况，二进制精度无法准确表示所有小数，此类问题称之为精度缺失（例如：0.5-0.4=0.09999999999999998）
