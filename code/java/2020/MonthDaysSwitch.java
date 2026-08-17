import java.util.Scanner;

public class MonthDaysSwitch {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("월을 입력하시오: ");
        int month = Integer.parseInt(in.nextLine());
        int day;

        switch (month) {
            case 2:
                day = 28;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                day = 30;
                break;
            default:
                day = 31;
                break;
        }

        System.out.println(day + "일");
        in.close();
    }
}
