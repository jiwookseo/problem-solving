inp = list(map(lambda x: int(x, 16), input()))  # 01D06079861D79F99F # 0F97A3
tt = 3
t = inp.pop(0)
while inp or tt != -1:
    out = 0
    for i in range(7):
        if tt == -1:
            if not inp:
                break
            t = inp.pop(0)
            tt = 3
        if t & (1 << tt):
            out += 1 << (6 - i) if inp else 1 << tt
        tt -= 1
    print(out)
