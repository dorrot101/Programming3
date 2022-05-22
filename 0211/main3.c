#include "kadai3.c"

int main(void){

    List *list = (List*)calloc(1,sizeof(List));

    InitList(list);
    AppendNode(list,3,"cc");
    AppendNode(list,1,"aa");
    InsertNode(list,2,"bb");
    InsertNodeNth(list,3,4,"dd");
    InsertNodeNth(list,1,5,"ee");
    PrintList(list);
    DeleteBottomNode(list);
    PrintList(list);
    DeleteNodeBackNth(list,1);
    PrintList(list);
    DeleteNodeBackNth(list,6);
    PrintList(list);
    TermList(list);


    return 0;
}