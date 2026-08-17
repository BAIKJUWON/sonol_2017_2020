-- 전화번호 테이블 생성
CREATE TABLE phone_table (
    name VARCHAR(20),
    phone VARCHAR(30),
    age INT
);

-- 당시 학습 환경에서 사용한 문자셋 설정
SET CHARACTER SET euckr;

-- 예제 데이터 입력
INSERT INTO phone_table VALUES ('곽혁순', '010-1223-1556', 20);
INSERT INTO phone_table VALUES ('곽규빈', '010-3223-1556', 17);
INSERT INTO phone_table VALUES ('김경우', '010-2333-1436', 43);

COMMIT;

-- 전체 데이터 조회
SELECT * FROM phone_table;
