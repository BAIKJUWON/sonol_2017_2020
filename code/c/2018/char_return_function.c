#include <stdio.h>

char add(void);

int main(void) {
    char result;

    result = add();
    printf("%c\n", result);

    return 0;
}

char add(void) {
    // 문자 하나를 반환하는 함수 예제입니다.
    return 'n';
}
