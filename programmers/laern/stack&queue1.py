# https://programmers.co.kr/learn/courses/30/lessons/42585
def solution(arrangement):
    li = list(arrangement.replace("()", "0"))
    answer = 0
    count = 0
    for i in li:
        if i == '0':
            answer += count
        elif i == '(':
            count += 1
            answer += 1
        else:
            count -= 1
    return answer
