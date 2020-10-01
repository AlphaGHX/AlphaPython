N = 100010
idx = 0
h = [-1] * N
e = [0] * N
ne = [0] * N


def insert(x):
    global idx
    k = (x % N + N) % N
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1


def query(x):
    k = (x % N + N) % N
    i = h[k]
    while (i != -1):
        if (e[i] == x):
            return 1
        i = ne[i]
    return 0


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        op, x = input().split()
        x = int(x)
        if (op == 'I'):
            insert(x)
        else:
            if (query(x)):
                print("Yes")
            else:
                print("No")