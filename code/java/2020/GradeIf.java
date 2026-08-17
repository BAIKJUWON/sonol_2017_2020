import java.util.Scanner;

public class GradeIf {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("점수: ");
        int n = in.nextInt();

        if (n >= 90 && n <= 100) {
            System.out.println("A");
        } else if (n >= 80) {
            System.out.println("B");
        } else if (n >= 70) {
            System.out.println("C");
        } else {
            System.out.println("F");
        }

        in.close();
    }
}
