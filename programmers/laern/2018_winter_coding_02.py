# https://programmers.co.kr/learn/courses/30/lessons/49994


def solution(dirs):
    answer = set()
    r = c = 5
    for d in dirs:
        tr, tc = r, c
        if d == "U":
            tr += 1
        elif d == "D":
            tr -= 1
        elif d == "R":
            tc += 1
        else:
            tc -= 1
        if 0 <= tr < 11 and 0 <= tc < 11:
            a = r * 11 + c
            b = tr * 11 + tc
            answer.add(121 * a + b if a > b else 121 * b + a)
            r, c = tr, tc
    return len(answer)


print(solution("LULLLLLLU"))
