// 6781. 삼삼 트리플 게임 D3
// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgqpQV6r8gDFAW0&categoryId=AWgqpQV6r8gDFAW0&categoryType=CODE

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