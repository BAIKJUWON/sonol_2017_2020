#include <stdio.h>

int main(void) {
    int a;

    a = 90;

    // 점수 구간에 따라 등급을 출력합니다.
    if (a >= 90) {
        printf("A\n");
    } else if (a >= 80) {
        printf("B\n");
    } else {
        printf("C\n");
    }

    return 0;
}
