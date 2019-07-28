#include <stdio.h>
#include <stdlib.h>


/**

Enter A number : 5
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

Enter A number : 7
            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   6   1   0   5   1
1   7   7   1   5   6   1

*/

int value = 1;
int getnumber(int n,int r){
    char a[100];
    itoa(value,a,10);
    if(n == r)
        value *= 11;
    int re = a[r] - 48;
    return re;
}

int main()
{
    int i,j,input;
    printf("Enter A number : ");
    scanf("%d",&input);
    int k,flag;
    for(i=0;i<input; i++){
        k = input-1;
        flag = 0;
        for(j=0;j<input*2-1; j++){
            if(i+j==k){
                int ans = getnumber(i,flag);
                printf("%d ",ans);
                if(flag==i)
                    break;
                k += 2;
                flag += 1;
            }else{
                printf("  ");
            }
        }
        printf("\n");
    }
    return 0;
}
