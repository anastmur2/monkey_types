#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

#define C_NUM 200000 // 'Tis roughly two times ten thousand
                     // more characters
                     // than needed,
                     // but better more than less ig

void monkey_type(int argc, char *argv[]) {
    // 32 - 126 & 13 ASCII
    char c[C_NUM];

    srand(time(NULL));

    for(int i = 0; i < C_NUM-1; i++) {
        
        int r = (rand() % 96) + 32;
        if (r == 127) {
            r = 13;
        }
        // printf("%d\n", r);
        c[i] = r;
    }

    c[C_NUM-1] = '\0';

    FILE *f = fopen("isithamlet.txt", "w");

    if(f) {
        fwrite(c, sizeof c[0], C_NUM, f);
    }
}