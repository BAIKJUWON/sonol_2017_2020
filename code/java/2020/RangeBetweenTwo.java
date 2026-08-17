import java.util.Scanner;

public class RangeBetweenTwo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("첫 번째 정수: ");
        int n = Integer.parseInt(in.nextLine());
        System.out.print("두 번째 정수: ");
        int m = Integer.parseInt(in.nextLine());

        // 작은 값이 앞에 오도록 교환합니다.
        if (n > m) {
            int temp = n;
            n = m;
            m = temp;
        }

        for (int i = n; i <= m; i++) {
            System.out.println(i);
        }

        in.close();
    }
}
