# https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    gd = dict()
    for i in range(len(plays)):
        g, p = genres[i], plays[i]
        if g in gd:
            gd[g][0].append((p, i))
            gd[g][1] += p
        else:
            gd[g] = [[(p, i)], p]
    result = list(gd.values())
    result.sort(key=(lambda x: x[1]), reverse=True)
    answer = []
    for g in result:
        g[0].sort(key=(lambda x: (x[0], -x[1])), reverse=True)
        for v, i in g[0][:2]:
            answer.append(i)
    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
