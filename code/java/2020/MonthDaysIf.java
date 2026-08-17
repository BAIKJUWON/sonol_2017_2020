import java.util.Scanner;

public class MonthDaysIf {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("월을 입력하시오: ");
        int month = Integer.parseInt(in.nextLine());

        if (month == 2) {
            System.out.println("28일");
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            System.out.println("30일");
        } else {
            System.out.println("31일");
        }

        in.close();
    }
}
