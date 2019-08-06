class AccessLevel:
    def canAccess(self, rights, minPermission):
        return "".join(map(lambda x: "A" if int(x) >= minPermission else "D", rights))


AL = AccessLevel()
print(AL.canAccess(["0", "1", "2", "3", "4", "5"], 2))
