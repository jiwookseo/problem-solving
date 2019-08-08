class Counter:
    counter = 0

    def f(self, num):
        if num == 0:
            self.counter += 1
        if num > 3:
            self.f(num - 3)
            self.f(num - 2)
            self.f(num - 1)
        elif num == 3:
            self.f(num - 2)
            self.f(num - 1)
            self.counter += 1
        elif num == 2:
            self.f(num - 1)
            self.counter += 1
        else:
            self.counter += 1


for TC in range(int(input())):
    c = Counter()
    c.f(int(input()))
    print(c.counter)
