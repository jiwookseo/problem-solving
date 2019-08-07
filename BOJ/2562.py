ind = 0
maximum = 0
for i in range(1, 10):
    temp = int(input())
    if maximum < temp:
        ind = i
        maximum = temp
print(f"{maximum}\n{ind}")
