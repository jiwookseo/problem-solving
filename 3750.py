"""
3750. Digit sum

자연수 n에 대해 함수 f(n)은 n의 각 자릿수를 더한 값이다.

예를 들어 n = 588432라면, f(n) = 5 + 8 + 8 + 4 + 3 + 2 = 30인 것이다.

어떤 자연수 n이 주어질 때, n이 한 자리수가 될 때까지 n에 f(n)을 대입하는 것을 반복하면, 최종적으로 n이 어떤 값이 되는지 구하는 프로그램을 작성하라.

예를 들어 n = 588432라면 f(n) = 30이므로 n = 30이 되고, 이 때 f(n) = 3으로 최종적으로 n = 3이 되는 것이다.



[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 자연수 n(1 ≤ n ≤ 1018)이 주어진다.

[출력]

각 테스트 케이스마다 n이 한 자릿수가 될 때까지 f(n)을 취한 값을 출력한다.

입력 예시)
3
5
108
588432	


출력 예시)
#1 5
#2 9
#3 3

"""

"""
#include <stdio.h>
int main(void)
{
    int test_case;
    int T;
    unsigned long long temp ;
    scanf("%d", &T);    
    for (test_case = 1; test_case <= T; ++test_case){
        scanf("%llu", &temp);
        printf("#%d %d\n",test_case,(temp-1)%9+1);
    }
    return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
"""

input()
i=0

while(1):
    i+=1
    try:
        temp=int(input())%9
        print(f"#{i} {temp}") if temp!=0 else print(f"#{i} 9")
    except EOFError:
        break

# Python은 시간초과, C로 제출하여 Pass