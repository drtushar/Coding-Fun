#include <stdio.h>
#include <stdlib.h>
int a = 0,b = 1;
void fibiterative(int n){
    int c;
    printf("%d",a);
    while(n != 1){
        c = a + b;
        a = b;
        b = c;
        printf(" %d",c);
        n--;
    }
}

void recfib(int n){
    int c;
    if(n != 0){
        c = a+b;
        a = b;
        b = c;
        printf(" %d",c);
        recfib(n-1);
    }
}

int main()
{
    recfib(10);
    return 0;
}
