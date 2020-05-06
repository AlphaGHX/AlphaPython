def sort(a) :
    n = len(a)
    for i in range(n) :
        for j in range(i + 1, n) :
            if a[j] < a[i] :
                t = a[j]
                a[j] = a[i]
                a[i] = t

a = []

n = int(input("请输入需要排序的数的数量\n"))

for i in range(0, n) :
    a.append(int(input("依次输入需要排序的第" + str(i + 1) + "个数\n")))

sort(a)

print("排序后数组:")
for i in a :
    print (i)