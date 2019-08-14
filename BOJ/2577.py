count = {str(i): 0 for i in range(10)}
for i in str(int(input()) * int(input()) * int(input())):
    count[i] += 1
for i in range(10):
    print(count[str(i)])
