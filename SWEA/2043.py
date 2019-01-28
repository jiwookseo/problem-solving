# 2043. 서랍의 비밀번호 D1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QJ_8KAx8DFAUq&categoryId=AV5QJ_8KAx8DFAUq&categoryType=CODE

i=(input()).split(" ")
p,k=int(i[0]),int(i[1])
def func(p,k):
    return p-k+1 if p>=k else 0
print(func(p,k))