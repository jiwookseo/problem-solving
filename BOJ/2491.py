n = int(input())
num = list(map(int, input().split()))
result = 0
i = 0
while i + result < n and i != n-1:
    j = i + 1
    check = True
    while num[j-1] <= num[j]:
        j += 1
        if j == n:
            break
    if result < j - i:
        result = j - i
    i = j
i = 0
while i + result < n and i != n-1:
    j = i + 1
    check = True
    while num[j-1] >= num[j]:
        j += 1
        if j == n:
            break
    if result < j - i:
        result = j - i
    i = j
print(max(result, 1))
