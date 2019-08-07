for TC in range(int(input())):
    inp = input().split()
    N = int(inp[0])
    nums = list(map(int, inp[1:]))
    average = sum(nums) / N
    count = 0
    for num in nums:
        if num > average:
            count += 1
    print("%.3f" % round((count / N) * 100, 3) + "%")
