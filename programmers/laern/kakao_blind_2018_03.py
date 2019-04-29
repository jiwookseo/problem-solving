# https://programmers.co.kr/learn/courses/30/lessons/42890


def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    able = [False] * col
    for j in range(col):
        temp = set()
        for i in range(row):
            if relation[i][j] not in temp:
                temp.add(relation[i][j])
            else:
                able[j] = True
                break
        if not able[j]:
            answer += 1
    ns = [i for i in range(col) if able[i]]
    key = []
    for a in range(1 << len(ns)):
        select = []
        for b in range(len(ns)):
            if a & (1 << b):
                select.append(ns[b])
        if len(select) > 1:
            temp = set()
            for i in range(row):
                data = " ".join([relation[i][j] for j in select])
                if data not in temp:
                    temp.add(data)
                else:
                    break
            if len(temp) == row:
                key.append(set(select))
    for a in key:
        check = True
        for b in key:
            if a != b and a.issuperset(b):
                check = False
                break
        if check:
            answer += 1
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
