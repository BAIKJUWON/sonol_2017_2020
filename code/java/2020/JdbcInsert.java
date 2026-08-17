import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class JdbcInsert {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/javadb";
        String user = "root";
        String pass = "1234";

        try {
            // MySQL JDBC 드라이버를 불러옵니다.
            Class.forName("com.mysql.jdbc.Driver");

            // 데이터베이스에 연결합니다.
            Connection conn = DriverManager.getConnection(url, user, pass);
            Statement stm = conn.createStatement();

            // 한 행을 추가합니다.
            String sql = "insert into phone_table values('곽경우','010-9877-3223',20);";
            stm.executeUpdate(sql);

            conn.close();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}
