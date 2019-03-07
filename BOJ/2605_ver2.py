n = int(input())
num = list(map(int, input().split()))
result = []
for i in range(n):
    result.insert(num[i], i + 1)
print(" ".join([str(i) for i in result[::-1]]))