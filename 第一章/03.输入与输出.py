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