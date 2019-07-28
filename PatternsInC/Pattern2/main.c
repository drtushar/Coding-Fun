#include <stdio.h>
#include <stdlib.h>
/**
Enter a number : 5
A B C D E D C B A
A B C D   D C B A
A B C       C B A
A B           B A
A               A
Enter a number : 20
A B C D E F G H I J K L M N O P Q R S T S R Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P Q R S   S R Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P Q R       R Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P Q           Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P               P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O                   O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N                       N M L K J I H G F E D C B A
A B C D E F G H I J K L M                           M L K J I H G F E D C B A
A B C D E F G H I J K L                               L K J I H G F E D C B A
A B C D E F G H I J K                                   K J I H G F E D C B A
A B C D E F G H I J                                       J I H G F E D C B A
A B C D E F G H I                                           I H G F E D C B A
A B C D E F G H                                               H G F E D C B A
A B C D E F G                                                   G F E D C B A
A B C D E F                                                       F E D C B A
A B C D E                                                           E D C B A
A B C D                                                               D C B A
A B C                                                                   C B A
A B                                                                       B A
A                                                                           A

*/


int main()
{
    int input;
    printf("Enter a number : ");
    scanf("%d",&input);
    int i,j;
    char start = 'A';
    for(i=0; i<input*2-1; i++){
        if(i<input-1){
            printf("%c ",start);
            start += 1;
        }else{
            printf("%c ",start);
            start -= 1;
        }
    }
    printf("\n");
    int low,high;
    low = input-1;
    high = input-1;
    for(i=0; i <input-1; i++){
        start = 'A';
        for(j=0; j<input*2-1 ; j++){
            if( !(i+j>=low && i+j<=high) ){
                if(j<input-1){
                    printf("%c ",start);
                    start += 1;
                }else{
                    start -= 1;
                    printf("%c ",start);
                }
            }else{
                printf("  ");
            }
        }
        printf("\n");
        high += 2;
    }


    return 0;
}
