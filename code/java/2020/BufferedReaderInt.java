import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferedReaderInt {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("입력: ");
        String str = in.readLine();
        // 문자열을 정수로 변환합니다.
        int num = Integer.parseInt(str);
        System.out.println(num);
    }
}
