class Queue:
    def __init__(self):
        self.size = n ** 2
        self.init = None
        self.storage = [self.init] * self.size
        self.front = -1
        self.rear = -1

    def enQueue(self, item):
        self.rear += 1
        self.storage[self.rear] = item

    def deQueue(self):
        self.front += 1
        return self.storage[self.front]

    def isEmpty(self):
        return self.front == self.rear


def land(r, c):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    for i in range(4):
        tr, tc = r + dr[i], c + dc[i]
        if 0 <= tr < n and 0 <= tc < n:
            if apt[tr][tc] == "1":
                apt[tr][tc] = "0"
                q.enQueue((tr, tc))


n = int(input())
apt = [list(input()) for _ in range(n)]
result = []
while True:
    check = False
    for i in range(n):
        for j in range(n):
            if apt[i][j] == "1":
                apt[i][j] = "0"
                r, c = i, j
                check = True
                break
        if check:
            break
    if check:
        q = Queue()
        q.enQueue((r, c))
        while not q.isEmpty():
            land(*q.deQueue())
        result.append(q.rear + 1)
    else:
        break
result.sort()
print(len(result))
for i in result:
    print(i)
