nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
N = int(input())
count = 1
temp = [None] * 10
while N != count:
    temp[0] = nums[1]
    temp[9] = nums[8]
    for i in range(1, 9):
        temp[i] = nums[i - 1] + nums[i + 1]
    nums = temp[:]
    count += 1
print(sum(nums) % 1000000000)
