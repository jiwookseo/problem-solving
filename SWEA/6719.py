# 6719. 성수의 프로그래밍 강좌 시청 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWd7sgDatsMDFAUh&categoryId=AWd7sgDatsMDFAUh&categoryType=CODE

for tc in range(1,int(input())+1):
    inp=input().split()
    n,k=int(inp[0]),int(inp[1])
    inp=list(map(int,input().split()))
    lecture=sorted(inp)[-k:]
    sudoon=0
    for i in lecture:
        sudoon=(sudoon+i)/2
    print(f"#{tc} {sudoon}")

# Python 제출 불가능
# C코드로 작성해 제출하였다.
"""
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int test_case, T;
    int n, k, i, j, temp, max, index;
    float sudoon;
    int *input, *lecture;
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for (test_case = 1; test_case <= T; ++test_case){
        scanf("%d %d", &n, &k);
        input=(int *)malloc(sizeof(int) * n);
        lecture=(int *)malloc(sizeof(int) * k);
        for (i=0; i<n; ++i){
            scanf("%d", &input[i]);
        }
        for (i=k-1; i>=0; --i){
            max=input[0];
            index=0;
            for (j=0; j<n; ++j){
                if(max<input[j]){
                    max=input[j];
                    index=j;
                }
            }
            lecture[i]=max;
            input[index]=0;
        }
        sudoon=0;
        for (i=0; i<k; ++i){
            sudoon+=lecture[i];
            sudoon/=2.;
        }
        printf("#%d %f\n", test_case, sudoon);
    }
    return 0;
}
"""