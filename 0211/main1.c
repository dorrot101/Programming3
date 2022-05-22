#include "kadai1.c"

int main(void){
    Menu menu;
    Node *list;
    int tmp;

    InitList(&list);
    do{
        Node x;
        switch(menu = SelectMenu()){
            case Insert: x = Read("挿入");
                InsertNode(&list,x.no,x.name); break;
            case Append: x = Read("追加");
                AppendNode(&list,x.no,x.name); break;
            case InsertNth: x = Read("挿入");
                printf("何番目:"); scanf("%d",&tmp); InsertNodeNth(&list,tmp,x.no,x.name); break;
            case DeleteNth: 
                printf("何番目:"); scanf("%d",&tmp); DeleteNodeNth(&list, tmp); break;
            case Delete: DeleteNodeNth(&list,3); break;
            case Print: PrintList(&list); break;
            case Clear: ClearList(&list); break;
        }
    }while(menu != Term);
    TermList(&list);
    return 0;
}