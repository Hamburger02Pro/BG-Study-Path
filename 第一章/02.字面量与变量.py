# # 字面量的写法
# print(100) # 整数(int)
# print(3.14) # 浮点数/小数(float)
# print(True) # 布尔（bool）
# print(False) # 布尔(bool)
# print("Hello Python") # 字符串(str)
# print("-------------") # 字符串(str)
# print(None) # 空值(NoneType)
#
# # 布尔类型本质也是整数类型（True--1,False--0）
# print(True - 1)
# print(False + 2)

# 变量  (Python 是动态类型语言，单变量可以储存多类型数值)
# num = 114.3
# print(num)
#
# num = num + 1
# print(num)
#
# num ="OK"
# print(num)

# # 案例1
# base = 20.7
# new= 50
# # 等效 --> base,new = 20.7 , 50
# print("初始播放量为：",base,"W")
# print("第一个月播放量为：",base + new,"W")
# print("第二个月播放总量为：",base + new + new,"W")

# 标识符

# 靠中间变量完成数值交换
# a = 100
# b = 200
# c = 300
# print("初始值为",a,b,c)
# t = c
# c = a
# a = b
# b = t
# print("交换后数值为",a,b,c)

# 常见数据类型
#  int -->整数
#  float-->浮点数
#  str-->字符串
#  bool-->布尔
#  NoneType-->None

# type()
# num = 10
# print(num)
# print(type(num))

# isinstance(数据，类型)-->输出结果为布尔值
# num=10
# print(num)
# print(isinstance(num,int))

#  字符串
# 单引号
# s1 = "APPLE"
# s2 = 'Banana'
# s3 = """(空行)
# 多字符串，\n支持换行\n支持转义字符\t缩进字符
# """# 注释放结尾
# s4 = 'It‘s very good !'
# s5 = "Hello 的意思是\"您好\""
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(type(s1))
# 字符串拼接
a1 = "111122"
a2 = "223333"
s1 = "hello"
s2 = "world"
name = "XiaoZhu"
age = 16
pro = "Python"
print(a1+a2)
#方法一
print("Python 基础："+s1+","+s2)
print("Name:"+name+"\nAge:",age,"\nPro:"+pro)#age属于int类型，想和字符串拼接需要用转义字符str(age)
#方法二-->%s
print("\nName : %s \nAge : %s \nPro : %s"% (name,age,pro))
#方法三-->f"...{}"
print(f"\nName:{name}\nAge:{age}\nPro:{pro}")