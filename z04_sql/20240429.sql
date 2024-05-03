--drop table board cascade constraints;


--무결성 제약조건 :  부적합한 자료가 입력되지 않도록 하기 위한 규칙
-- not null, unique, primary key, foreign key, check
-- 테이블 생성
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('남자','여자')),
mdate date default sysdate
);

-- 데이터 입력, 출력, 수정, 삭제 부분
insert into member (memNo,id,pw,name,gender,mdate) values(
member_seq.nextval, 'aaa','1111','홍길동','남자',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','유관순','여자'
);

insert into member values(
member_seq.nextval,'ccc','1111','이순신','남자',sysdate
);

select * from member;
----------------------------------------------------------------------------
-- 테이블 생성 :  게시판 테이블 구조
create table board(
bno number(4) primary key,
id varchar2(30),  --외래키 등록
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- 외래키(foreign key)의 별칭: fk_id
references member(id) -- member 테이블의 primary key id 

);

insert into board(bno, id, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values (
board_seq.nextval,'aaa','제목입니다.','내용입니다.',sysdate, board_seq.currval,0,0,1,''
);

insert into board values(
board_seq.nextval,'bbb','제목입니다2.','내용입니다2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bno, id, btitle, bcontent, bgroup) values(
board_seq.nextval,'aaa','제목입니다3.','내용입니다3.',board_seq.currval
);
--primary key를 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제를 모두해야 함.
--primary key가 삭제되면 모두 삭제하는 방법 - on delete cascade, 모두 존재하는 방법 on update cascade 이 있다.

select * from  board;

-- 삭제
--delete board where bno=3;

commit;

delete member where id='aaa';

---------------------------------------------------------------------------------
-- 논리연산자 이용
-- [ DECODE 조건문 ]
select emp_name, department_id,
decode(department_id,
10,'총무기획부',
20, '마케팅',
30, '구매/생산부',
40, '인사부'
)as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;
-- 90점 -A, 80점 -B, 70점 -C : ~점 이상 성적을 주는 것이 아닌, 딱 90점, 80점 이렇게 점수를 부여할 수 있다는 한계점
select name, avg,
decode(avg,
90,'A',
80, 'B',
70, 'C'
)as grade
from stu_score order by avg desc;

select job_id, salary from employees;
-- clerk salary * 15%, asst * 10% rep * 5%, man * 2%;
select job_id, salary,
decode(job_id,
'SH_CLERK', salary+(salary*0.15),
'AD_ASST', salary+(salary*0.10),
'MK_REP', salary+(salary*0.05)
) as salaryUp
from employees order by salaryUp;

-- job_id에 clerk이 들어가 있는 job_id를 검색하시오!
select job_id, emp_name, salary from employees
where job_id like '%CLERK%';

-----------------------------------------------------------------------------------------
-- 논리연산자 이용
-- [ CASE  조건문 ]
select name, avg,
case when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id, department_name from departments;

select department_id from employees
order by department_id asc;

-- case 구문을 사용해서 department_id, name을 출력해보세요
select department_id,
case when department_id = 10 then '총무기획부'
when department_id = 20 then '마케팅'
when department_id = 30 then '구매/생산부'
when department_id = 40 then '인사부'
when department_id = 50 then '배송부'
when department_id = 60 then 'IT'
when department_id = 70 then '홍보부'
when department_id = 80 then '영업부'
when department_id = 90 then '기획부'
when department_id = 100 then '자금부'
when department_id = 110 then '경리부'
end as depart_name
from employees;

-- clerk포함 salary * 15%, ad_asst * 10% rep * 5%, man * 2%;
select job_id, emp_name, salary,
case when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id = 'AD_ASST' then salary+(salary*0.10)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
end as salaryUp
from employees
order by salaryUp asc;

-- 월급이 평균 이하 : salary * 0.15, 평균이상: salary * 0.05 인상해서 출력하시오
select avg(salary) from employees; -- 6461.xxxx

select job_id, emp_name, salary,
case when salary < (select avg(salary) from employees) then salary+(salary*0.15)
when salary >= (select avg(salary) from employees) then salary+(salary*0.05)
end as salaryUp,
case when salary < (select avg(salary) from employees) then 'DOWN'
when salary >= (select avg(salary) from employees) then 'UP'
end as salary_UpDown
from employees
order by salary asc;

--------------------------------------------------------------------------------------
-- 성적순으로 등수 매기기
select total, rank from stu_score
order by total desc
;

--rank() 함수
select total, rank() over (order by total desc) as ranks
from stu_score;

select * from stu_score;

update stu_score set rank = 1
where total = 291;
--------------------------
update stu_score a
set rank = (
select ranks from(
select no,rank() over (order by total desc) as ranks from stu_score
) b
where a.no = b.no
)
;

commit;

select * from stu_score
order by rank;
----------------------------
---------------------------------------------------------------------------------------

-- 두 개 테이블 조인
select emp_name, department_id from employees;
select department_id, department_name from departments
;

select emp_name, employees.department_id, department_name from employees,departments
where employees.department_id = departments.department_id;


-- 두 테이블 조인해서 출력
select a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id
;

-----------------------------------------------------------------------------------------
-- 그룹 함수 sum, avg, count, max, min, stddev 표준편차, variance 분산
-- 월급 총합
select sum(salary) from employees;
-- 사원 수
select count(*) from employees;

select count(*) from employees
where department_id = 50
;

-- 퀴즈
-- 커미션을 받는 사원의 수를 구하시오
select count(*) from employees
where commission_pct is not null;
-- 커미션이 있는 사원을 검색하시오.
select emp_name, commission_pct from employees
where commission_pct is not null;

----------------------------
select employee_id from employees;
select employees.employee_id from employees,departments;

-- 부서번호가 50번인 사원 수 구하기
select * from employees;
select count(*) from employees
where department_id = 50;

------------------------------
-- 부서별 그룹지어 사원수 출력
select department_id, count(department_id) from employees
group by department_id
order by department_id
;

-- column명 grade
-- stu_score에서 90점 이상 A, 80점이상 B, 70점 이상 C, 60점 이상 D, 60점 미만 F
select avg,
case when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

-- 성적별 학생 수 구하기
select grade,count(*) from (
select avg,
case when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade 
from stu_score
)
group by grade
order by grade
;
-- A: 53명, B: 223명, C: 444명, D: 245명, F: 35명

--확인해보기
select avg from stu_score
where avg >= 60 and avg < 70;

-----------------------------------
-- trunc 함수를 사용하여 국어점수가 90점대, 80점대,... 점수별 학생수
select trunc(kor,-1) from stu_score;
select grade, count(grade) from (
select case
when trunc(kor,-1) = 100 then '100'
when trunc(kor,-1) = 90 then '90'
when trunc(kor,-1) = 80 then '80'
when trunc(kor,-1) = 70 then '70'
when trunc(kor,-1) = 60 then '60'
when trunc(kor,-1) < 60 then '미달'
end as grade
from stu_score
)
group by grade
order by grade desc
;

-- 또는
select k_kor, count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor
;

--그룹함수 group by 사용
select department_id, count(*) from employees
group by department_id
order by department_id;

select emp_name, count(emp_name) from employees
group by emp_name;

------------------------------------------
-- 부서별 평균 월급을 구하시오
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id
;

--CLERK이 포함되어 있는, MEP이 포함된, MAN이 포함된 월급 평균을 구하시오.
select job, count(job), round(avg(salary),1) sal_avg
from (select job_id, salary,
case when job_id like '%CLERK%' then 'CLERK'
when job_id like '%REP%' then 'REP'
when job_id like '%MAN%' then 'MAN'
else 'EX'
end as job
from employees) 
group by job
order by job;

select job_id, avg(salary), count(job_id) from employees
group by job_id;

-- 부서별(group by department_id) 최대월급, 최소월급, 평균월급을 출력하시오
select department_id, max(salary), min(salary), round(avg(salary),1) avg from employees
group by department_id;

------------------------------------------------
-- 부서별 커미션을 받는 사원 수를 출력하시오
select department_id,count(department_id),count(commission_pct) from employees
group by department_id;

-------------------------------------------------------------------------------------------
-- having, group by 조건절, where 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

-- emp_name의 두 번째 글자가 a로 시작하는 것은 제외
select department_id, round(avg(salary),2) 
from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- 전체부서 평균월급보다 낮은 부서의 평균월급 출력
select department_id, round(avg(salary),2) 
from employees
group by department_id
having avg(salary) < (select avg(salary) from employees)
order by avg(salary);


-- 부서별 최대월급이 8천 이상인 부서만 출력
select department_id, max(salary) 
from employees
group by department_id
having max(salary) > 8000
order by max(salary);

--------------------------------------------------------------------------------------------
-- 조인 

select emp_name,department_id,departmentent_name, salary from employees;

select count(*) from employees; --107개
select count(*) from departments;  --27 개 

select department_id,department_name from eomployees;

select * from employees,departments;

-- 테이블 2개를 연결한 것을 조인이라고 함
-- 107*27 = 2889
select count(*) from employees, departments;

-- equi join
--: 조인 대상이 되는 두 테이블에서 공통적으로 존재하는 컬럼의 값이 일치되는 행을 연결하여 결과 생성
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id
;

select department_id,department_name from departments;

--------------------
 select * from member;
 select * from board;

-- board 테이블에 id와 name을 넣고 싶을때
select id,name from member;
select id,name from member;
select id,btitle,bcontent from board;

update member set name='홍길자'
where id = 'aaa';

select bno,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board, member
where member.id = board.id
;
-- member의 이름이 변경되어도 id는 동일하기 때문에 동시 변경 가능

------------------------------------------------------------------------------------

