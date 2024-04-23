-- <5장 내용>
select * from students;

--순차정렬
select * from students
order by name asc;

--alter table students add rank number(3);

--update students set rank = 0;

--commit;

-----------------------------------------------------------
select total, rank() over(order by total desc) rank
from students;

update students set total = 0;
-- 모든 total 값이 0

select * from students;

update students set total=(kor+eng+math);

--1. 기본 구문:
-- update students as s1 set rank=()

--2. rank()구문:
--(select no, rank() over(order by total desc) as ranks from students) s2;

update students s1 set rank=(select ranks from
(select no, rank() over(order by total desc) as ranks from students s2) 
where s1.no = s2.no);

select * from students;
commit;

--역순정렬
select no,total,rank from students
order by total desc;

--순차정렬
select no,total,rank from students
order by no;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

--역순정렬 :  null값이 제일 먼저 나옴
select manager_id from employees
order by manager_id  desc;

--날짜 역순정렬 : 가장 최신 날짜가 먼저 나온다
select hire_date from employees
order by hire_date desc;

select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

-------------------------------------------------------------------------
-- 퀴즈
-- 입사일로 오름차순, 컬럼 사원번호,사원명,부서번호,직급,입사일,월급 출력
select * from employees;

select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date asc;

--퀴즈2
--급여를 적게받는 사람 순으로 출력하되, 월급이 같으면 사원명으로 순차정렬
select employee_id, emp_name, job_id, hire_date, salary from employees
order by salary asc, emp_name asc;

--------------------------------------------------------------------------
--숫자함수
--abs: 절댓값
select -10, abs(-10) from dual; --dual은 가상 테이블

--floor: 소수점 버림
--round: 반올림
select 34.789, floor(34.789) as f, round(34.789) as r from dual;

--소수점 둘째 자리까지 반올림
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;

--음수는 정수부분
select 34.5678, round(34.5678,-1) from dual;

--trunc 지정한 자리수 이하 버림
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.45678) from dual;

--올림
select ceil(34.123) from dual;

--나누기
select 10/7 from dual;
--mod: 나머지
select round(100/7,2) from dual;
select mod(10,7) from dual;

-------------------------------------------------------------------------
--퀴즈
--국어점수 일단위 절사 출력
select trunc(kor,-1) kor from students
order by kor
;

--국어, 영어, 수학 일단위 절사해서 국영수 합계를 출력
select trunc(kor,-1) "국어", trunc(eng,-1) "영어", trunc(math,-1) "수학",
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) "합계" from students;

--사원번호가 짝수인 것을 출력하시오: 나머지가 0이면
--파이썬에선 employee_id%2 == 0
select employee_id from employees
where mod(employee_id,2) = 0;

--몫만 남게 하려면?
select floor(10/7) from dual;

--학번이 3의 배수인 것만 출력하시오: 3으로 나눠서 나머지 0
select * from students
where mod(no,3) = 0;
---------------------------------------------------------------------------
---------------------------------------------------------------------------
-- <6장> 시퀀스 :  기본키 설정!!
create sequence seq_no
    increment by 1 -- 1씩 증감됨
    start with 1   -- 1부터 시작
    minvalue 1     -- 최솟값 1
    maxvalue 9999  -- 최댓값
    nocycle        -- 순환하지 않음
    nocache       -- 캐시사용 않음
;
--nextval 시퀀스번호 1씩 증가
select seq_no.nextval from dual;

--currval 시퀀스 번호 확인
select seq_no.currval from dual;

-------------------------------------------------------------------------
--create table member (
--mno number(4),
--id varchar2(30),
--pw varchar2(20),
--name varchar2(30),
--phone varchar2(15)
--);

create sequence seq_mno
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval, 'eee', '1111', '강감찬','010-5555-5555'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

-- '00000' 자리수
select 's'||trim(to_char(seq_mno.nextval,'00000')) from dual;
-----------------------------------------------------------------------
-- 퀴즈
-- 한국대학교 ko20240001 학번 만들기!
-- 시퀀스 seq_kono 1 - 9999 까지
create sequence seq_kono
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

select to_char(sysdate,'yyyy') from dual;

-- trim()은 공백제거
select 'ko'||to_char(sysdate, 'yyyy')||trim(to_char(seq_kono.nextval,'0000')) as stuno from dual;

----------------------------------------------------------------------------------------------------

-- 게시판 만들기
create table board (
bno number(5) primary key,
bittle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

-- 퀴즈
-- 시퀀스  시작1001, 증감 10 1,99999
-- 5번 실행
create sequence seq_dept
    increment by 10
    start with 1001
    minvalue 1
    maxvalue 99999
    cycle
    nocache
;
select seq_dept.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar(30),
hire_date date
);

create sequence emp_seq
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

alter sequence emp_seq
    increment by 1001
;

insert into emp01 values(
emp_seq.nextval, '이순신', sysdate
);
select * from emp01;

commit;
----------------------------------------------------------------------------
--퀴즈 : 최근 입사한 직원을 먼저 출력
select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

-- 현재까지 입사한 일수를 함께 출력하세요
select employee_id, emp_name, job_id, hire_date, ceil(sysdate - hire_date)||'일' as "근속기간" from employees
order by 근속기간 desc;

select emp_name from employees;
-- 직급과 사번을 합쳐서 출력하시오..
select job_id||employee_id from employees;

----------------------------------------------------------------------------
-- substr: 문자열 잘라오기 함수, substr(대상,시작위치,길이)
select substr(job_id,0,2) from employees;
select emp_name, substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;


-- 퀴즈
-- job_id 앞에 2개문자와 사번 5자리 00001를 만들어 함께 출력
select substr(job_id,1,2)||trim(to_char(employee_id,'00000')) as emp_no from employees
order by emp_no
;
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- 날짜 함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

-- 현재-입사일 사이의 개월 수 확인 : 몇 개월 / 일 수
select round(MONTHS_BETWEEN(SYSDATE,hire_date),0), sysdate-hire_date from employees;

--개월 수를 추가( 2개월 후를 나타내줌)
select sysdate, add_months(sysdate,2) from dual;

--next_day :  현재를 기준점으로 지정하는 요일이 다음에 언제 오는 지 알려줌
select next_day(sysdate,'월요일') from dual;

-- 현재를 기준으로 달 말일을 알려줌
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;
