# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 D2

def draw(array,sr,sc,er,ec,color):
    for r in range(sr,er+1):
        for c in range(sc,ec+1):
            array[r][c]=color if array[r][c]==color or array[r][c]==0 else 3
def countPurple(array):
    count=0
    for r in array:
        for c in r:
            count+=1 if c==3 else 0
    return count
for tc in range(1,int(input())+1):
    grid=[[0]*10 for _ in range(10)]
    for _ in range(int(input())):
        draw(grid,*map(int,input().split()))
    print(f"#{tc} {countPurple(grid)}")