# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bw = 0
    while truck_weights:
        tw = truck_weights[0]
        bw -= bridge.pop()
        if bw + tw <= weight:
            bw += tw
            del truck_weights[0]
            bridge = [tw] + bridge
            answer += 1
        else:
            answer += 1
            while bridge[-1] == 0:
                answer += 1
                del bridge[-1]
            bridge = [0] * (bridge_length - len(bridge)) + bridge
    for i in range(bridge_length):
        if bridge[i] != 0:
            answer += bridge_length - i
            return answer


print(solution(2, 10, [7, 4, 5, 6]))
