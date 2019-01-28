def solution(arrA, arrB):
    if set(arrA)-set(arrB)!=set():
        return False
    else:
        for _ in range(len(arrA)):
            arrA.insert(0,arrA[-1])
            del arrA[-1]
            if arrA==arrB:
                return True
    return False

"""
채점 결과
정확성: 100.0
효율성: 0.0
합계: 100.0 / 100.0
"""