#include <stdio.h>

int main(void) {
    int number;
    float value;

    number = 10;
    value = 10.0f / 3.0f;

    // 정수와 실수를 각각 형식 지정자로 출력합니다.
    printf("%d\n", number);
    printf("%f\n", value);

    return 0;
}
