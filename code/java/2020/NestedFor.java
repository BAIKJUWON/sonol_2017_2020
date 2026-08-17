public class NestedFor {
    public static void main(String[] args) {
        // 이중 반복문으로 i와 j의 조합을 출력합니다.
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 2; j++) {
                System.out.println(i + " : " + j);
            }
        }
    }
}
