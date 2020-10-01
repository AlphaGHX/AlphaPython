# python的输入输出
print(r'\\\t\\')  # r''可忽略''内的转义字符
print("%-4d %-4s" % (1, "ss"))  # 格式化输出
li = map(int, input().split())  # 一行多个输入，用空格隔开。
print(' '.join(map(str, li)))  # 一行多个输出，用空格隔开。

# python的逻辑表达式
print(3 > 2 and 4 > 2)  # 相比c语言，python用and来表示&&
print(3 > 2 or 4 > 6)  # 用or来表示||
print(not 1)  # 用not表示!

# python是动态语言，也就是说一个变量可以转变类型
a = 1
print(a)
a = "1"
print(a)

# python除法的特点
print(10 / 3)  # 用‘/’会输出精确的答案
print(10 // 3)  # 用‘//’会输出整数答案

# py的字符串
print(ord('A'))  # 将A转化为字符编码
print(ord('陈'))
print("转化字符型" + chr(99))  # 将99转化为字符

# list和tuple
# list是一种有序集合，可以随时添加和删除其中的元素
classmate = ["cyh", "yy", "tt"]  # 一个list
print('\n', len(classmate))  # 输出长度
print(classmate[-1])  # 特殊的，python可以用-1表示最后一个元素
classmate.append("py")  # 调用append方法来向末尾加一个元素
classmate.insert(2, "to")  # 用inser方法来向一个指定位置插入元素
classmate.pop()  # 用pop方法删除list最后一个元素，同时可以传入参数i来删除第i个元素
print(classmate)
classmate = ["iPad", 6999, True]  # 在一个list内可以容纳不同的数据类型
print(classmate)
classmate = [1, 2, [1, 2], 3]  # 可以在list内包含list
print(classmate)
# tuple
# tuple和list非常类似，但是tuple一旦初始化就不能被修改
classmates = ("cyh", "yy", "tt")  # 一个tuple
classmates1 = (1,)  # 一个长度为1的tuple

# py的条件判断
# python的if else语句比较特别，要牢记
# print("\n输入你的年龄来判断是否有权访问")
#age = int(input())
age = 19
if age >= 18:
    print("全面的访问")
elif age >= 16:
    print("受保护的访问")
else:
    print("无权访问")

# py的循环
# for...in...循环
names = ['cyh', 'yy', 'gg']
print('\n将循环打印三行')
for name in names:
    print(name)
print(list(range(5)))  # !!!重点 通过range()来生成0到x的整数序列，然后通过list()转换为list
print('输出前两个名字')
for i in range(2):
    print(names[i])
# while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# py字典
d = {'身高': 175, '体重': 65}  # 注意用{}括号
print('身高为：', d['身高'])
