n, x = map(int, input().split())
print(*[num for num in map(int, input().split()) if num < x])
