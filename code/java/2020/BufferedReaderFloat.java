import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferedReaderFloat {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("입력: ");
        String str = in.readLine();
        // 문자열을 실수로 변환합니다.
        float num = Float.parseFloat(str);
        System.out.println(num);
    }
}
