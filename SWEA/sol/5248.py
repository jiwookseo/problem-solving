# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
# ver 1. python set 이용한 방식
# for TC in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     djs = [{i} for i in range(1, n + 1)]
#     inp = list(map(int, input().split()))
#     for a, b in zip(inp[::2], inp[1::2]):
#         sa = sb = None
#         c1 = c2 = False
#         for i in djs:
#             if a in i:
#                 if b in i:
#                     break
#                 else:
#                     sa = i
#                     c1 = True
#             elif b in i:
#                 sb = i
#                 c2 = True
#             if c1 and c2:
#                 break
#         if sa:
#             sa.update(sb)
#             djs.remove(sb)
#     print("#{} {}".format(TC, len(djs)))

# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
# ver 2. tree 로 구현한 disjoint set 이용한 방식
class disjoint:
    def __init__(self, data):
        self.data = data
        self.par = self
        self.rank = 0

    def union(self, other):
        a, b = self.findset(), other.findset()
        if a.rank >= b.rank:
            b.par = a
            if a.rank == b.rank:
                a.rank += 1
        else:
            a.par = b

    def findset(self):
        if self != self.par:
            self.par = self.par.findset()
        return self.par


for TC in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    djs = [disjoint(i) for i in range(n + 1)]
    inp = list(map(int, input().split()))
    for a, b in zip(inp[::2], inp[1::2]):
        sa, sb = djs[a], djs[b]
        if sa.findset() != sb.findset():
            sa.union(sb)
    result = set()
    for i in range(1, n + 1):
        result.add(djs[i].findset())
    print("#{} {}".format(TC, len(result)))
