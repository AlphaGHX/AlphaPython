n = int(input())
li = list(map(int, input().split()))
li.sort(reverse = True) #从大到小
print(li)
li.sort() #从小到大
print(li)