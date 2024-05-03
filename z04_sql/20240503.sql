--[ 1 ] 사원정보(Employees) 테이블에서
-- 사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하시오
-- 이때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오(107행)

select * from employees;
select * from departments;
select * from jobs;

select employee_id, emp_name, salary, department_name, hire_date, e.manager_id
from employees e, departments d, jobs j
;

select employee_id, emp_name||'_'||job_title as name, salary, department_name, e.manager_id
from employees e, departments d, jobs j
where e.department_id = d.department_id and e.job_id = j.job_id
order by salary desc;

--------------------------------------------------------------------------------------------------
-- [ 2 ] 사원정보(Employees) 테이블에서
-- 사원의 이름과 성은 Name, 업무는 Job, 급여는 Salary, 연봉에 $100 보너스를 추가하여
-- 계산한 값은 Increase Ann_Salary,
-- 급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오(107행)

select * from employees;

select emp_name name, job_title job, salary, (salary+100) "Increase Ann_Salary"
from employees e, jobs j
where e.job_id = j.job_id ;

------------------------------------------------------------------------------------------------
-- [ 3 ] HR 부서에서 예산편성문제로 급여 정보 보고서를 작성하려고 함
-- 사원정보(Employees) 테이블에서 급여가 $7000~$10,000 범위 이외인 사람의 이름과 성(Name으로 별칭) 및
-- 급여가 적은 순서로 출력

select * from employees;
desc employees;

select emp_name NAME, salary from employees
where salary > 10000 or salary < 7000
order by salary asc;

-----------------------------------------------------------------------------------------------
-- [ 4 ] 사원의 성(last_Name) 중에 'e' 및 'o' 글자가 포함된 사원을 출력하시오
-- 이때 머리글은 'e or o Name'이라고 출력하시오

select emp_name "e or o Name" from employees
where lower(emp_name) like '%e%' or lower(emp_name) like '%o%';

------------------------------------------------------------------------------------------------
-- [ 5 ] 이번 분기에 60번 IT부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다.
-- 이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 60번 IT 부서 사원의 급여를 12.3% 인상하여
-- 정수만(반올림) 표시하는 보고서를 작성하시오.
-- 보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력한다.

select employee_id, emp_name "Name", department_name, salary, 
case when department_name = 'IT' then round(salary*1.123,0)
else salary
end as "Increase Salary"
from employees e, departments d
where e.department_id = d.department_id;

----------------------------------------------------------------------------------------------
-- [ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 보고서에 사원의 이름과 성(Name), 급여, 수당여부에 따른
-- 연봉을 포함하여 출력하시오. 수당여부는 수당이 있으면 "Salary + Commission", 수당이 없으면 "Salary only"라고 표시
-- 별칭은 적절히 붙이기
-- 출력시, 연봉이 높은 수능로 정렬

select nvl(commission_pct,0) from employees;

-- 1)
select emp_name "Name", salary+(salary*nvl(commission_pct,0)) salary,
case 
when commission_pct is null then 'Salary only'
else 'Salary + Commission'
end as "S+C"
from employees
order by salary desc;

-- 2)
select emp_name "Name", salary+(salary*nvl(commission_pct,0)) salary,
decode( salary,  -- 해당하는 숫자만 가능, 범위 못씀
3000,'A',
4000,'B',
5000,'C') as dept
from employees
order by salary desc;

-- 3) nvl2
select emp_name "Name", salary+(salary*nvl(commission_pct,0)) salary,
nvl2(commission_pct,'Salary + Commission','Salary only') "S+C"
from employees
order by salary desc;

--------------------------------------------------------------------------------------------------
-- [ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최대값, 급여 최솟값을 집계하고자 한다.
-- 계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오.
-- 단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력시 머리글은 "그룹함수명"을 별칭(alias)처리하시오

select department_id from employees;

select department_name, count(department_name) count,
to_char(sum(salary),'$999,999,999') SUM, to_char(trunc(avg(salary),1),'$999,999') AVG,
to_char(max(salary),'$999,999') MAX, to_char(min(salary),'$999,999') MIN from employees e, departments d
where e.department_id = d.department_id(+)
group by department_name;



-------------------------------------------------------------------------------------------------
-- [ 8 ] 사원들의 직급별 전체 급여 평균이 $ 10,000보다 큰 경우를 조회하여 업무별 급여 평균을 출력하시오
-- 단. 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체급여 평균이 높은 순서대로 출력하시오

select job_title from jobs;

select job_title, avg(salary) from employees e, jobs j 
where not(job_title like '%CLERK%') and e.job_id = j.job_id
group by job_title;

-- where : 일반 컬럼의 조건을 넣는 곳
select * from 
(select job_title, avg(salary) avg from employees e, jobs j
where e.job_id = j.job_id 
group by job_title)
where avg > 10000 and not(job_title like '%CLERK%')
order by avg desc;

-- having :  그룹컬럼의 조건을 넣는 곳
select job_title, avg(salary) avg from employees e, jobs j
where e.job_id = j.job_id and not(job_title like '%CLERK%')
group by job_title
having avg(salary) > 10000
order by avg desc;

select job_id, avg(salary) from employees
where job_id not like '%CLERK%'
group by job_id
having avg(salary) > 10000;

----------------------------------------------------------------------------------------------------
-- [ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
-- 예) 홍길동은 허균에게 보고한다. -> 홍길동 report to 허균
-- 어떤 사원이 누구에게 보고하는 지 위 예를 참고하여 출력하시오. 단 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력
-- 상사의 이름과 성은 대문자로 출력

select b.employee_id, b.emp_name, b.manager_id, a.emp_name superior
from employees a, employees b
where a.employee_id(+) = b.manager_id  -- a가 b안으로 들어가는 것
;

select b.emp_name||' report to '||upper(a.emp_name) report
from employees a, employees b
where a.employee_id(+) = b.manager_id;

--------------------------------------------------------------------------------------------------------
-- [ 10 ] Employees, Departments 테이블의 구조를 파악한 후 사원 수가 다섯 명 이상인 부서의
-- 부서이름과 사원 수를 출력하시오. 이때 사원 수가 많은 순으로 정렬 하시오

select * from employees;
select * from departments;

select department_name, count(department_name) count
from employees e, departments d
where e.department_id = d.department_id
group by department_name
having count(department_name) >= 5
order by count desc;

-------------------------------------------------------------------------------------------------------
-- [ 추가 ] HR부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고있다.
-- 이름에 Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오
select salary from employees
where emp_name like '%Tucker%';  -- Tucker의 연봉은 10000

select emp_name, job_id, salary from employees
where salary > (select salary from employees
where emp_name like '%Tucker%')
;  -- 총 15명

-- 전체 평균월급 이상인 사원들 출력
select emp_name, salary from employees
where salary > (select avg(salary) from employees)
order by salary desc
;
-------------------------------------------------------------------------------------------------------
-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름, 업무,급여, 부서번호, 부서평균연봉을 출력
select emp_name name, job_id job, salary, department_id
from employees;

-- 부서별로 평균월급 구한거
select department_id, avg(salary) from employees
group by department_id;

-- equi-join 하면 된다!!
select emp_name name, job_id job, salary, e.department_id, "Department Avg Salary"
from employees e, 
(select department_id, round(avg(salary),1) "Department Avg Salary" from employees
group by department_id) a
where e.department_id = a.department_id
order by department_id;

-------------------------------------------------------------------------------------------------------

select emp_name from (select * from employees
where salary > (select avg(salary) from employees) )
where emp_name like '%a%';

select * from employees
where salary > (select avg(salary) from employees);

-------------------------------------------------------------------------------------------------------
alter table melon modify v_rank varchar(100);

create table daum_movie(
dno number,
title varchar2(100),
img varchar2(300),
viewer varchar2(100),
mdate date
);

alter table daum_movie modify viewer varchar(100);
alter table daum_movie modify img varchar(300);

insert into daum_movie values( daum_seq.nextval, 'test', 'test', '천만', to_date('20200115'));


select * from daum_movie;  -- 성공!!!

--drop table daum_movie ;

