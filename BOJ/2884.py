h, m = map(int, input().split())
print(f"{h if m - 45 >= 0 else (h - 1) % 24} {(m - 45) % 60}")
