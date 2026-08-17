#include <stdio.h>

void main2(void);
void main3(void);

int main(void) {
    int i;

    printf("a");
    main2();
    printf("b");
    main3();

    for (i = 0; i < 100; i++) {
        printf("c");
    }

    return 0;
}

void main2(void) {
    printf("n");
}

void main3(void) {
    printf("c");
}
