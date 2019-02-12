# 1267. [S/W 문제해결 응용] 10일차 - 작업순서 D6
# before 0을 소거
# 메모리 111,660 kb
# 실행시간 429 ms
# 코드길이 1,120
# DFS 응용보다 퍼포먼스가 떨어짐.
class node:
    def __init__(self):
        self.before=[]
        self.next=[]
    def addb(self,item):
        self.before.append(item)
    def addn(self,item):
        self.next.append(item)
    def remove(self,item):
        for i in range(len(self.before)):
            if self.before[i]==item:
                del self.before[i]
                return True
        return False
        

def next():
    for i in range(1,len(nodes)):
        if nodes[i].before==[] and not visited[i]:
            for j in nodes[i].next:
                nodes[j].remove(i)
            print(i,end=" ")
            visited[i]=True
            next()
            break

for tc in range(1,11):
    i=input().split()
    v,e=int(i[0]),int(i[1])
    visited=[False for _ in range(v+1)]
    nodes=[node() for _ in range(v+1)]

    input_list=list(map(int,input().split()))

    temp=0
    for i in range(len(input_list)):
        if i%2:
            nodes[input_list[i]].addb(temp)
            nodes[temp].addn(input_list[i])
        else:
            temp=input_list[i]
    result=[]
    print(f"#{tc}",end=" ")
    next()
    print("")