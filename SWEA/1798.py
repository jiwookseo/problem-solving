# 1798. 범준이의 제주도 여행 계획 D5
"""
1
21 4
141 160 240 226 202 87 214 92 177 61 94 210 83 212 89 114 123 223 118 132 
202 105 121 200 179 221 145 205 194 210 215 93 117 236 82 213 209 200 204 
173 107 183 225 145 228 169 176 201 111 193 103 224 60 157 193 165 101 
159 132 122 108 134 235 151 166 78 132 143 163 84 180 183 221 177 
108 119 186 238 175 108 212 203 114 111 61 136 86 217 222 166 
142 202 103 113 96 79 133 190 216 194 81 99 216 134 174 
235 164 191 150 231 212 202 100 177 105 132 104 221 225 
202 113 98 84 220 166 225 198 159 88 240 65 163 
108 238 186 79 204 75 163 218 99 105 231 174 
217 107 113 61 209 229 116 216 100 103 123 
93 231 167 189 205 110 198 199 159 130 
148 127 133 190 66 111 172 102 210 
147 111 120 103 236 176 144 161 
147 204 192 238 138 61 168 
199 82 76 136 126 124 
68 168 186 62 100 
63 144 110 194 
179 174 230 
186 118 
170 
A
P 119 2
P 167 5
P 158 3
P 222 7
P 63 1
P 142 6
P 222 9
P 127 8
P 150 3
P 166 10
P 180 1
P 122 6
P 145 8
P 115 1
H
H
H
H
H
H"""
max=0
def sol(visited,v,time,day,score,trv):
    global max,G,a,h,p,d,result
    visited=visited[:]
    temp=trv[:]
    temp.append(v)
    if v==a:
        if max<score and day==d:
            max=score
            result=temp[:]
        return
    if v in p:
        time+=p[v][0]
        score+=p[v][1]
        visited[v]=True
        if time>540:
            return
    elif v in h:
        if day==d:
            return
        time=0
        day+=1
    for i in range(1,len(visited)):
        if not visited[i] and time+G[v][i]<=540:
            sol(visited,i,time+G[v][i],day,score,temp)
for tc in range(1,int(input())+1):
    i=input().split()
    v,d=int(i[0]),int(i[1])
    G=[[0]*(v+1) for _ in range(v+1)]
    visited=[False]*(v+1)
    result=[]
    max=0
    for i in range(1,v):
        inp=list(map(int,input().split()))
        for j in range(v-i):
            G[i][i+1+j]=G[i+1+j][i]=inp[j]
    a=0
    h=[]
    p={}
    for i in range(1,v+1):
        inp=input().split()
        if inp[0]=='A':
            a=i
        elif inp[0]=='P':
            p[i]=(int(inp[1]),int(inp[2]))
        else:
            h.append(i)
    for i in range(1,v+1):
        if not visited[i]:
            sol(visited,i,G[a][i],1,0,[])
    print(f"#{tc} {max} "+" ".join([str(i) for i in result]))