#基本数学函数
abs(-9)
max(4, 3, 11)
int(3.14)
float('12.34')
str(1.234)
bool(1)

#!!!重点，定义函数
def my_abs(x):#def用来定义函数
    if not isinstance(x, (int, float)) : return "TypeError" #isinstance用来判断x是否为int或者float
    if (x >= 0) : return x
    else : return -x
print(my_abs(-99))

def nop() : pass #定义了一个空函数,注意pass可以用来占位，使得函数没实现的时候程序能运行\

def tur(x, y) : 
    nx = x + 100
    ny = y - 100
    return nx, ny #函数可以返回多个值，并以tuple类型放回
r = tur(1, 2)
print(r)

def power(x, n = 2) : #这里使用了默认参数n
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s
print(power(2)) #所以当调用的时候可以不写第二个参数

def calc(*numbers) : #使用可变参数，可以接受任意数量的参数，类型是tuple
    sum = 0
    for n in numbers :
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print(*nums) #同样可以简化参数的传递
