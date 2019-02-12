# 6907. 단위 변환기 프로그램 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWh4GaY6EkEDFAXp&categoryId=AWh4GaY6EkEDFAXp&categoryType=CODE
# python 제출이 없음....
# example cass 는 pass했으나 test case는 python 미지원으로 불가
# C code로 porting 해 pass ( 6907.c )

si={"yotta" : 24,"zetta" : 21,"exa" : 18,"peta" : 15,"tera" : 12,"giga" : 9,"mega" : 6,"kilo" : 3,"hecto" : 2,"deca" : 1,"deci" : -1,\
"centi" : -2,"milli" : -3,"micro" : -6,"nano" : -9,"pico" : -12,"femto" : -15,"ato" : -18,"zepto" : -21,"yocto" : -24,"none": 0 }
for tc in range(1,int(input())+1):
    i=input().split()
    n=i[0]
    if len(i)==3:
        s1,s2=i[1],i[2]
    else:
        s1="none"
        s2=i[1]
    if float(n)>=1 and float(n)<10:
        temp=0
        pass
    elif n[0]=='0':
        dot=0
        for i in range(len(n)):
            if n[i]!="0" and n[i]!=".":
                break
        temp=1-i
        n=n[i:]
    else :
        dot=len(n)
        for i in range(len(n)):
            if n[i]==".":
                dot=i
                break
        n=n.replace(".","")
        n=n[0]+"."+n[1:]
        temp=dot-1
    print(f"#{tc} {n} * 10^{si[s1]+temp} {s2}")