select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

--타입 : numebr +,-,*,/ 가능
select salary, salary * 1400 as m_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score;

--파이썬.

select department_id from employees;

select nvl(department_id,0) from employees; --null은 원래 0의 값이 아니기 때문에 직접 찾아서 0으로 바꿔줘야함

select * from employees;

--월급(월급+커미션)
select salary, salary + (salary*commission_pct) from employees; --null로 나옴
select salary, salary + (salary*nvl(commission_pct,0)) as real_sal from employees;
--오라클은 대소문자 구별이 없기 때문에, 구별해서 쓰고 싶으면 
--""를 사용하기(있는 그대로 출력가능) *별칭
select salary, salary + (salary*nvl(commission_pct,0)) as "Real_sal" from employees;

--별칭 사용에 한글도 가능하지만, 웬만하면 사용하지 않는게 좋다.(오류발생 가능성있음)
select salary as 연봉 from employees; 

--

select * from departments;

--부서 번호, 부서 이름을 출력하시오.

select department_id as "부서 번호",department_name as "부서 이름" from departments;

-- 여러개의 데이터를 1개로 합쳐서 넘겨야 할 경우 concat을 사용
-- concat : 홍길동, 유관순, 이순신, 강감찬, 김구 - > split(",") : 분리

select * from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

--distinct : 중복제거
--where : 조건절 not 제거하고 검색하려면 is not null -> null이 아닌 값들만 불러와라
select distinct department_id from employees where department_id is not null;

-- manager_id

select manager_id from employees;
select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;
select employee_id, salary from employees 
where employee_id = 200 or employee_id = 201 or employee_id = 202;

-- where : 조건절 응용
select * from employees
where employee_id >= 200 and employee_id <=203;

select * from employees
where employee_id >= 200 or employee_id <= 150;

--부서 번호 : 10,30,50 번에 해당하는 사원 출력
select employee_id, department_id from employees
where department_id = 10 or department_id = 30 or department_id = 50;

--월급 6000 ~ 9000 이하인 사원을 출력하시오
select * from employees;
select employee_id, salary from employees
where salary >= 6000 and salary <= 9000;

--월급 6000,7000,8000 인 사원을 출력하시오
select employee_id, salary from employees
where salary = 6000 or salary = 7000 or salary = 8000;

--부서번호가 50번이면서, 월급이 8000이상인 사원 출력
select department_id, employee_id, salary from employees
where department_id =50 and salary >= 8000;


drop table stu_score;

create table stu_score(
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);
insert into stu_score values (
5,'김구',100,100,100,300,100,1
);
commit;

--stu_score 이름이 홍길동인 사람을 출력하시오
select * from stu_score;

-- 역순정렬
select hire_date from employees
order by hire_date desc;

--순차정렬
select emp_name, hire_date from employees
where hire_date >='02/01/01'
order by hire_date asc;

--날짜 사칙연산 가능
select hire_date, hire_date+100 from employees;
--반올림 round
select round(sysdate-hire_date,2) from employees;

select * from employees;

--문자 합치기는 +연산자 불가능, ||명령어 사용
select emp_name||email from employees;

--입사일 05년 이상 06년 이하이면서 월급이 6000 달러 이상인 사원을 역순정렬로 출력하시오
select * from employees;
select emp_name, salary, hire_date from employees
where hire_date >='05/01/01' and hire_date <='06/12/31' and salary >= 6000
order by hire_date desc;

-- not 표시: !=, ^=, <>
select department_id from employees
where department_id <> 10 and department_id <> 50 
order by department_id
;

--5000 이상 9000 이하
select emp_name, salary from employees
where salary >= 5000 and salary <=9000
order by salary
;

-- 평균이 99점 이상인 학생을 검색하시오
select name, avg from stu_score
where avg >= 99
;

select * from students;

-- 이름 수정
update students set name='홍길자' 
where no = 8
;

commit;

select * from students;

--students
-- 국어가 70점, 평균이 75점 이상인 학생 출력
select name,kor,avg from students
where kor >=70 and avg >=75
;

--국어점수 80, 국어 점수 70, 국어 점수 90 인 학생을 출력하시오
select name, kor from students
where kor = 80 or kor = 70 or kor = 90
order by kor
;

-- in 
select name, kor from students
where kor in(80,70,90)
order by kor;

update students set kor=100
where no=1;

rollback;

select * from students
where no = 1;

-- 수정
update students set kor=100, total = 100+eng+math, avg =(100+eng+math)/3
where no =1;
select * from students
where no = 1;
commit;

-- 국어 점수 70~90점인 학생을 출력하시오
select name, kor from students
where kor >=80 and kor <=90
order by kor
;

-- 100명
select * from students;

-- 27명
--between a and b : a보다 크거나 같고, b보다 작거나 같은 것 검색  
--> >,<은 오류가 발생할 가능성이 있어 between을 사용함
select name, kor from students
where kor between 70 and 90
order by kor
;

-- 73명
-- not between a and b : a보다 크거나, b보다 작은 것 검색(a,b 포함 안됨)
select name, kor from students
where kor not between 70 and 90
;

-- 날짜도 between 사용 사능
select emp_name, hire_date from employees
order by hire_date;

--95년 이상, 01년 이하 입사일 사원 검색
select emp_name, hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc;

-- 이름 검색
select * from students
where name='홍길동';

-- like 검색 : 특정 단어가 포함되어 있는 데이터 검색
select * from students
where name like '%홍%';

-- 제일 끝글자가 홍인 단어를 검색하세요
select * from students
where name like '%홍';
-- 시작 단어 홍 : '홍%'
-- 끝 단어 홍 : '%홍'
-- 특정 단어 홍 : '%홍%'

-- '길'이 포함되어 있는 단어 검색
select * from students
where name like '%길%';

-- _: 한 칸 공간을 사용, 길 앞에 1개의 단어가 있으면서 길이 포함되어 있는 단어 검색
select * from students
where name like '_길%';

--3번째 칸에 t가 들어가는 이름 검색
select * from students
where name like '__t%';

--길이가 4이고, 3번째 r이 들어가 있는 이름 검색
--1) 코드는 짧을 수록 좋음
select * from students
where name like '__r_';
--2)
select * from students
where name like '__r%' and length(name) = 4;

-- 이름이 A로 시작되는 학생 이름을 검색하세요
select * from students
where name like 'A%';

-- 이름에 a가 들어가 있는 학생 검색
select * from students
where name like '%a%'
order by name;

-- 대소문자 구분 없이 a가 들어가 있는 학생 검색
-- 소문자 치환(lower), 대문자 치환(upper), 첫글자 대문자 (initcap)
select * from students
where lower(name) like '%a%';

-- 이름에 a가 포함되지 않은 학생 검색
select no,name from students
where lower(name) not like '%a%';


select manager_id from employees;
--manager_id가 100 인 사원 검색
select employee_id, emp_name, manager_id from employees
where manager_id = 100;

--null은 등가비교가 안됨
select employee_id, emp_name, manager_id from employees
where manager_id = null;

--null값을 찾을 땐 is 사용
select employee_id, emp_name, manager_id from employees
where manager_id is null;

select * from employees
where manager_id is not null;
--------------------------------------------------------------------------
select * from stu_score;

-- 한글 정렬도 가능
select * from stu_score
order by name asc;

-------------------------------------------------------------------------
select * from students;

--kor 값이 동일할 경우, eng 기준 순차정렬 진행
select * from students
order by kor desc, eng asc;

-- total로 역순정렬(desc)
select * from students
order by total desc;

--------------------------------------------------------------------------
-- 컬럼추가
alter table students add rank number(3);
-- 컬럼타입
desc students;

select * from students;

update students set rank = 0;

commit;

--------------------------------------------------------------------------
-- 등수 매기기(보여지지만, table에 저장은 안됨)
select no,name,total,rank() over(order by total desc) as rank from students;

select * from students; 
-- no=1에 13등 업데이트
update students set rank = 13
where no = 1;

select * from students
where no =1;

-- 2번째 방법
update students s1 set rank = 13
where no = 1;

-- 전체 등수 업데이트
update students s1 set rank = (select ranks from 
( select no no2, rank() over(order by total desc) as ranks from students) s2
where s1.no = s2.no2);

select * from students;
commit;

-- select * from (테이블);
-- 평균이 60점 이상인 학생들 중 국어성적이 70점 이상인 학생 검색
select * from (select * from students where avg >= 60)
where kor >= 70;

----------------------------------------------------------------------