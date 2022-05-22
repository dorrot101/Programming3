#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kadai3.h"

void SetNode(Node *node, int no, char *name, Node *prev, Node *next){
    node->no = no;
    node->prev = prev;
    node->next = next;
    strcpy(node->name,name);
    if(prev != NULL){
        prev->next = node;
    }
    if(next != NULL){
        next->prev = node;
    }
}
void InsertNode(List *list, int no, char *name){
    Node* ptr = list->top;
    list->top = AllocNode();
    SetNode(list->top,no,name,NULL,ptr);
    if(ptr == NULL) list->bottom = list->top;
}
void AppendNode(List *list, int no, char *name){
    Node *ptr = list->bottom;
    list->bottom = AllocNode();
    SetNode(list->bottom,no,name,ptr,NULL);
    if(ptr == NULL) list->top = list->bottom;
}
void DeleteNode(Node *node){
    if(node != NULL){
        if(node->prev != NULL)   node->prev->next = node->next;
        if(node->next != NULL)   node->next->prev = node->prev;
        free(node);
    }
}
void DeleteBottomNode(List *list){
    Node* ptr = list->bottom->prev;
    DeleteNode(list->bottom);
    list->bottom = ptr;
}
void InsertNodeNth(List *list, int n, int no, char *name){
    if(n == 1) {
        InsertNode(list,no,name);
        return;
    }
    Node* ptr = list->top;
    int cnt = n-1;
    while(cnt > 0 && ptr->next != NULL){
        ptr = ptr->next;
        cnt--;
    }
    if(cnt > 0) {
        AppendNode(list,no,name); 
    }
    else{
        Node* ist = AllocNode();
        SetNode(ist,no,name,ptr->prev,ptr);  
    }
  
}
void DeleteNodeBackNth(List *list, int n){
    if(n == 1) {
        DeleteBottomNode(list);
        return;
    }
    Node* ptr = list->bottom;
    int cnt = n-1;
    while(cnt > 0 && ptr->prev != NULL){
        ptr = ptr->prev;
        cnt--;
    }    
    if(cnt > 0){
        Node* nptr = ptr->next;
        DeleteNode(ptr);
        list->top = nptr;
    }
    else DeleteNode(ptr);
}
void InitList(List *list){
    list->top = NULL;
    list->bottom = NULL;
}
void TermList(List *list){
    Node* ptr = list->top;
    while(ptr != NULL){
        Node* tmp = ptr->next;
        free(ptr);
        ptr = tmp;
    }
    free(list);
}
void PrintList(List *list){
    Node* ptr = list->top;
    puts("【一覧表】");
    while(ptr != NULL){
        printf("%5d %-10.10s\n", ptr->no, ptr->name);
        ptr = ptr->next;
    }
} 
Node *AllocNode(void){
    return calloc(1,sizeof(Node));
}