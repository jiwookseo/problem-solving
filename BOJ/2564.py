w, h = tuple(map(int, input().split()))
n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
cd, cl = tuple(map(int, input().split())) # 1234 북남서동
check = cd <= 2
result = 0
for d, l in s:
    check2 = d <= 2
    if check2 == check : # 맞은 편이나 같은 편
        if cd == d: # 같은 편
            result += abs(cl - l)
        elif check:
            if cl + l < w: # 맞은 편 중에 이득인 코너로
                result += h + cl + l
            else:
                result += h + 2 * w - cl - l
        else:
            if cl + l < h: # 맞은 편 중에 이득인 코너로
                result += w + cl + l
            else:
                result += w + 2 * h - cl - l
    else:
        if check: # 동근이가 남북에 있을 때
            if d == 3:
                if cd == 1:
                    result += cl + l
                else:
                    result += cl + h - l
            else:
                if cd == 1:
                    result += w - cl + l
                else:
                    result += w - cl + h - l
        else: # 동근이가 동서에 있을 때
            if d == 1:
                result += cl + l
            else:
                result += w - cl + l
print(result)
