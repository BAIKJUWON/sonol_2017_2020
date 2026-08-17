import java.util.Scanner;

public class IfCompareTen {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("입력: ");
        int n = in.nextInt();

        if (n > 10) {
            System.out.println("10보다 크다");
        } else {
            System.out.println("10보다 작거나 같다");
        }

        in.close();
    }
}
