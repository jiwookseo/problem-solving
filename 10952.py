import sys
n=int(input())
for _ in range(n):
    temp=sys.stdin.readline().rstrip().split(" ")
    print(int(temp[0])+int(temp[1]))