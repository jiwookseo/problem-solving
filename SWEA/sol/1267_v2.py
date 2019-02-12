# 1267. [S/W 문제해결 응용] 10일차 - 작업순서 D6
# DFS 응용
# 메모리 59,640 kb
# 실행시간 250 ms
# 코드길이 884
class node:
    def __init__(self):
        self.before=[]
    def add(self,item):
        self.before.append(item)
    def remove(self,item):
        for i in range(len(self.before)):
            if self.before[i]==item:
                del self.before[i]
                return True
        return False

def next(v):
    visited[v]=True
    for i in nodes[v].before:
        if not visited[i]:
            next(i)
    print(v,end=" ")

for tc in range(1,11):
    i=input().split()
    v,e=int(i[0]),int(i[1])
    visited=[False for _ in range(v+1)]
    nodes=[node() for _ in range(v+1)]
    input_list=list(map(int,input().split()))
    temp=0
    for i in range(len(input_list)):
        if i%2:
            nodes[input_list[i]].add(temp)
        else:
            temp=input_list[i]
    print(f"#{tc}",end=" ")
    [next(i) for i in range(1,v+1) if not visited[i]]
    print("")