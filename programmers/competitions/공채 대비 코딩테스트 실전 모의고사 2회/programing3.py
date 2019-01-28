def solution(board, nums):
    n=len(board)
    raw={}
    r=[n]*n
    c=[n]*n
    x1=n
    x2=n
    count=0
    for i in range(n):
        for j in range(n):
            raw[board[i][j]]=(i,j)
    for num in nums:
        rt,ct=raw[num][0],raw[num][1]
        r[rt]-=1
        c[ct]-=1
        if rt==ct:
            x1-=1
        if rt+ct==n-1:
            x2-=1
    count+=r.count(0)
    count+=c.count(0)
    count+=(x1==0)
    count+=(x2==0)
    return count

"""
채점 결과
정확성: 70.0
효율성: 30.0
합계: 100.0 / 100.0
"""