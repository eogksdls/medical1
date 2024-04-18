--가지고 있는 테이블 검색
--F5: console창 모양(스크립트 출력, 이전 거까지 전체실행), F9: 테이블 형태(질의 결과, 한 줄씩 실행)
--웬만하면 F9를 눌러 한 줄씩 실행하기
--console 창에서 보고 싶으면 그 줄만 드래그해서 F5 누르면 됨
select * from tab;

select * from employees;

--테이블 구조 확인(console창에서 볼 수 있다)
desc employees;

--테이블 생성
create table stu_score(
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2) -- 5자리 중 2개는 소수점으로 표기해라
);

insert into stu_score(no,kor,eng,avg) values(
1,100,99,(100+99)/2
);

insert into stu_score values( --변수를 모두 채우면 위처럼 (no,kor,eng,avg)작성 안해도 됨!
1,95,98,(95+98)/2
);

insert into stu_score values(
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;
-- 데이터 반영(이전 데이터 복원,수정 불가능)
commit;

create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);

-----------------------------------------------------------------------------
--현재 날짜(기본 형태)
-- dual이란 가상테이블에서 가져오는 것
select sysdate from dual;
-- 출력형태 지정
-- 날짜 포맷변경 :  to_char 형변환 -> 포맷을 지정
select to_char(sysdate,'yyyy-mm-dd') from dual;
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'hh:mi:ss') from dual;

--현재로부터 +1000일 후의 날짜를 보여줌
select sysdate+1000 from dual;

select sysdate - to_date('24/01/01') from dual;
