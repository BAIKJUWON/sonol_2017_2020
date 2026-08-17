import java.io.IOException;

public class SystemInAscii {
    public static void main(String[] args) throws IOException {
        System.out.print("입력: ");
        // 한 바이트를 읽어 정수 코드값으로 출력합니다.
        int ch = System.in.read();
        System.out.println(ch);
    }
}
