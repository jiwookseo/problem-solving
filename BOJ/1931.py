import sys
n = int(input())
result = 0
meet = [tuple(map(int, m.split())) for m in sys.stdin.read().splitlines()]
meet.sort(key=(lambda x: (x[1], x[0])), reverse=True)
t = 0
while meet:
    while meet:
        s, e = meet.pop()
        if s >= t:
            t = e
            result += 1
            break
print(result)
