n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b - 1] = c
    else:
        sum = 0
        for i in range(b - 1, c):
            sum += nums[i]
        print(sum)
