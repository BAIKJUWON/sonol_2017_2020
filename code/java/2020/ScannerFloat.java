import java.util.Scanner;

public class ScannerFloat {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("입력: ");
        float value = in.nextFloat();
        System.out.println(value);
        in.close();
    }
}
