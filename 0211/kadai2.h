#define NAMELEN 10

typedef struct __node{
    int no;
    char name[NAMELEN];
    struct __node *next;
}Node;

typedef struct{
    int num;
    Node *front;
    Node *rear;
}Queue;

void QueueFree(Queue *q);
void PrintQueue(Queue *q);
void SetNode(Node *x, int no, char *name, Node *next);
int QueueIsEmpty(const Queue *q);
int QueueInit(Queue *q);
int QueueEnque(Queue *q, Node *x);
int QueueNo(const Queue *q);
Node *AllocNode(void);
Node *QueueDeque(Queue *q);