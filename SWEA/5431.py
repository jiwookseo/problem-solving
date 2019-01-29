# 5431. 민석이의 과제 체크하기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl3rWKDBYDFAXm&categoryId=AWVl3rWKDBYDFAXm&categoryType=CODE

for tc in range(1,int(input())+1):
    n,k=input().split()
    n,k=int(n),int(k)
    student=set([str(i) for i in range(1,n+1)])
    submit=set(input())-{' '}
    print(f"#{tc} "+ " ".join(student-submit))