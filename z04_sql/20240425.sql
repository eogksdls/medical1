-- 어제,오늘,내일
select sysdate-1, sysdate, sysdate+1 from dual;

-- 오늘, 이달의 첫일, 이달의 마지막일
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- 두 날짜간 일수
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date)) from employees;

-- trunc 일단위 버림, group by 그룹함수
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

-- 퀴즈, hire_date 날짜에서 월만 출력하시오
-- 2008-01-01 형식으로
select to_char(hire_date,'month') month, count(to_char(hire_date,'month')) count from employees
group by to_char(hire_date,'month')
order by month;

-- 퀴즈, hir_date 2008년도, 년도별 인원수를 출력하시오.
select to_char(hire_date,'yyyy') year, count(to_char(hire_date,'yyyy')) count from employees
group by to_char(hire_date,'yyyy')
order by year;

------------------------------------------------------------------------------------------------
-- 형변환 -> number, character, date
-- number 사칙연산 가능, 쉼표표시는 불가능, 원화표시도 불가능
-- char 사칙연산(+,-) 안됨, 쉼표 표시 가능, 원화표시 가능
-- date +,- 가능 날짜 출력형태는 변경불가 -> to_char로 형변환을 해주어야 한다.!!


-- 시퀀스, 날짜의 년도를 가지고 학번을 부여하려고 함
--ko20240001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) stu_no from dual;

--drop table stu_no;

-- 문자형 타입 퀴즈
-- 출력형태 : 123,556,789
select replace('123,456,789',',',''), replace('100,000',',','') from dual;
select to_char(to_number(replace('123,456,789',',',''))+
to_number(replace('100,000',',','')),'999,999,999') sum from dual;

select to_char(to_number('123,456,789','999,999,999')-to_number('100,000','999,999'),'999,999,999') from dual;

---------------------------------------------------------------------------------------------------
-- 숫자타입을 날짜타입으로 변경
select 20240425 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425+3) from dual;

-- 숫자타입을 날짜타입으로 변경
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

-- 퀴즈: 08월에 입사한 사원 이름, 2번째에 a가 들어가 있는 사람을 출력하시오.
select emp_name, hire_date from employees
where to_char(hire_date,'mm') in ('08','05','01') and emp_name like '_a%'
order by hire_date;

-- 퀴즈: 20070101 이후 입사한 사원이름, 2번째에 a가 들어가 있는 사람을 출력하시오.
select emp_name, hire_date from employees
where hire_date > to_date(20070101) and emp_name like '_a%';

------------------------------------------------------------------------
select trunc(sysdate-to_date('20240401'),0) from dual;
select sysdate, '2024-04-01', trunc(sysdate-to_date('2024-04-01')) from dual;

--------------------------------------------------------------------------
create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

-- 입력시 날짜타입에 문자(형태-날짜형태)를 입력해도 저장됨.
-- 날짜와 문자를 뼤기는 불가능, 그래서 문자를 날짜타입으로 변경해야 함.
insert into eventDate values(
seq_mno.nextval, sysdate, '2024-02-01', trunc(sysdate-to_date('2024-02-01'),0)
);

select * from eventDate;

-----------------------------------------------------------------------------
-- 문자타입을 숫자타입으로 변경
select to_number('20,000','999,999')-to_number('10,000','999,999') from dual;

-- null을 0으로 치환 nvl()
select salary, salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

------------------------------------------------------------------------------
-- 그룹함수 :  sum, avg, count(), count(*), min, max
-- 일반 열의 조회와 그룹함수는 동일한 select에 같이 쓸 수 없다.

-- count 함수 -> number 형태
select count(*) from employees; --모든 컬럼의 수를 카운트 해준다.(107개)
select count(emp_name) from employees; -- (107개)
select count(manager_id) from employees; -- null값은 count가 안된다.(106개)


select emp_name,manager_id from employees;

-- sum : 총합
select sum(salary) from employees;

-- avg : 평균
select avg(salary) from employees;
-- 평균보다 월급이 높은 사람을 출력하시오
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees)
order by salary;

-- min: 최솟값, max: 최댓값
select min(salary), max(salary) from employees;
--최소월급을 받는 사람의 사번, 이름을 출력하려면?
select employee_id, emp_name, salary from employees
where salary = (select min(salary) from employees);
-- 최대 월급을 받는 사람의 사번, 이름 출력
select employee_id, emp_name, salary from employees
where salary = (select max(salary) from employees) ;

-- 부서번호가 50번인 사람만 전체 월급 합계를 내고 싶음
select department_id, salary from employees;

select sum(salary) from employees
where department_id = 50;

-- 퀴즈 : kor 점수가 80점 이상인 학생을 출력하시오
select * from stu_score;
select no, name, kor from stu_score
where kor > 80;

-- 퀴즈 : 국어점수 평균이상, 영어점수 평균이상인 학생만 출력하세요
select no, name, kor, eng from stu_score
where kor >= (select avg(kor) from stu_score) 
and eng >= (select avg(eng) from stu_score);

select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) 
and eng >= (select avg(eng) from stu_score);

------------------------------------------------------------------------
create table s_info (
sno number,
s_count number

);

insert into s_info values(
stu_seq.nextval,2000
);

insert into s_info values(
stu_seq.nextval, ( select count(*) from stu_score
where kor >= (select avg(kor) from stu_score) 
and eng >= (select avg(eng) from stu_score) )
);

select * from s_info;

-- 퀴즈. 국어점수 최고점인 학생, 영어점수 최고점인 학생, 수학점수 최고점인 학생 출력
select name, kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math = (select max(math) from stu_score)
order by kor desc, eng desc, math desc;
--------------------------------------------------
-- 퀴즈. 월급이 최대, 최소, 평균인 사원을 출력하시오
-- 평균보다 낮은 값
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc;

select avg(salary) from employees; -- 평균 : 6461.83177....

-- 평균보다 낮은 사원들 중 월급의 최대값 찾기 : 6400
select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
;

-- 또는 평균보다 높은 사원들 중 월급의 최소값 찾기 : 
select min(salary) from (select emp_name, salary from employees
where salary >= (select avg(salary) from employees)
order by salary desc)
;

-- 대입하기
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select max(salary) from (select emp_name, salary from employees
                                      where salary <= (select avg(salary) from employees)
                                      order by salary desc));

-----------------------------------------------------------
----------------------------------------------------------------------------------
-- 문자함수
-- lpad(왼쪽), rpad(오른쪽) 빈공백 채우기
select emp_name, lpad(emp_name, 15, '#') from employees;
select emp_name,rpad(emp_name, 20, '@') from employees;

-- ltrim(왼쪽), rtrim(오른쪽) 지정한 문자를 잘라내고 출력
select emp_name, ltrim(emp_name,'Do') from employees;

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(데이터, 순서, 개수)
select emp_name, substr(emp_name,3,4) from employees;

select job_id, employee_id from employees;

-- 퀴즈. job_id에 있는 SH와 사원번호를 결합해서 출력하시오
select emp_name, substr(job_id,0,2)||employee_id from employees;

------------------------------------------------------------------------
-- length
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- 날짜함수 +,- 가능, 하지만 날짜데이터끼리 더하기(+)는 불가능
-- 날짜 데이터 + 숫자 가능
select sysdate+1 from dual;

-- 날짜 데이터 - 날짜 데이터 가능
select sysdate - hire_date from employees;

-- 날짜 데이터 + 날짜데이터 불가능
select sysdate + hire_date from employees;

-- 월을 기준으로 반올림
select round(sysdate,'month') from dual;

-- trunc: 버림, round: 반올림 => 자리수 지정 가능
select sysdate, trunc(sysdate,'month'), round(sysdate,'month') from dual;

-- 년을 기준으로 반올림
select round(sysdate,'year') from dual;

-- 개월 수 더하기
select sysdate, add_months(sysdate,3) from dual;

-----------------------------------------------------------------------------
-- ceil: 올림, floor: 버림, mod: 나머지, power: 제곱
select ceil(-4.2), floor(-4.2), mod(8,3), power(3,2) from dual;

--퀴즈 
--" 이름 1979년 09월 19일 수요일" 형태로 조회
select concat(emp_name,to_char(hire_date,'  yyyy"년" mm"월" dd"일" day')) from employees;

-- 퀴즈. 사원명, 월급*1400 앞에 원화표시와 쉽표를 넣어주세용
-- 빈공백은 0으로 표시
select emp_name, to_char(salary*1400,'L00,000,000') from employees;
-- 정상표시
select emp_name, to_char(salary*1400,'L999,999,999') from employees;

-- 자신의 생일과 자신의 생일 속한 달의 마지막 날짜를 출력하세요
-- '2010-10-10' 이것을 통해.
select to_char(trunc(to_date('2010-10-10'),'month'),'yyyy-mm-dd') m_firstday,to_char(to_date('2010-10-10'),'yyyy-mm-dd') birthday,
to_char(last_day('2010-10-10'),'yyyy-mm-dd') m_lastday from dual;

----------------------------------------------------------------------------------------------
select * from member;

desc member;

-- DDL(data definition language) 

-- column 추가, 삭제, 수정
-- default: female, null을 허용하지 않음
-- 위 commit, rollback이 안됨 => 바로 저장된다.
alter table member add gender varchar2(6) default 'female' not null; 

-- 컬럼 삭제
--alter table member drop column phone;

-- 컬럼 수정 -> 컬럼 이름, 타입변경 가능
alter table member rename column name to stu_name
;
desc member;

-- 타입 변경
alter table member modify(stu_name varchar2(50));
alter table member modify(stu_name varchar2(3)); -- 일부값이 너무 커서 열 길이를 줄일 수 없음
--> 기존의 데이터가 변경하려는 크기보다 작을 때만 가능함
-- 제약없이 컬럼의 타입을 변경하려면 컬럼데이터가 빈공백이거나, update member set stu_name=" "
-- null일 때 가능하다
alter table member modify(stu_name number(100)); -- 수치의 정도 범위(38자리 이내)를 초과했습니다

desc member;

select * from member;

update member set gender = 'male';

commit;



