memo = [1, 1, 2, 6]


def f(n):
    if n >= len(memo):
        memo.append(n * f(n - 1))
    return memo[n]


N = int(input())
print(f(N))
