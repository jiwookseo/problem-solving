# 6781. 삼삼 트리플 게임 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgqpQV6r8gDFAW0&categoryId=AWgqpQV6r8gDFAW0&categoryType=CODE

def check(data):
    result=0
    for i in range(3):
        if len(data[i])-len(set(data[i]))>=2:
            for j in data[i]:
                if data[i].count(j)>=3:
                    result+=1
                    for _ in range(3):
                        data[i].remove(j)
        else:
            temp=sorted(data[i])
            while(len(temp)>=3):
                if temp[1]==temp[0]+1:
                    if temp[2]==temp[0]+2:
                        result+=1
                        for _ in range(3):
                            del temp[0]
                else:
                    del temp[0]
    return "Win" if result>=3 else "Continue"

for tc in range(1,int(input())+1):
    num=map(int,input())
    col=input()
    card=zip(num,col)
    data=[[],[],[]]
    for n,c in card:
        if c=='R':
            data[0].append(n)
        elif c=='G':
            data[1].append(n)
        else:
            data[2].append(n)
    print(f"#{tc} {check(data)}")

# Python 제출 불가능
# C코드로 작성해 제출하였다.
# 오답 41/50 맞음
"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int strt(int *list){
    int result=0, i;
    for (i=0; i<7; ++i){
        if(list[i]>=3 && list[i+1]>=3 && list[i+2]>=3){
            result+=3;
            list[i]-=3;
            list[i+1]-=3;
            list[i+2]-=3;
        }
        else if(list[i]>=2 && list[i+1]>=2 && list[i+2]>=2){
            result+=2;
            list[i]-=2;
            list[i+1]-=2;
            list[i+2]-=2;
        }
        else if(list[i]>=1 && list[i+1]>=1 && list[i+2]>=1){
            result+=1;
            list[i]-=1;
            list[i+1]-=1;
            list[i+2]-=1;
        }
    }
    return result;
}

int tri(int *list){
    int result=0, i;
    for (i=0; i<9; ++i){
        if (list[i]>=3){
                list[i]-=3;
                result+=1;
            }
    }
    return result;
}

int check(int *num, char *col){
    int strt(int*);
    int tri(int*);
    int result=0;
    int i;
    int r=0,g=0,b=0;
    int *rc,*gc,*bc;
    rc=(int*)malloc(sizeof(int)*10);
    gc=(int*)malloc(sizeof(int)*10);
    bc=(int*)malloc(sizeof(int)*10); 
    for (i=0; i<9; ++i){
        if (col[i]==82){
            rc[num[i]]+=1;
        }
        else if (col[i]==71){
            gc[num[i]]+=1;
        }
        else {
            bc[num[i]]+=1;
        }
    }
	result+=tri(rc);
    result+=tri(gc);
    result+=tri(bc);
    result+=strt(rc);
    result+=strt(gc);
    result+=strt(bc);
    if (result>=3){
        return 1;
    }
    else{
        return 0;
    }
}
        
int main(void)
{
	int test_case,T;
	int *num, i, temp;
    char *col;
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
        num=(int*)malloc(sizeof(int)*9);
		col=(char*)malloc(sizeof(char)*9);
        scanf("%d ", &temp);
        for (i=8; i>=0; --i){
            num[i]=temp%10;
            temp/=10;
        }
        for (i=0; i<9; ++i){
            scanf(" %c", &col[i]);
        }
        printf("#%d ",test_case);
        if (check(num,col)){
            printf("Win\n");
        }
        else{
            printf("Continue\n");
        }
	}
	return 0;
}
"""