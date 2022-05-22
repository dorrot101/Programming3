typedef enum{
    Term, Insert, Append, InsertNth, DeleteNth, Delete, Print, Clear
}Menu;

typedef struct __node{
    int no;
    char name[10];
    struct __node *next;
}Node;

void SetNode(Node *x, int no, char *name, Node *next);
void InsertNode(Node **top, int no, char *name);
void AppendNode(Node **top, int no, char *name);
void DeleteNode(Node **top);
void ClearList(Node **top);
void PrintList(Node **top);
void InitList(Node **top);
void TermList(Node **top);
void InsertNodeNth(Node **top, int n, int no, char *name);
void DeleteNodeNth(Node **top, int n);
Node Read(char *Message);
Node *AllocNode(void);
Menu SelectMenu(void);