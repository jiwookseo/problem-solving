i=input().split(" ")
n=int(i[0])
q=int(i[1])
query=[]
personnel=[0]*n
ordered=[]

for i in range(q):
    query.append(input().split(" "))

def reserv(sq):
    result=personnel.index(0)
    while(1):
        if result+sq>n:
            return None
        elif sum(personnel[result:result+sq])==0:
            return result
        else:
            if result+1==n:
                return None
            else :
                try:
                    result=personnel.index(0,result+1)
                except:
                    return None

def check(ordn, pern):
    start,end=ordered[ordn-1][0] #(L,R)
    ordered[ordn-1][1]+=pern
    if ordered[ordn-1][1]==0:
        for i in range(start,end+1):
            personnel[i]=0
        print(f"CLEAN {start+1} {end+1}")

new_ind=1
for row in query:
    if row[0]=='new':
        per=int(row[1])
        sq=int(row[2])
        result=reserv(sq)
        if result!=None:
            ordered.append([(result,result+sq-1),per])
            print(f"{result+1} {result+sq}")
            for i in range(result,result+sq):
                personnel[i]=1
            new_ind+=1
        else:
            print("REJECTED")
    
    elif row[0]=='in':
        ordn=int(row[1])
        per=int(row[2])
        check(ordn,per)

    elif row[0]=='out':
        ordn=int(row[1])
        per=int(row[2])
        check(ordn,-per)