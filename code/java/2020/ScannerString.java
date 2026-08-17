import java.util.Scanner;

public class ScannerString {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("입력: ");
        String name = in.nextLine();
        System.out.println(name);
        in.close();
    }
}
