#include <stdio.h>
#include "kadai2.c"

int main(void){

    Queue* Qptr = (Queue*)calloc(1,sizeof(Queue));;
    QueueInit(Qptr);
    
    Node* dd = AllocNode();
    Node* aa = AllocNode();
    SetNode(dd, 1, "hi", NULL);
    SetNode(aa, 2, "gg", NULL);
    QueueEnque(Qptr, dd);
    QueueEnque(Qptr, aa);
    PrintQueue(Qptr);
    
    Node* pp = QueueDeque(Qptr);
    PrintQueue(Qptr);

    QueueEnque(Qptr, pp);
    PrintQueue(Qptr); 
    QueueDeque(Qptr);
    PrintQueue(Qptr); 
    QueueDeque(Qptr);
    PrintQueue(Qptr); 
    QueueDeque(Qptr); 
    PrintQueue(Qptr);   
    QueueFree(Qptr);

    return 0;
}