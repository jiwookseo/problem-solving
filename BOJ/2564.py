w, h = map(int, input().split())
n = int(input())
s = [map(int, input().split()) for _ in range(n)]
cd, cl = map(int, input().split())  # 1234 북남서동
check = cd <= 2
result = 0
for d, l in s:
    check2 = d <= 2
    if check2 == check:  # 맞은 편이나 같은 편
        if cd == d:  # 같은 편
            result += abs(cl - l)
        elif check:  # 맞은 편 중에

            result += h
            result += cl + l if cl + l < w else 2 * w - cl - l  # 맞은 편 중에 이득인 코너로
        else:
            result += w
            result += cl + l if cl + l < h else 2 * h - cl - l  # 맞은 편 중에 이득인 코너로
    else:
        if check:  # 동근이가 남북에 있을 때
            result += cl if d == 3 else w - cl  # 가로 방향 : 상점 위치 구분
            result += l if cd == 1 else h - l  # 세로 방향 : 동근이 위치 구분
        else:  # 동근이가 동서에 있을 때
            result += cl if d == 1 else h - cl  # 세로 방향 : 상점 위치 구분
            result += l if cd == 3 else w - l  # 가로 방향 : 동근이 위치 구분
print(result)
