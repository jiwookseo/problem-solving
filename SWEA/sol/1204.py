# dictionary 이용한 방법
# 메모리 48,048 kb
# 실행시간 144 ms
# 의외로 메모리가 리스트보다 적게 든다
for tc in range(1, int(input()) + 1):
    input()
    d = {str(i): 0 for i in range(101)}
    for i in input().split():
        d[i] += 1
    max = 0
    result = '0'
    for i, v in d.items():
        if max <= v:
            result, max = i, v
    print("#{} {}".format(tc, result))

# # list 이용한 방법
# # 50,408 kb 메모리
# # 140 ms 실행시간
# # 의외로 메모리가 딕셔너리보다 많이 든다
# for tc in range(1, int(input()) + 1):
#     input()
#     d = [0]*101
#     for i in map(int,input().split()):
#         d[i] += 1
#     max = 0
#     result = 0
#     for i in range(101):
#         if max <= d[i]:
#             result, max = i, d[i]
#     print("#{} {}".format(tc, result))
