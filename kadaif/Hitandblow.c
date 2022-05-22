// Hitandblow.c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 
#include <math.h>
#include <time.h>
#include "Hitandblow.h"

void Hitandblow(char* name, FILE *fp){
    //　変数生成
    int *target, digit, MAXCOUNT, *target_index, index, cur_index, num, current_number, strike, ball;
    target = (int*)calloc(digit, sizeof(int));
    srand((unsigned int)time(NULL));
    // 桁数の指定及び重複していない乱数の生成
    printf("How many digits do you want? ");
    scanf("%d", &digit);
    MAXCOUNT = 2*digit - 1;
    
    for(target_index = target; target_index != target + digit; target_index++){
        int* loop_index;
        *target_index = rand()%10;
        for(loop_index = target; loop_index != target_index; loop_index++){
            if(*target_index == *loop_index){
                target_index--;
                break;
            }
        }
    }
    printf("\n%d digits number is created!", digit);
    /*
    正解になるまでループする。
    1.１つも当たってない場合にはアウトになる。
    2.桁と数字が同じであれば、ストライク。
    3.数字はあってるが桁が異なると、ボール。
    */
    while(MAXCOUNT > 0){      
        printf("You have %d chances\n", MAXCOUNT);
        MAXCOUNT--;
        //do{   
            printf("Enter the number : ");
            scanf("%d", &num);
        //}while(!boundarycheck(0,(int)pow(10,(double)digit)-1,&num));
        strike = 0;
        ball = 0;
        cur_index = digit-1;
        while(cur_index >= 0){
            current_number = num % 10;
            num /= 10;
            for(index = digit-1; index != -1; index--){
                if(target[index] == current_number){
                    if(index == cur_index) strike++;
                    else ball++;
                }
            }
            cur_index--;
        }
        if(strike == 0 && ball == 0) printf("Out!\n");
        else printf("%d strike %d ball\n",strike, ball);
        if(strike == digit){
            printf("Good jjob!");
            break;
        }
    }
    if(MAXCOUNT == 0 && strike != digit){
        printf("You can do better than this!! \n");
        printf("The Answer was : ");
        for(index = 0; index<digit; index++){
            printf("%d",target[index]);
        }
        printf("\n");
    }
    free(target);
    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    if(fprintf(fp,"Hitandblow %s %d %d.%d.%d\n", name, 7-MAXCOUNT, t->tm_year + 1900,t->tm_mon+1,t->tm_mday) > 0) printf("History is saved successfully!");
    return;
}