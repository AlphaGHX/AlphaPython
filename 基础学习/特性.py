#切片
L = ['cyh', 'xjh', 'yy']
print(L[:2]) #切片，取0~1的数据(不包括L[2])
print(L[1:2]) #取1~1的数据
print(L[-2:])
print(L[-2:-1]) #同样

#迭代
for ch in "str" :
    print(ch) #在字符串中迭代输出

#列表生成
li = list(range(10)) #生成0~9的列表
print(li)
li = list(range(5, 10)) #生成5~9的列表
print(li)
li = [x * x for x in range(1, 11)] #生成x * x(x由1到10)的列表
print(li)
li = [m + n for m in 'ABC' for n in 'XYZ']
print(li)