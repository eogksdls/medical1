-- trunc 버림, round 반올림
select sysdate, hire_date, trunc(sysdate-hire_date) as 근속기간 from employees;

-- 어제 sysdate-1, 내일 sysdate+1
select sysdate-1 어제, sysdate 오늘, sysdate+1 내일, sysdate+100 from dual;

-- 퀴즈 : m_yesterday, m_today, m_tomorrow,m_year의 날짜컬럼을 가진 테이블 생성
create sequence mno_seq
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

create table m_date(
    m_no varchar2(15),
    m_today varchar2(15),
    m_tomorrow varchar2(15),
    m_year varchar2(15)
    
);
insert into m_date values(
mno_seq.nextval, sysdate, sysdate+1, sysdate+365);

select m_no no,m_today today,m_tomorrow tomorrow,m_year as afteryear from m_date;

-----------------------------------------------------------------------------------
-- abs: 절댓값, ceil: 올림, round: 반올림(자릿수 가능), floor: 버림, trunc: 버림(자릿수 가능)
select abs(hire_date-sysdate) from employees;

select hire_date,round(hire_date,'month') from employees;

--날짜의 월을 기준으로 버림
select hire_date, trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') 기준일, hire_date from employees
order by hire_date;

------------------------------------------------------------------------------------
select * from channels;

select period,count(period) from kor_loan_status
group by period --기간 별로 수를 센 것
order by period;

select period from kor_loan_status
where period='201111';

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) from students -- 일의자리 수 버림
group by trunc(kor,-1)
order by t_kor;

-- 날짜의 월을 기준으로 버림
select trunc(hire_date,'month') m_hire_date, count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by trunc(hire_date,'month');

-----------------------------------------------------------------------------------------------
--drop table stu_score;
--drop table emp01;
--drop table board;

select * from stu_score
order by no;

update stu_score set name = '관순스'
where no = 10;

select * from stu_score;

update stu_score set avg=round(total/3,3);
select * from stu_score;

----------------------------------------------------------------------------------------------------
-- 2개의 날짜에서 월 간격을 확인
select hire_date, floor(months_between(sysdate,hire_date)), trunc(sysdate-hire_date,2) from employees;

-- 개월 추가
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

-- 한 주를 기준으로 일요일 or 토요일 출력 (반올림)
select sysdate,round(sysdate, 'd') from employees;

-- 닐짜를 기준으로 현재일, 처음일, 마지막일
select sysdate 현재일, trunc(sysdate,'month') 처음일, last_day(sysdate) 마지막일 from dual;

-- 특정 요일의 날짜를 확인
select sysdate, next_day(sysdate,'수요일') from dual;

-- 요일의 처음일
select sysdate,trunc(sysdate,'d'), next_day(sysdate,'토요일') from dual;

---------------------------------------------------------------------------------------------
-- board 테이블 default는 입력이 없을 시 지정한 데이터가 자동으로 입력된다.
create table board(
bno number(4) primary key, -- 중복이 안됨, null 허용하지 않음. 기본키로 사용됨
id varchar2(30),
btitle varchar(1000),
bcontent clob,  -- varchar2(3000)까지만 제한 but clob은 무제한(type은 varchar와 동일)
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','제목입니다.','내용입니다.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);

--default 값이 지정되어 있어, 따로 안넣어줘도 값이 출력된다.
insert into board(bno,id,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','이벤트 신청','이벤트를 신청합니다.',board_seq.currval,'2.jpg'
);

select * from board;

--------------------------------------------------------------------------------------
--형변환 : number(숫자형), character(문자형), date(날짜형)

select sysdate from dual;

--문자열로 변형해야 날짜 출력형식을 바꿀 수 있다.
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

--퀴즈 ko20240001 형식으로 출력하기(문자끼리는 + 사용을 할 수 없음. ||을 사용하자~)
select 'ko'||to_char(sysdate, 'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'),to_char(sysdate,'day') from dual; -- 수 // 수요일

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

--퀴즈 hire_date를 년월일 시간 월 요일 형식으로 출력하기
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees;

-----------------------------------------------------------------------------------------
--am, pm 오전, 오후 형식 출력 hh24  24시간으로 표시
select to_char(sysdate, 'pm hh24:mi:ss') from dual;

--drop table stu_score;
select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

--날짜별로 몇개의 데이터가 들어가있는지 출력하시오
select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') c_date_, count(to_char(c_date,'yyyy-mm-dd hh:mi:ss day')) count from stu_score
group by to_char(c_date,'yyyy-mm-dd hh:mi:ss day')
order by c_date_
;
-------------------------------------------------------------------------------------
-- 문자형은 사칙연산(+,-,*,/)이 불가능. 하지만 자리수 표시, 쉼표 표시 가능
-- 숫자형 사칙연산 가능/ 컬럼별 사칙연산 가능/ 자리수 표시(0001->안됨), 쉼표표시 안됨.
-- 날짜형 +,- 연산기능 가능, months_between 2개 날짜 사이 개월 수 계산가능, 하지만 날짜유형을 지정해서 출력이 안됨

-- 문자형 안에 있는 데이터가 숫자이면 자동으로 형변환해서 계산해줌
-- 문자형 안에 문자가 있으면 자동 형변환 불가
select 10 a, 100 b, (10+100) ab, to_char(100), 10+'100' from dual;
select 10 a, 100 b,(10+100) ab, to_char(100),10+'100원'  from dual;

-- '0000' 빈자리는 0으로 채움, '9999' 빈자리는 공백으로 둠.
select 12340000, to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(12340000), to_char(12340000), to_char(12340000,'999,999,999'),
length(to_char(12340000,'999,999,999')) from dual;

-- L 은 원화 표시
select 12340000, to_char(12340000,'L999,999,999') from dual;
-- $ 는 $ 표시
select 12340000, to_char(12340000,'$999,999,999') from dual;
-- 
select 1234.1234, to_char(1234.1234),to_char(1234.1234, '000,999.99') from dual;

--10개 자리수 표시
-- 공백제거해서 자리수 확인 trim 사용
select length(trim(to_char(12345, '0000000000'))), length(trim(to_char(12345,'999,999'))) from dual;

--퀴즈
--123,456,789 + 100,000 값을 출력하시오/ 천단위 표시
--123,556,789
------------------------------
--1. 123,456,789 쉼표 제거
select replace('123,456,789',',','') from dual;
--2. 타입을 number로 변경
select to_number(replace('123,456,789',',','')) from dual;
--3. 더하기
--4. 문자형 타입으로 변경해서 원화, 쉼표 표시
select to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')),'L999,999,999') sum from dual;

select '123,456,789' n1, '100,000' n2,
to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')),'L999,999,999') sum from dual; 

----------------------------------------------------------------------------------------------------------------------------
-- 데이터 길이 함수
select length('안녕하세요') from dual;
select length(1234000) from dual;

select to_number('0001234') from dual; -- 1234만 출력

----------------------------------------------------------------------------------------
-- 날짜형
-- 문자형 +,- 안됨
select '2024-04-24 11:00:00'-'2024-04-01 10:00:00' from dual; --오류
select to_date('2024-04-24')-to_date('2024-04-01') from dual;
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;

select to_date('2024-04-24 11:00:00') from dual;

-- 퀴즈 
-- '20240401'형태를 2024-04-01 타입으로 변경해서 출력
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

select hire_date from employees
where hire_date >= '20080101'
;

select * from stu_score;

--문자형일지라도 날짜형을 띠면 알아서 인식을 할 수 있다.
select c_date from stu_score
where c_date = '2024/04/05';

select sysdate-to_date('2024/04/01') from dual;

-- 퀴즈
-- 20,000 / 10,000 문자형에서 
select '20,000', '10,000' from dual;
-- 콤마 제거
select replace('20,000',',',''), replace('10,000',',','') from dual;
select to_number('20,000','99,999') from dual; -- 바로 숫자형으로 형변환
-- 숫자형으로 형변환 후 나누기
select to_number(replace('20,000',',',''))/to_number(replace('10,000',',','')) from dual;
select to_number('20,000','99,999') / to_number('10,000','99,999') from dual;

-- 퀴즈
select commission_pct from employees;
-- 실제월급 = 월급 + (월급 * 커미션) 실제월급해서 출력하시오
select salary, salary+(salary*nvl(commission_pct,0)),commission_pct from employees;

-- commission_pct null값만 출력하시오
-- is null
select commission_pct from employees
where commission_pct is null ;

-------------------------------------------------------------------------------------
select manager_id from employees
order by manager_id desc;

-- 퀴즈 매니저아이디가 null이면 0으로 출력 -> nvl(데이터명,0)
select nvl(manager_id,0) from employees
order by manager_id desc;

-- 퀴즈 manager_id가 null이면 ceo로 입력하시오
-- ceo는 문자열이기 때문에 manager_id 또한 문자열로 변환해주어야 한다. 
select nvl(to_char(manager_id), 'ceo') from employees
order by manager_id desc;




