class Person {
    private int age;
    private String name;

    public Person() {
    }

    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }
}

public class GetterSetter {
    public static void main(String[] args) {
        // 기본 생성자와 setter를 이용합니다.
        Person hong = new Person();
        hong.setAge(20);
        hong.setName("홍길동");

        // 매개변수가 있는 생성자를 이용합니다.
        Person hong2 = new Person(20, "홍길동");
        hong2.setName("김길동");

        System.out.println(hong.getAge());
        System.out.println(hong.getName());
    }
}
