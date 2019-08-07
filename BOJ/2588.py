a = int(input())
b = int(input())
r1 = a * (b % 10)
b //= 10
r2 = a * (b % 10)
b //= 10
r3 = a * (b % 10)
r4 = r1 + r2 * 10 + r3 * 100
print(f"{r1}\n{r2}\n{r3}\n{r4}")
