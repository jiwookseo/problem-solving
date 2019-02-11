// 6808. 규영이와 인영이의 카드게임 D3
// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0&categoryId=AWgv9va6HnkDFAW0&categoryType=CODE

// 오답 : 시간초과 91/100

#include <stdio.h>
#include <stdlib.h> 
void versus(int *a, int *b, int* win, int* lose){
    int i,s=0;
    for(i=0;i<10;++i){
        if(a[i]>b[i]){
            s+=a[i]+b[i];
        }
        else{
            s-=a[i]+b[i];
        }
        if(s>85||s<-85){
            break;
        }
    }
    if (s>0){
        *win+=1;
    }
    else if (s<0){
        *lose+=1;
    }
}
void swap(int *a, int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
}

void permute(int *a,int *b, int l, int r, int *win, int *lose){
    int i,temp;
    if(l==r){
        versus(a,b,win,lose);
    }
    else{
        for(i=l;i<=r;i++){
            swap((b+l),(b+i));
            permute(a, b, l+1, r, win, lose);
            swap((b+l),(b+i));
        }
    }
}

int main(){
    int T,tc,i,j,index,check;
    int a[9],b[9];
    int win, lose;
    scanf("%d",&T);
    for(tc=1;tc<=T;++tc){
        win=0;
        lose=0;
        for(i=0;i<9;++i){
            scanf("%d", &a[i]);
        }
        index=0;
        for(i=1;i<=18;++i){
            check=1;
            for(j=0;j<9;++j){
                if(i==a[j]){
                    check=0;
                }
            }
            if(check==1){
                b[index]=i;
                index++;
            }
        }
        permute(a,b,0,8,&win,&lose);
        printf("#%d %d %d\n",tc,win,lose);
    }
    return 0;
}