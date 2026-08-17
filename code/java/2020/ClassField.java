class PersonData {
    public String name;
    public int age;
    public float weight;
}

public class ClassField {
    public static void main(String[] args) {
        // 객체를 생성하고 필드에 값을 저장합니다.
        PersonData data = new PersonData();
        data.name = "kim";
        data.age = 20;
        data.weight = 1.2f;

        System.out.println(data.name);
        System.out.println(data.age);
        System.out.println(data.weight);
    }
}
