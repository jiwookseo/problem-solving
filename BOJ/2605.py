# double linked list
# 헛짓거리.. case size가 적어서 double linked list를 사용해봤자 퍼포먼스 차이 없음
# ver2 list insert method 사용한 것 코드 길이 1/5
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


n = int(input())
ns = [Node(i) for i in range(1, n+1)]
num = list(map(int, input().split()))
tail = ns[0]
for i in range(1, n):
    tail.next = ns[i]
    ns[i].prev = tail
    p = ns[i]
    if num[i] == 0:
        tail = ns[i]
    else:
        while num[i] != 0:
            p = p.prev
            num[i] -= 1
        if p.prev is None:
            p.prev, ns[i].prev, ns[i].next = ns[i], None, p
        else:
            p.prev, p.prev.next, ns[i].prev, ns[i].next = ns[i], ns[i], p.prev, p
        tail.next = None
result = []
while tail is not None:
    result.append(tail.data)
    tail = tail.prev
print(" ".join([str(i) for i in result[::-1]]))
