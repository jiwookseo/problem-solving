def permutate(a, t, s):
    global r
    if len(a) == n + 1:
        r.append("".join([str(i) for i in a]))
        return
    for i in t:
        if s[0] == '>':
            if a[-1] > i:
                permutate(a+[i], t-{i}, s[1:])
        else:
            if a[-1] < i:
                permutate(a+[i], t-{i}, s[1:])


r = []
n = int(input())
s = input().split()
t = set(range(10))
for i in t:
    permutate([i], t-{i}, s)
print(max(r))
print(min(r))
