n = int(input())
li = list(map(int, input().split()))
def find(x):
    l = 0
    r = n - 1
    while l < r :
        m = l + r >> 1
        if li[m] >= x : r = m
        else : l = m + 1
    return l
x = int(input())
print(find(x))