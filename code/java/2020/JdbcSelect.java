import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JdbcSelect {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/javadb";
        String user = "root";
        String pass = "1234";

        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection conn = DriverManager.getConnection(url, user, pass);
            Statement stm = conn.createStatement();

            // phone_table의 모든 행을 조회합니다.
            ResultSet rs = stm.executeQuery("select * from phone_table;");
            while (rs.next()) {
                String name = rs.getString(1);
                String phone = rs.getString(2);
                int age = rs.getInt(3);
                System.out.println(name + "," + phone + "," + age);
            }

            conn.close();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}
