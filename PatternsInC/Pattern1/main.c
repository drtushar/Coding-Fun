#include <stdio.h>
#include <stdlib.h>

/**
Enter a number : 4
      1
    2   3
  4   5   6
7   8   9   10
*/


int main()
{
    int input;
    printf("Enter a number : ");
    scanf("%d",&input);
    int i,j,k,l,flag;
    l = 1;
    for(i = 0; i<input ; i = i+1){
        k = input-1;
        flag = 0;
        for(j = 0 ; j<(input*2)-1 ; j = j+1){
            if(i+j==k){
                printf("%d ",l);
                l++;
                k += 2;
                if(flag==i)
                    break;
                flag += 1;
            }else{
                printf("  ");
            }
        }
        printf("\n");
    }
    return 0;
}
