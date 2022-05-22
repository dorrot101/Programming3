/*
    本プログラムはHitandBlowゲームとヨット(YACHT)ゲームができるプログラムである。
    最初にプレイヤー名を入力して始まる。
    以後、ゲームを選択して楽しむことができる。
    ゲームの終了時に記録が残される。
*/
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include "Yacht.h"
#include "Hitandblow.h"
//　境界を与えてターゲットのバウンダリーチェックを行う。
bool boundarycheck(int from, int to, int *target){
    return (*target < from || *target > to)?false:true;
}
int main(void){
    int gamemode = 0;
    char name[20];
    // "history.txt"ファイルの有効性をチェックして有効でなければ終了させる。
    FILE *fp = fopen("history.txt","at+");
    if(fp == NULL) {
        printf("History file is detroyed, or doesn't exist!!");
        return -1;
    }
    // 名前を入力してからゲームを選択する。
    printf("Enter your name : ");
    scanf("%s", name);
    printf("1: Hit and blow\t\t2: Yacht Dice\n");
    printf("Select Game : ");
    scanf("%d", &gamemode);
    switch(gamemode){
        case 1:
            printf("Hit and blow Game is initialized\n");
            Hitandblow(name, fp);
            break;
        case 2:
            printf("YachtDice Game is initialized\n");
            YachtDice(name, fp);
            break;
    }
    //　最後にテキストファイルを閉じてからファイルポインターを解除する。
    fclose(fp);
    return 0;
}