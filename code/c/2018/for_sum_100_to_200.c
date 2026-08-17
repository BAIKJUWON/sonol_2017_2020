#include <stdio.h>

int main(void) {
    int i;
    int sum;

    sum = 0;

    // 100부터 200까지의 합을 구합니다.
    for (i = 100; i <= 200; i++) {
        sum += i;
    }

    printf("%d\n", sum);

    return 0;
}
