T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = [0] + list(map(int, input().split()))
    if stations[-1] != N:
        stations += [N]
        M += 1
    M += 1

    for i in range(M - 2):
        if stations[i + 2] - stations[i] < K + 1:
            stations[i + 1] = 0
    stations = [x for x in stations if x != 0]

    min_count = len(stations) - 1
    for i in range(len(stations) - 1):
        if stations[i + 1] - stations[i] > K or stations[0] > K or stations[-1] - stations[-2] > K:
            min_count = 0
    print(stations)
    print('#%d' % test_case, min_count)