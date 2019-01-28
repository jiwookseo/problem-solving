i=input().split(" ")
A=int(i[0])
B=int(i[1])
C=int(i[2])
print((A+B)%C)
print((A%C+B%C)%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
#첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.