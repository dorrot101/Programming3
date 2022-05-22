#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void func(int arr[][2]){
    int j,k,i;
    int(*temp)[2] = arr;
    for(j = 0; j<5; j++){
        for(k=0;k<4;k++){
            if(arr[k][1] < arr[k+1][1]){
                    temp = &arr[k];
                    arr[k] = arr[k+1];
                    arr[k+1] = temp;
            }
        }
    }
}

int main(void){
    int a[5][2];
    int i,j,t;
    srand((int)time(NULL));
    t = rand()%90 + 10;

    for(i = 0; i<5; i++){
        a[i][0] = i+1;
        a[i][1] = t;
        printf("%d : %d\n", a[i][0], a[i][1]);
        t = rand()%90 + 10;
    }

    func(a);

        for(i = 0; i<5; i++){

        printf("%d : %d\n", a[i][0], a[i][1]);

        }

    int input;
    printf("input the number : ");
    scanf("%d",&input);
    for(i = 0; i<5; i++){
        if(a[i][0] == input) printf("%d is %d", input, i+1);
    }

}