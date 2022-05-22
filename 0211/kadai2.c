#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kadai2.h"

void QueueFree(Queue *q){
    Node *ptr = q->front;
    while(ptr != NULL){   
        Node* temp = ptr->next;
        free(ptr);
        ptr = temp;
    }
    free(q);
}

void PrintQueue(Queue *q){
    puts("【一覧表】");
    Node *ptr = q->front;
    if(ptr == NULL){
        puts("\t...");
        return;
    }
    while(ptr != NULL){
        printf("%5d %-10.10s\n", ptr->no, ptr->name);
        ptr = ptr->next;
    }
}

void SetNode(Node *x, int no, char *name, Node *next){
    x->no = no;
    x->next = next;
    strcpy(x->name, name);
}

int QueueIsEmpty(const Queue *q){
    if(q->num == 0) return 1;
    else return 0;
}

int QueueInit(Queue *q){
    q->front = NULL;
    q->rear = NULL;
    q->num = 0;
    puts("\nQueue is intialized!\n");
    return 0;
}
/*
キューにノードを入れる。
キューが空いていれば最初のノードを表すFrontポインターと
最後のノードを表すRearポインターが同時に同じノードを指すように指定する。
*/
int QueueEnque(Queue *q, Node *x){
        if(QueueIsEmpty(q) == 1){
            q->front = x;
            q->rear = x;
        }
        else{
            Node *ptr = q->rear;
            ptr->next = x;
            x->next = NULL;
            q->rear = x;
        }
        q->num++;
}

int QueueNo(const Queue *q){
    return q->num;
}

Node *AllocNode(void){
    return (calloc(1, sizeof(Node)));
}

//キューから最初のノードを取り出す。
//最初のノードがなければキューが空いている状態を出力してＮＵＬＬを返還する。
Node *QueueDeque(Queue *q){
    Node *ptr = q->front;
    if(ptr != NULL){
        Node *result = AllocNode();
        SetNode(result,ptr->no,ptr->name,ptr->next);
        Node* temp = ptr->next;
        free(q->front);
        q->front = temp;
        q->num--;
        return result;
    }
    else {
        puts("Queue is Empty!!");
        return NULL;
    }
}