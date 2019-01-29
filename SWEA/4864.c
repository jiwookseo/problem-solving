// 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
// Brute Force

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int str1_max=100;
int str2_max=1000;
int main(){
    int tc;
    int i, j, k;
    char *a, *b;
    int check=0;
    scanf("%d",&tc);
    for(i=1;i<=tc;++i){
        a=(char*)malloc(sizeof(char)*str1_max);
        b=(char*)malloc(sizeof(char)*str2_max);
        scanf("%s",a);
        scanf("%s",b);
        for(j=0;j<=(strlen(b)-strlen(a));++j){
            for(k=0;k<strlen(a);++k){
                if(a[k]==b[j+k]){
                    check=1;
                }
                else{
                    check=0;
                    break;
                }
            }
            if(check==1){
                printf("#%d 1\n",i);
                break;
            }
        }
        if(check==0){
            printf("#%d 0\n",i);
        }
    }
    return 1;
}