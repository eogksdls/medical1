-- ����,����,����
select sysdate-1, sysdate, sysdate+1 from dual;

-- ����, �̴��� ù��, �̴��� ��������
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;

-- �� ��¥�� �ϼ�
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date)) from employees;

-- trunc �ϴ��� ����, group by �׷��Լ�
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;

-- ����, hire_date ��¥���� ���� ����Ͻÿ�
-- 2008-01-01 ��������
select to_char(hire_date,'month') month, count(to_char(hire_date,'month')) count from employees
group by to_char(hire_date,'month')
order by month;

-- ����, hir_date 2008�⵵, �⵵�� �ο����� ����Ͻÿ�.
select to_char(hire_date,'yyyy') year, count(to_char(hire_date,'yyyy')) count from employees
group by to_char(hire_date,'yyyy')
order by year;

------------------------------------------------------------------------------------------------
-- ����ȯ -> number, character, date
-- number ��Ģ���� ����, ��ǥǥ�ô� �Ұ���, ��ȭǥ�õ� �Ұ���
-- char ��Ģ����(+,-) �ȵ�, ��ǥ ǥ�� ����, ��ȭǥ�� ����
-- date +,- ���� ��¥ ������´� ����Ұ� -> to_char�� ����ȯ�� ���־�� �Ѵ�.!!


-- ������, ��¥�� �⵵�� ������ �й��� �ο��Ϸ��� ��
--ko20240001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) stu_no from dual;

--drop table stu_no;

-- ������ Ÿ�� ����
-- ������� : 123,556,789
select replace('123,456,789',',',''), replace('100,000',',','') from dual;
select to_char(to_number(replace('123,456,789',',',''))+
to_number(replace('100,000',',','')),'999,999,999') sum from dual;

select to_char(to_number('123,456,789','999,999,999')-to_number('100,000','999,999'),'999,999,999') from dual;

---------------------------------------------------------------------------------------------------
-- ����Ÿ���� ��¥Ÿ������ ����
select 20240425 from dual;
select to_char(20240425+3) from dual;
select to_date(20240425+3) from dual;

-- ����Ÿ���� ��¥Ÿ������ ����
select emp_name, hire_date from employees
where hire_date > to_date(20070101)
order by hire_date;

-- ����: 08���� �Ի��� ��� �̸�, 2��°�� a�� �� �ִ� ����� ����Ͻÿ�.
select emp_name, hire_date from employees
where to_char(hire_date,'mm') in ('08','05','01') and emp_name like '_a%'
order by hire_date;

-- ����: 20070101 ���� �Ի��� ����̸�, 2��°�� a�� �� �ִ� ����� ����Ͻÿ�.
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

-- �Է½� ��¥Ÿ�Կ� ����(����-��¥����)�� �Է��ص� �����.
-- ��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ� ��.
insert into eventDate values(
seq_mno.nextval, sysdate, '2024-02-01', trunc(sysdate-to_date('2024-02-01'),0)
);

select * from eventDate;

-----------------------------------------------------------------------------
-- ����Ÿ���� ����Ÿ������ ����
select to_number('20,000','999,999')-to_number('10,000','999,999') from dual;

-- null�� 0���� ġȯ nvl()
select salary, salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

------------------------------------------------------------------------------
-- �׷��Լ� :  sum, avg, count(), count(*), min, max
-- �Ϲ� ���� ��ȸ�� �׷��Լ��� ������ select�� ���� �� �� ����.

-- count �Լ� -> number ����
select count(*) from employees; --��� �÷��� ���� ī��Ʈ ���ش�.(107��)
select count(emp_name) from employees; -- (107��)
select count(manager_id) from employees; -- null���� count�� �ȵȴ�.(106��)


select emp_name,manager_id from employees;

-- sum : ����
select sum(salary) from employees;

-- avg : ���
select avg(salary) from employees;
-- ��պ��� ������ ���� ����� ����Ͻÿ�
select emp_name, salary from employees
where salary > (select avg(salary) avg_sal from employees)
order by salary;

-- min: �ּڰ�, max: �ִ�
select min(salary), max(salary) from employees;
--�ּҿ����� �޴� ����� ���, �̸��� ����Ϸ���?
select employee_id, emp_name, salary from employees
where salary = (select min(salary) from employees);
-- �ִ� ������ �޴� ����� ���, �̸� ���
select employee_id, emp_name, salary from employees
where salary = (select max(salary) from employees) ;

-- �μ���ȣ�� 50���� ����� ��ü ���� �հ踦 ���� ����
select department_id, salary from employees;

select sum(salary) from employees
where department_id = 50;

-- ���� : kor ������ 80�� �̻��� �л��� ����Ͻÿ�
select * from stu_score;
select no, name, kor from stu_score
where kor > 80;

-- ���� : �������� ����̻�, �������� ����̻��� �л��� ����ϼ���
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

-- ����. �������� �ְ����� �л�, �������� �ְ����� �л�, �������� �ְ����� �л� ���
select name, kor, eng, math from stu_score
where kor = (select max(kor) from stu_score) 
or eng = (select max(eng) from stu_score)
or math = (select max(math) from stu_score)
order by kor desc, eng desc, math desc;
--------------------------------------------------
-- ����. ������ �ִ�, �ּ�, ����� ����� ����Ͻÿ�
-- ��պ��� ���� ��
select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc;

select avg(salary) from employees; -- ��� : 6461.83177....

-- ��պ��� ���� ����� �� ������ �ִ밪 ã�� : 6400
select max(salary) from (select emp_name, salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc)
;

-- �Ǵ� ��պ��� ���� ����� �� ������ �ּҰ� ã�� : 
select min(salary) from (select emp_name, salary from employees
where salary >= (select avg(salary) from employees)
order by salary desc)
;

-- �����ϱ�
select emp_name, salary from employees
where salary = (select max(salary) from employees)
or salary = (select min(salary) from employees)
or salary = (select max(salary) from (select emp_name, salary from employees
                                      where salary <= (select avg(salary) from employees)
                                      order by salary desc));

-----------------------------------------------------------
----------------------------------------------------------------------------------
-- �����Լ�
-- lpad(����), rpad(������) ����� ä���
select emp_name, lpad(emp_name, 15, '#') from employees;
select emp_name,rpad(emp_name, 20, '@') from employees;

-- ltrim(����), rtrim(������) ������ ���ڸ� �߶󳻰� ���
select emp_name, ltrim(emp_name,'Do') from employees;

-- ko20240001
select 'ko20240001', ltrim('ko20240001','ko2024') from dual;

--substr(������, ����, ����)
select emp_name, substr(emp_name,3,4) from employees;

select job_id, employee_id from employees;

-- ����. job_id�� �ִ� SH�� �����ȣ�� �����ؼ� ����Ͻÿ�
select emp_name, substr(job_id,0,2)||employee_id from employees;

------------------------------------------------------------------------
-- length
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

-- ��¥�Լ� +,- ����, ������ ��¥�����ͳ��� ���ϱ�(+)�� �Ұ���
-- ��¥ ������ + ���� ����
select sysdate+1 from dual;

-- ��¥ ������ - ��¥ ������ ����
select sysdate - hire_date from employees;

-- ��¥ ������ + ��¥������ �Ұ���
select sysdate + hire_date from employees;

-- ���� �������� �ݿø�
select round(sysdate,'month') from dual;

-- trunc: ����, round: �ݿø� => �ڸ��� ���� ����
select sysdate, trunc(sysdate,'month'), round(sysdate,'month') from dual;

-- ���� �������� �ݿø�
select round(sysdate,'year') from dual;

-- ���� �� ���ϱ�
select sysdate, add_months(sysdate,3) from dual;

-----------------------------------------------------------------------------
-- ceil: �ø�, floor: ����, mod: ������, power: ����
select ceil(-4.2), floor(-4.2), mod(8,3), power(3,2) from dual;

--���� 
--" �̸� 1979�� 09�� 19�� ������" ���·� ��ȸ
select concat(emp_name,to_char(hire_date,'  yyyy"��" mm"��" dd"��" day')) from employees;

-- ����. �����, ����*1400 �տ� ��ȭǥ�ÿ� ��ǥ�� �־��ּ���
-- ������� 0���� ǥ��
select emp_name, to_char(salary*1400,'L00,000,000') from employees;
-- ����ǥ��
select emp_name, to_char(salary*1400,'L999,999,999') from employees;

-- �ڽ��� ���ϰ� �ڽ��� ���� ���� ���� ������ ��¥�� ����ϼ���
-- '2010-10-10' �̰��� ����.
select to_char(trunc(to_date('2010-10-10'),'month'),'yyyy-mm-dd') m_firstday,to_char(to_date('2010-10-10'),'yyyy-mm-dd') birthday,
to_char(last_day('2010-10-10'),'yyyy-mm-dd') m_lastday from dual;

----------------------------------------------------------------------------------------------
select * from member;

desc member;

-- DDL(data definition language) 

-- column �߰�, ����, ����
-- default: female, null�� ������� ����
-- �� commit, rollback�� �ȵ� => �ٷ� ����ȴ�.
alter table member add gender varchar2(6) default 'female' not null; 

-- �÷� ����
--alter table member drop column phone;

-- �÷� ���� -> �÷� �̸�, Ÿ�Ժ��� ����
alter table member rename column name to stu_name
;
desc member;

-- Ÿ�� ����
alter table member modify(stu_name varchar2(50));
alter table member modify(stu_name varchar2(3)); -- �Ϻΰ��� �ʹ� Ŀ�� �� ���̸� ���� �� ����
--> ������ �����Ͱ� �����Ϸ��� ũ�⺸�� ���� ���� ������
-- ������� �÷��� Ÿ���� �����Ϸ��� �÷������Ͱ� ������̰ų�, update member set stu_name=" "
-- null�� �� �����ϴ�
alter table member modify(stu_name number(100)); -- ��ġ�� ���� ����(38�ڸ� �̳�)�� �ʰ��߽��ϴ�

desc member;

select * from member;

update member set gender = 'male';

commit;



