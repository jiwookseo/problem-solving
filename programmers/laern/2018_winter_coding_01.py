# https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    for tree in skill_trees:
        i = 0
        check = True
        for j in range(len(tree)):
            if tree[j] in skill:
                if skill[i] == tree[j]:
                    i += 1
                else:
                    check = False
                    break
        if check:
            answer += 1
    return answer
