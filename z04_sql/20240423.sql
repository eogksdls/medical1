-- <5�� ����>
select * from students;

--��������
select * from students
order by name asc;

--alter table students add rank number(3);

--update students set rank = 0;

--commit;

-----------------------------------------------------------
select total, rank() over(order by total desc) rank
from students;

update students set total = 0;
-- ��� total ���� 0

select * from students;

update students set total=(kor+eng+math);

--1. �⺻ ����:
-- update students as s1 set rank=()

--2. rank()����:
--(select no, rank() over(order by total desc) as ranks from students) s2;

update students s1 set rank=(select ranks from
(select no, rank() over(order by total desc) as ranks from students s2) 
where s1.no = s2.no);

select * from students;
commit;

--��������
select no,total,rank from students
order by total desc;

--��������
select no,total,rank from students
order by no;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

--�������� :  null���� ���� ���� ����
select manager_id from employees
order by manager_id  desc;

--��¥ �������� : ���� �ֽ� ��¥�� ���� ���´�
select hire_date from employees
order by hire_date desc;

select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

-------------------------------------------------------------------------
-- ����
-- �Ի��Ϸ� ��������, �÷� �����ȣ,�����,�μ���ȣ,����,�Ի���,���� ���
select * from employees;

select employee_id, emp_name, job_id, hire_date, salary from employees
order by hire_date asc;

--����2
--�޿��� ���Թ޴� ��� ������ ����ϵ�, ������ ������ ��������� ��������
select employee_id, emp_name, job_id, hire_date, salary from employees
order by salary asc, emp_name asc;

--------------------------------------------------------------------------
--�����Լ�
--abs: ����
select -10, abs(-10) from dual; --dual�� ���� ���̺�

--floor: �Ҽ��� ����
--round: �ݿø�
select 34.789, floor(34.789) as f, round(34.789) as r from dual;

--�Ҽ��� ��° �ڸ����� �ݿø�
select 34.178, round(34.178), round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;

--������ �����κ�
select 34.5678, round(34.5678,-1) from dual;

--trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.45678) from dual;

--�ø�
select ceil(34.123) from dual;

--������
select 10/7 from dual;
--mod: ������
select round(100/7,2) from dual;
select mod(10,7) from dual;

-------------------------------------------------------------------------
--����
--�������� �ϴ��� ���� ���
select trunc(kor,-1) kor from students
order by kor
;

--����, ����, ���� �ϴ��� �����ؼ� ������ �հ踦 ���
select trunc(kor,-1) "����", trunc(eng,-1) "����", trunc(math,-1) "����",
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) "�հ�" from students;

--�����ȣ�� ¦���� ���� ����Ͻÿ�: �������� 0�̸�
--���̽㿡�� employee_id%2 == 0
select employee_id from employees
where mod(employee_id,2) = 0;

--�� ���� �Ϸ���?
select floor(10/7) from dual;

--�й��� 3�� ����� �͸� ����Ͻÿ�: 3���� ������ ������ 0
select * from students
where mod(no,3) = 0;
---------------------------------------------------------------------------
---------------------------------------------------------------------------
-- <6��> ������ :  �⺻Ű ����!!
create sequence seq_no
    increment by 1 -- 1�� ������
    start with 1   -- 1���� ����
    minvalue 1     -- �ּڰ� 1
    maxvalue 9999  -- �ִ�
    nocycle        -- ��ȯ���� ����
    nocache       -- ĳ�û�� ����
;
--nextval ��������ȣ 1�� ����
select seq_no.nextval from dual;

--currval ������ ��ȣ Ȯ��
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
seq_mno.nextval, 'eee', '1111', '������','010-5555-5555'
);

select * from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;

-- '00000' �ڸ���
select 's'||trim(to_char(seq_mno.nextval,'00000')) from dual;
-----------------------------------------------------------------------
-- ����
-- �ѱ����б� ko20240001 �й� �����!
-- ������ seq_kono 1 - 9999 ����
create sequence seq_kono
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

select to_char(sysdate,'yyyy') from dual;

-- trim()�� ��������
select 'ko'||to_char(sysdate, 'yyyy')||trim(to_char(seq_kono.nextval,'0000')) as stuno from dual;

----------------------------------------------------------------------------------------------------

-- �Խ��� �����
create table board (
bno number(5) primary key,
bittle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10)
);

-- ����
-- ������  ����1001, ���� 10 1,99999
-- 5�� ����
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
emp_seq.nextval, '�̼���', sysdate
);
select * from emp01;

commit;
----------------------------------------------------------------------------
--���� : �ֱ� �Ի��� ������ ���� ���
select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

-- ������� �Ի��� �ϼ��� �Բ� ����ϼ���
select employee_id, emp_name, job_id, hire_date, ceil(sysdate - hire_date)||'��' as "�ټӱⰣ" from employees
order by �ټӱⰣ desc;

select emp_name from employees;
-- ���ް� ����� ���ļ� ����Ͻÿ�..
select job_id||employee_id from employees;

----------------------------------------------------------------------------
-- substr: ���ڿ� �߶���� �Լ�, substr(���,������ġ,����)
select substr(job_id,0,2) from employees;
select emp_name, substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;


-- ����
-- job_id �տ� 2�����ڿ� ��� 5�ڸ� 00001�� ����� �Բ� ���
select substr(job_id,1,2)||trim(to_char(employee_id,'00000')) as emp_no from employees
order by emp_no
;
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- ��¥ �Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

-- ����-�Ի��� ������ ���� �� Ȯ�� : �� ���� / �� ��
select round(MONTHS_BETWEEN(SYSDATE,hire_date),0), sysdate-hire_date from employees;

--���� ���� �߰�( 2���� �ĸ� ��Ÿ����)
select sysdate, add_months(sysdate,2) from dual;

--next_day :  ���縦 ���������� �����ϴ� ������ ������ ���� ���� �� �˷���
select next_day(sysdate,'������') from dual;

-- ���縦 �������� �� ������ �˷���
select last_day(sysdate) from dual;
select last_day('2024-02-01') from dual;
