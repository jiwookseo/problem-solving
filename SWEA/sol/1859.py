for t in range(1,int(input())+1):
    n,s,=int(input()),list(map(int, input().split()));m,r=s[-1],0
    for i in range(n-2,-1,-1):
        if s[i]>m:m =s[i]
        else:r+=m-s[i]
    print(f"#{t} {r}")
