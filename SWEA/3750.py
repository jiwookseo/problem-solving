# 3750. Digit sum D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPiSYKAD0DFAUn&categoryId=AWHPiSYKAD0DFAUn&categoryType=CODE

input()
i=0

while(1):
    i+=1
    try:
        temp=int(input())%9
        print(f"#{i} {temp}") if temp!=0 else print(f"#{i} 9")
    except EOFError:
        break

# Python은 시간초과, C로 제출하여 Pass