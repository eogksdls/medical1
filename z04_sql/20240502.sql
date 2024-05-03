-- equi join: 같은 컬럼이 2개의 테이블에 존재하여 2개 컬럼을 이용해 검색하는 방법
-- non-equi join: 같은 컬럼이 없으면서 2개 테이블을 사용해 검색하는 방법
select name, s_amount, rank from (
select name,sum(amount) as s_amount from shop_product
where pdate >='2024/03/01' group by name), customer_rank
where s_amount between amount_low and amount_high
;

select name,sum(amount) as s_amount from shop_product
where pdate >= '2024/03/01'
group by name;

---------------------------------------------------------------------------------------
-- 2개 테이블  : department_id

select * from employees;
select * from departments;

select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;

select * from students; 
update students set id = 'aaa',name='홍길동',gender='M' where id='Marlo' and pw='2781';
update students set id='bbb',name='유관순',gender='F' where id='Zaccaria';
update students set id='ccc',name='이순신',gender='M' where id='Ferguson';
update students set id='ddd',name='강감찬',gender='M' where id='Alma';
update students set id='eee',name='김구',gender='M' where id='Rhodie';
update students set id='fff',name='김유신',gender='M' where id='eee' and pw='3447';
update students set id='ggg',name='홍길자',gender='F' where id='Mendie' and pw='2029';
update students set id='hhh',name='홍길순',gender='F' where id='Alan' and pw='2225';

commit;

select count(*) from students;

alter table students add no number(38);

insert into students(no) select no from stu_score; 

select * from students;

update students b set no = (select rnum from(select rownum rnum,id from students) a)
where a.id = b.id
;

select rnum from(
select rownum rnum,a.* from students a);

--drop table students;
--drop table stu_score;

-- 2개 테이블 join - 1ro
-- 동일한 컬럼은 중복이 없어야 함. 2개 중 하나 테이블에서는 primary key를 가지고 있어야함
select a.id, a.name, phone, total, avg from students a, stu_score b
where a.id = b.id
order by name;

-- self join
-- 동일한 테이블 2개를 가지고 서로 join
select a.employee_id, a.department_id, a.job_id, a.manager_id, b.emp_name 
from employees  a, employees b
where a.manager_id = b.employee_id
order by department_id;

desc stu_score;  -- no 있음
desc students;   -- no 없음

--drop table students;
-- no 부여해서 새롭게 임포트

select * from students order by no;
select * from stu_score;

-- rank-> total 순으로 줄 세우기
select ranks from (select no, id, rank() over(order by total desc) as ranks, rank, total from stu_score) b
;
-- stu_score에 rank 부여하기
update stu_score a 
set rank=(select ranks from (select no, id, rank() over(order by total desc) as ranks
, rank, total from stu_score) b
where a.no = b.no )
;

select * from stu_score
order by rank;

--commit;

select * from member;
insert into member values ( member_seq.nextval,'iii',1111,'감찬스','남자',sysdate )
;
--commit;

select rownum rnum, id from member a;
alter table member add no number(38);

update member a
set no = (select rnum from (select rownum rnum, id from member) b 
where a.id = b.id);

-- rank, id 
select rownum rnum, id from member;
-- rnum
select rnum from (select rownum rnum, id from member) b
where id = b.id;

select * from member;

-------------------------------------------------------------------------------------------
select total, rank from stu_score
order by total desc;

--
select total, rank() over(order by total desc) ranks from stu_score;
select row_number() over(order by total desc) rnum, total from stu_score;

--  stu_score, rank 순위를 모두 update하시오. 
select total, rank() over(order by total desc) ranks from stu_score;

-- update 방법
update stu_score a
set rank = (select ranks from (select no, id, rank() over(order by total desc) as ranks
, rank, total from stu_score) b
where a.no = b.no);

select * from stu_score
order by rank;

--commit;

-- row_number() over()
select * from stu_score;

--
select * from (
select rownum rnum,a.* from
(select * from stu_score order by total desc) a)
where rnum >= 11 and rnum <= 20;


-- row_number() over를 사용하면, 번호 부여 한 번에 가능
select * from (
select row_number() over(order by total desc) rnum, a.* from stu_score a)
where rnum >= 11 and rnum <= 20
;

------------------------------------------------------------------------------------
select employee_id, emp_name, manager_id from employees
order by employee_id
;

-- self join manager_id,이름을 출력하시오
-- 값이 충족되지 않아도 출력되도록 outer join
-- null 값이 있는 반대편 항목에 (+)기호를 넣으면 됨
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b  -- self join
where a.manager_id = b.employee_id(+)
;
-- 오류 --
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b  -- self join
where a.manager_id(+) = b.employee_id
;
---------------------

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

-- equi join, outer join // 
-- outer join :  null값이 있는(데이터가 부족한) 반대편 항목에 (+)기호 넣어주기
select emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id(+) = b.department_id
order by b.department_id
;
-- employees 테이블에는 부서번호가 10~110 까지만 존재
-- departments 테이블에는 부서번호 10~270 까지 존재
-- employees에는 없는 부서번호도 부서명이 모두 출력되도록
select department_id from departments;

--------------------------------------------------------------------------------
-- ANSI join
select * from employees cross join departments;
select * from employees, departments; -- 두 코드는 동일한 출력물을 나타냄

select a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id
;

select a.department_id,department_name
from employees a inner join departments b
on a.department_id = b.department_id
;

-- ansi inner join - using
-- 공통적인 부분은 알아서 지정해서 가져옴
select employee_id, emp_name, department_id, department_name
from employees join departments
using (department_id)
;

-- equi join으로 가져오려면?
select a.*, department_name
from employees a, departments b 
where a.department_id = b.department_id
;

-- natural join
select * from employees natural join departments;

-- ansi outer join : left outer, right outer, full outer join
select * from employees a
left outer join employees b
on a.manager_id = b.employee_id;

-- 기본 sql: left outer, right join, full outer join 불가
select a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+);

--------------------------------------------------------------------------------
-- 공부
-- ansi inner join
select emp_name, a.department_id, department_name
from employees a inner join departments b
on a.department_id = b.department_id
;
-- oracle join
select emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;
----------------------------------------------------------
-- ansi outer join: 조인 테이블 값이 존재하지 않아도 메인 테이블의 데이터가 조회된다.
-- left outer join: 왼쪽 테이블이 메인
-- right outer join: 오른쪽 테이블이 메인
select emp_name, a.department_id, department_name
from employees a left outer join departments b
on a.department_id = b.department_id
;

-- oracle join
-- null값이 있는(데이터가 부족한) 반대편 항목에 (+)기호 넣어주기
select emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id(+) = b.department_id;
-----------------------------------------------------------
-- ansi cross join
-- : 두 테이블의 모든 데이터를 서로 한 번씩 조인을 한다고 생각함
----------------------------------------------------------
-- ansi full outer join
-- :
---------------------------------------------------------





-- 이름 검색
select * from stu_score 
where id like '%a%'
order by no;

select count(*) from stu_score where id like '%a%';

-- 10개씩 정보 가져올 수 있게 명령어
select rownum, a.* from stu_score a;

-- 이름에 a가 들어가는 학생 중 번호 부여 -> 10명씩 뽑아내기
-- 1) 이름에 a가 들어가는 학생 찾기
select * from stu_score where id like '%a%' order by no;
-- 2) 이들만 rownum을 부여해서 일렬로 나열
select rownum, a.* from (select * from stu_score where id like '%a%' order by no) a;
-- 3) rownum 별칭 지정 후 사용, 원하는 범위의 rnum 번호 호출
select rnum, no,id,kor,eng,math,total,avg,rank
from (select rownum rnum, a.* from (select * from stu_score where id like '%a%' order by no) a)
where rnum >= 11 and rnum <= 20
;
-- 4) 개수 : id에 a가 들어간 학생의 수 520명
select count(*) from (
select rnum, no,id,kor,eng,math,total,avg,rank
from (select rownum rnum, a.* from (select * from stu_score where id like '%a%' order by no) a)
);

--
select * from (select row_number() over(order by no) rnum, a.* 
from stu_score a where id like '%{search}%');


--------------------------------------------------------------------------
create table melon(
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number
);

create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);

--alter table melon modify img varchar2(500);
--alter table yanolja modify img varchar2(500);

