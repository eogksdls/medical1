select * from stu_score;

select * from stu_score
where name like '%a%'
order by no;

select * from board;

select a.*, name from board a,member b
where a.id = b.id;

select bno, a.id, name, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile
from board a, member b
where a.id = b.id
;

select * from employees;

select no,name,total,avg,
case when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

select job_id,avg(salary) from employees
group by job_id;

select * from employees;

select employee_id,emp_name,salary,(salary+(salary*nvl(commission_pct,0))) real_sal, to_char(salary*1410,'L999,999,999') kor_sal from employees
;

select job_id, avg(salary), max(salary), min(salary) from employees
group by job_id;
---------------------------------------------------------------------------
-- 찾고자하는 학생의 이름 검색
select * from stu_score
order by no;

--update stu_score set name = '관순스'
--where no = 10;
--
--commit;

-- 홍 이라고 검색하면 글자가 포함된 이름을 가진 학생을 모두 출력하시오
select * from stu_score
where name like '%홍%';

--평균 점수 이상의 학생들 출력
select * from stu_score
where avg > (select avg(avg) from stu_score)
;

-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오
select employee_id, emp_name, e.department_id, department_name, salary
from employees e,departments d
where e.department_id = d.department_id and emp_name like '_a%' 
and salary > (select avg(salary) from employees)
;

-- 그리고, 이름 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%';

-- 월급이 평균 이상인 사람만 검색
select * from employees
where salary > (select avg(salary) from employees)
;

select * from employees;

select * from jobs;

--사원 번호, 사원명, 부서번호, 부서명, 직급번호, 직급명 출력 
select employee_id, emp_name, e.department_id, department_name, e.job_id, job_title
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id
order by employee_id
;

select * from jobs;

-- 사원번호, 사원명, 월급, 최소월급분, 인상분, 직급, 직급타이틀을 출력하시오
-- 최소 월급 몇 % 이상을 받고 있는 지 출력(min_salary / salary) *100
select employee_id, emp_name, e.salary, min_salary, to_char(round((salary-min_salary)/min_salary*100,2)||'%') percent_sal, e.job_id, job_title
from employees e, jobs j
where e.job_id = j.job_id
;

-- job_title Manager 글자가 들어가 있는
-- 사원 번호, 사원명, 직급번호, 직급명, 월급, 최대월급을 출력하시오
select employee_id, emp_name, e.job_id, job_title, salary, max_salary
from employees e, jobs j
where e.job_id = j.job_id and job_title like '%Manager%'
order by employee_id
;

-- job_id 별로 평균 연봉 구하기
select job_id, avg(salary) from employees
group by job_id
order by avg(salary) desc;

-- jobs에서 최대, 최소 월급의 중앙값을 구하시오
select employee_id, emp_name, e.job_id, job_title, max_salary, min_salary, (max_salary+min_salary)/2 mid_salary
from employees e, jobs j
where e.job_id = j.job_id
order by employee_id
;

------------------------------------------------------------------------------------------------
create table stu_grade (
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A', 90,100
);
insert into stu_grade values(
'B', 80,89
);
insert into stu_grade values(
'C', 70,79
);
insert into stu_grade values(
'D', 60,69
);
insert into stu_grade values(
'F', 0,59
);
commit;
select * from stu_grade;

select avg from stu_score;

--case when then grade 컬럼 적용
select no,name,round(avg,1) avg,
case 
when round(avg,1) >= 90 then 'A'
when round(avg,1) >= 80 then 'B'
when round(avg,1) >= 70 then 'C'
when round(avg,1) >= 60 then 'D'
else 'F'
end as grade
from stu_score
order by no
;

------------------------------------------------------------------
update stu_grade set low_score=92
where grade = 'A';

update stu_grade set low_score=62, high_score=71
where grade = 'D';

update stu_grade set high_score = 61
where grade = 'F';

select * from stu_grade;

--non-equi join
-- 둘이 동일한 컬럼이 존재하지 않을 때 사용
select no,name,round(avg,1) avg,grade
from stu_score, stu_grade
where avg between low_score and high_score  -- stu_grade의 점수 범위 적용
order by no
;

commit;

--월별 매출액 기준으로 고객등급을 매기려고 함
-- 지역별 대출 합계를 출력하시오
select * from kor_loan_status;
select region, gubun, to_char(round(sum(loan_jan_amt),0),'L999,999,999') s from kor_loan_status
group by region,gubun
order by region
;

--부서별 월급 합계를 출력하시오
select department_id, sum(salary) a from employees
group by department_id
order by a
;

-- 연도별, 지역별, 대출합계금액
select * from kor_loan_status;
select substr(period,0,4) year, region, to_char(round(sum(loan_jan_amt)*1383,0),'L999,999,999,999') sum from kor_loan_status
group by substr(period,0,4),region
order by region
;

select substr(period,0,4) from kor_loan_status;

-----------------------------------------------------------------------------------------------
-- 새로운 데이터 임포트
-- 시간대별,연령대별 판매량 총합을 구하시오
select * from lotte_product;
select time_cd, age_cd, to_char(sum(purh_amt),'L999,999,999') sum from lotte_product
group by time_cd, age_cd
order by sum desc
;

---------------------------------------------------------------------------------------------
-- 새로운 데이터 임포트 (shop_product)
select * from shop_product;

-- 이름별, 판매금액 합계를 출력
select name, to_char(sum(amount),'999,999,999') sum from shop_product
where pdate >= '2024/03/01'
group by name
order by sum desc
;

-- customer_rank 테이블 생성
create table customer_rank(
amount_low number(10),
amount_high number(10),
rank varchar2(10)
);

insert into customer_rank values(
3000000,1000000000,'PLATINUM'
);

select * from customer_rank;

--commit;

select * from shop_product;

-- name, sum(amount), rank 출력하시오
-- non-equi join 으로 처리
select name,to_char(s_amount,'999,999,999') 금액,rank
from (select name, sum(amount) s_amount from shop_product group by name), customer_rank
where s_amount between amount_low and amount_high
order by name
;

select name, to_char(sum(amount),'999,999,999') s_amount
from shop_product
group by name
order by name
;

--- 최종 ---
select name, to_char(s_amount,'999,999,999') 금액, rank
from (select name, sum(amount) s_amount from shop_product where pdate >= '2024/03/01' group by name), customer_rank
where s_amount between amount_low and amount_high
;

-----------------------------------------------------------------------------------------------------
select * from lotte_product
order by std_ym
;

-- 순번을 새롭게 부여해서 출력해주는 함수
-- rownum, row_number()
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product
;

-- rownum이 10 이하인 데이터만 출력하기
select rownum, a.*
from (select * from lotte_product order by std_ym) a
where rownum <= 10
;

-- rownum이 10 이상 20 미만인 데이터 출력하기 // 불가능
-- 데이터가 모두 출력되고 나서 rownum을 부여하기 때문!!
select rownum, a.*
from (select * from lotte_product order by std_ym) a
where rownum >= 1 and rownum < 20
;

-- 미리 rownum을 부여한 것을
select rownum rnum, a.* from (select * from lotte_product order by std_ym) a;

-- from 자리에 넣어준다
select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from
(select rownum rnum, a.* from (select * from lotte_product order by std_ym) a) b
where rnum >=11 and rnum <=20 ;

-------------------------------------------------------------------------------
select * from stu_score
order by no;

-- kor 점수가 높은 순으로 21-30등까지 출력하시오
-- rownum 국어점수 순으로 먼저 부여해주기
select rownum, a.* from (select * from stu_score order by kor desc) a ;

-- from 자리에 저 위 코드를 넣어주고 rownum에 별칭 rnum을 지정
-- 원하는 rnum 데이터 범위에 따라 출력 가능
select rnum,no,name,kor,eng,math,total,round(avg,1) avg,rank
from
(select rownum rnum, a.* from (select * from stu_score order by kor desc) a)
where rnum >= 21 and rnum <= 30
;

-------------------------------------------------------------------------------
-- 국어, 영어 점수가 높은 순으로 31-40등까지 출력
select rownum, a.* from (select * from stu_score order by kor desc, eng desc) a; 

select rnum,no,name,kor,eng,math,total,round(avg,1) avg, rank
from (select rownum rnum, a.* from (select * from stu_score order by kor desc, eng desc) a)
where rnum >= 31 and rnum <= 40
;
