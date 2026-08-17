import java.io.IOException;

public class SystemInChar {
    public static void main(String[] args) throws IOException {
        System.out.print("입력: ");
        // 읽은 정수 값을 문자로 변환합니다.
        char ch = (char) System.in.read();
        System.out.println(ch);
    }
}
