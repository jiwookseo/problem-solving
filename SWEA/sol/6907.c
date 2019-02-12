// 6907. 단위 변환기 프로그램 D4
// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWh4GaY6EkEDFAXp&categoryId=AWh4GaY6EkEDFAXp&categoryType=CODE

#include <stdio.h>
#include <string.h>
int main(void)
{
	int test_case;
	int T,i,j,dot,temp,si,check;
    char s1[10], s2[51], n[1001];
	setbuf(stdout, NULL);
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf(" %s %s",n,s1);
        check=1;
        if (strcmp(s1,"yotta")==0)si=24;
        else if (strcmp(s1,"zetta")==0)si=21;
        else if (strcmp(s1,"exa")==0)si=18;
        else if (strcmp(s1,"peta")==0)si=15;
        else if (strcmp(s1,"tera")==0)si=12;
        else if (strcmp(s1,"giga")==0)si=9;
        else if (strcmp(s1,"mega")==0)si=6;
        else if (strcmp(s1,"kilo")==0)si=3;
        else if (strcmp(s1,"hecto")==0)si=2;
        else if (strcmp(s1,"deca")==0)si=1;
        else if (strcmp(s1,"deci")==0)si=-1;
        else if (strcmp(s1,"centi")==0)si=-2;
        else if (strcmp(s1,"milli")==0)si=-3;
        else if (strcmp(s1,"micro")==0)si=-6;
        else if (strcmp(s1,"nano")==0)si=-9;
        else if (strcmp(s1,"pico")==0)si=-12;
        else if (strcmp(s1,"femto")==0)si=-15;
        else if (strcmp(s1,"ato")==0)si=-18;
        else if (strcmp(s1,"zepto")==0)si=-21;
        else if (strcmp(s1,"yocto")==0)si=-24;
        else{
            si=0;
            check=0;
        }
        if (check==1){
            scanf(" %s",s2);
        }
        else{
            strcpy(s2,s1);
            s1[0]='\0';
        }
        if(n[0]==48){
            dot=0;
            for(i=0;i<strlen(n);++i){
                if (n[i]!=48 && n[i]!=46) break;
            }
            temp=1-i;
            n[0]=n[i];
            if (strlen(n)>i+1){
                n[1]=46;
                for(j=i+1;j<=strlen(n);++j){
                    n[j-i+1]=n[j];
                }
            }
            else n[1]='\0';
        }
        else{
            dot=strlen(n);
            check=0;
            for (i=0;i<strlen(n);++i){
                if (n[i]==46){
                    dot=i;
                    check=1;
                    break;
                }
            }
            temp=dot-1;
            for (i=dot;i>1;--i){
                n[i]=n[i-1];
            }
            n[1]=46;
            if (check==0){
                n[dot+1]='\0';
            }
        }
        printf("#%d %s * 10^%d %s\n",test_case,n,si+temp,s2);
	}
    return 0;
}