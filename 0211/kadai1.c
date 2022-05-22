#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kadai1.h"

void SetNode(Node *x, int no, char *name, Node *next){
    x->no = no;
    x->next = next;
    strcpy(x->name, name);
}
void InsertNode(Node **top, int no, char *name){
    Node *ptr = *top;
    *top = AllocNode();
    SetNode(*top, no, name, ptr);
}
void AppendNode(Node **top, int no, char *name){
    if(*top == NULL){
        InsertNode(top, no, name);
    }
    else{
        Node *ptr = *top;
        while(ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = AllocNode();
        SetNode(ptr->next, no, name, NULL);
    }
}
void DeleteNode(Node **top){
    if(*top != NULL){
        Node *ptr = (*top)->next;
        free(*top);
        *top = ptr;
    }
}
void ClearList(Node **top){
    while(*top != NULL){
        DeleteNode(top);
    }
}
void PrintList(Node **top){
    Node *ptr = *top;
    puts("【一覧表】");
    while(ptr != NULL){
        printf("%5d %-10.10s\n", ptr->no, ptr->name);
        ptr = ptr->next;
    }
}
void InitList(Node **top){
    *top = NULL;
}
void TermList(Node **top){
    ClearList(top);
}
void InsertNodeNth(Node **top, int n, int no, char *name){
    if(*top == NULL || n == 1){
        InsertNode(top,no,name);
        return;
    }

    int cnt = n-2;
    Node *target = *top;
    while(cnt > 0 && target->next != NULL){
        cnt--; 
        target = target->next;
    }
    if(cnt > 0){
        AppendNode(top,no,name);
    }
    else{
        Node* tmp = target->next;
        Node* ptr = AllocNode();
        target->next = ptr;
        SetNode(ptr, no, name, tmp);
    }
}
void DeleteNodeNth(Node **top, int n){
    int cnt = n-2;
    Node *target = *top;
    if(target == NULL) return;
    if(target->next == NULL) {
        DeleteNode(top);
        return;
    }
    while(cnt > 0 && target->next->next != NULL){
        cnt--; 
        target = target->next;
    }
    Node* tmp = target->next;
    DeleteNode(&tmp);
    target->next = tmp;

}
Node Read(char *Message){
    Node temp;
    printf("%sするデータを入力してください。\n", Message);
    printf("番号:"); scanf("%d", &temp.no);
    printf("名前:"); scanf("%s", temp.name);

    return temp;
}
Node* AllocNode(void){
    return (calloc(1, sizeof(Node)));
}
Menu SelectMenu(void){
    int ch;
    do{
        puts("(1)先頭にノードを挿入\t(2)末尾にノードを追加");
        puts("(3)ｎ番目にノードを挿入\t(4)n番目の要素を削除");
        puts("(5)先頭のノードを削除\t(6)全てのノードを表示");
        puts("(7)全てのノードを削除\t(0)処理終了");
        scanf("%d", &ch);
    }while(ch<Term || ch>Clear);
    return ((Menu)ch);
}