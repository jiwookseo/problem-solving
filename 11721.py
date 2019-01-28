l=input()
for i in range(len(l)):
    print(l[i],end="") if (i+1)%10 else print(l[i])