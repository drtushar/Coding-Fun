#include <iostream>
#include<stdio.h>
#include<stdlib.h>
///Standard Template Library Practice.
using namespace std;
///STL is now part standard c++ library and are defined in namespace std.

/**
    STL has 3 main components
    1. Containers : An object that actually stores data. A way data is organized in memory.
    2. Algorithms : It is a procedure that is used to process the data contained in the containers.
    3. Iterators  : It is an object(like pointer) that points to an element in a container.
*/
/**
    Containers : STL has 10 containers. {vector,list,deque,set,map,multiset,multimap,stack,queue,priority_queue}
    1. Sequence Containers : Stores elements in linear fashion. Eg : vector,list,deque.
                randomAccess    insertionInMiddle   insertionAtEnd
    Vector      FAST            SLOW                Fast at END(RandomAccess)
    List        SLOW            FAST                Fast at FRONT(Bidirectional)
    Deque       FAST            SLOW                FAST at BOTH ENDS.(RandomAccess)

    2. Associative Containers : Designed to support direct access to elements using the keys.
    EG : set,map,multiset,multimap
    Associative Containers use data structure as trees so they have quick searching, deletion and insertion
    but fails for random access and sorting.

*/
int fun(int arr[2]);
int fun1(int arr[]);
int f(int* a, int b){
    b = b - 1;
    if(b ==0 ) return 1;
    *a = *a + 1;
    return f(a,b)*(*a);
}
int main()
{
    //cout<<sizeof(int);
    int a = 3;
    int b = 3;
    return f(&a,b);
}
