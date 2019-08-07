y = int(input())
if y % 4:
    print(0)
elif not y % 400:
    print(1)
elif not y % 100:
    print(0)
else:
    print(1)
