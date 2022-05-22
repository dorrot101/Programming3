// Header file -> Yacht.h
#ifndef __YACHT_H__
#define __YACHT_H__

typedef struct YachtBoard{
    int score; 
    int categories[13];
    int dices[5];
    char name[20];
} YB;
extern bool boundarycheck(int from, int to, int *target);
void RollTheDice(YB *player, int* reroll);
void ShowTheDice(YB *player);
void SelectDice(YB *player, bool* mode);
void SetScore(YB *player);
void DisplayInfo(YB *player);
void YachtProcedure(YB *currentplayer, bool *mode);
void DisplayCategoryInfo(YB *player);
void initialize(YB *player, char* name);
void YachtDice(char *playername, FILE *fp);

#endif
