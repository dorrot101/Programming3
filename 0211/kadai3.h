#define NAMELEN 10

typedef struct __node{
    int no;
    char name[NAMELEN];
    struct __node *prev;
    struct __node *next;
}Node;

typedef struct{
    Node *top;
    Node *bottom;
}List;

void AppendNode(List *list, int no, char *name);
void DeleteBottomNode(List *list);
void InsertNodeNth(List *list, int n, int no, char *name);
void DeleteNodeBackNth(List *list, int n);
void SetNode(Node *node, int no, char *name, Node *prev, Node *next);
void InsertNode(List *list, int no, char *name);
void DeleteNode(Node *node);
void InitList(List *list);
void TermList(List *list);
void PrintList(List *list); 
Node *AllocNode(void);