# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []
    temp = []
    id_dict = dict()
    for data in record:
        data = data.split()
        if data[0] == "Leave":
            temp.append((data[1], 1))
        else:
            id_dict[data[1]] = data[2]
            if data[0] == "Enter":
                temp.append((data[1], 0))
    for data in temp:
        ment = "님이 나갔습니다." if data[1] else "님이 들어왔습니다."
        answer.append(id_dict[data[0]] + ment)
    return answer
