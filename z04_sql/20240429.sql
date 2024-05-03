--drop table board cascade constraints;


--���Ἲ �������� :  �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
-- ���̺� ����
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

-- ������ �Է�, ���, ����, ���� �κ�
insert into member (memNo,id,pw,name,gender,mdate) values(
member_seq.nextval, 'aaa','1111','ȫ�浿','����',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','������','����'
);

insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

select * from member;
----------------------------------------------------------------------------
-- ���̺� ���� :  �Խ��� ���̺� ����
create table board(
bno number(4) primary key,
id varchar2(30),  --�ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī: fk_id
references member(id) -- member ���̺��� primary key id 

);

insert into board(bno, id, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile) values (
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate, board_seq.currval,0,0,1,''
);

insert into board values(
board_seq.nextval,'bbb','�����Դϴ�2.','�����Դϴ�2.',sysdate, board_seq.currval,0,0,1,''
);

insert into board(bno, id, btitle, bcontent, bgroup) values(
board_seq.nextval,'aaa','�����Դϴ�3.','�����Դϴ�3.',board_seq.currval
);
--primary key�� �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 ������ ����ؾ� ��.
--primary key�� �����Ǹ� ��� �����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� on update cascade �� �ִ�.

select * from  board;

-- ����
--delete board where bno=3;

commit;

delete member where id='aaa';

---------------------------------------------------------------------------------
-- �������� �̿�
-- [ DECODE ���ǹ� ]
select emp_name, department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20, '������',
30, '����/�����',
40, '�λ��'
)as depart_name
from employees
order by department_id asc;

select * from stu_score order by avg desc;
-- 90�� -A, 80�� -B, 70�� -C : ~�� �̻� ������ �ִ� ���� �ƴ�, �� 90��, 80�� �̷��� ������ �ο��� �� �ִٴ� �Ѱ���
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

-- job_id�� clerk�� �� �ִ� job_id�� �˻��Ͻÿ�!
select job_id, emp_name, salary from employees
where job_id like '%CLERK%';

-----------------------------------------------------------------------------------------
-- �������� �̿�
-- [ CASE  ���ǹ� ]
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

-- case ������ ����ؼ� department_id, name�� ����غ�����
select department_id,
case when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then '����/�����'
when department_id = 40 then '�λ��'
when department_id = 50 then '��ۺ�'
when department_id = 60 then 'IT'
when department_id = 70 then 'ȫ����'
when department_id = 80 then '������'
when department_id = 90 then '��ȹ��'
when department_id = 100 then '�ڱݺ�'
when department_id = 110 then '�渮��'
end as depart_name
from employees;

-- clerk���� salary * 15%, ad_asst * 10% rep * 5%, man * 2%;
select job_id, emp_name, salary,
case when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id = 'AD_ASST' then salary+(salary*0.10)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
end as salaryUp
from employees
order by salaryUp asc;

-- ������ ��� ���� : salary * 0.15, ����̻�: salary * 0.05 �λ��ؼ� ����Ͻÿ�
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
-- ���������� ��� �ű��
select total, rank from stu_score
order by total desc
;

--rank() �Լ�
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

-- �� �� ���̺� ����
select emp_name, department_id from employees;
select department_id, department_name from departments
;

select emp_name, employees.department_id, department_name from employees,departments
where employees.department_id = departments.department_id;


-- �� ���̺� �����ؼ� ���
select a.department_id, department_name from employees a, departments b
where a.department_id = b.department_id
;

-----------------------------------------------------------------------------------------
-- �׷� �Լ� sum, avg, count, max, min, stddev ǥ������, variance �л�
-- ���� ����
select sum(salary) from employees;
-- ��� ��
select count(*) from employees;

select count(*) from employees
where department_id = 50
;

-- ����
-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�
select count(*) from employees
where commission_pct is not null;
-- Ŀ�̼��� �ִ� ����� �˻��Ͻÿ�.
select emp_name, commission_pct from employees
where commission_pct is not null;

----------------------------
select employee_id from employees;
select employees.employee_id from employees,departments;

-- �μ���ȣ�� 50���� ��� �� ���ϱ�
select * from employees;
select count(*) from employees
where department_id = 50;

------------------------------
-- �μ��� �׷����� ����� ���
select department_id, count(department_id) from employees
group by department_id
order by department_id
;

-- column�� grade
-- stu_score���� 90�� �̻� A, 80���̻� B, 70�� �̻� C, 60�� �̻� D, 60�� �̸� F
select avg,
case when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score;

-- ������ �л� �� ���ϱ�
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
-- A: 53��, B: 223��, C: 444��, D: 245��, F: 35��

--Ȯ���غ���
select avg from stu_score
where avg >= 60 and avg < 70;

-----------------------------------
-- trunc �Լ��� ����Ͽ� ���������� 90����, 80����,... ������ �л���
select trunc(kor,-1) from stu_score;
select grade, count(grade) from (
select case
when trunc(kor,-1) = 100 then '100'
when trunc(kor,-1) = 90 then '90'
when trunc(kor,-1) = 80 then '80'
when trunc(kor,-1) = 70 then '70'
when trunc(kor,-1) = 60 then '60'
when trunc(kor,-1) < 60 then '�̴�'
end as grade
from stu_score
)
group by grade
order by grade desc
;

-- �Ǵ�
select k_kor, count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor
;

--�׷��Լ� group by ���
select department_id, count(*) from employees
group by department_id
order by department_id;

select emp_name, count(emp_name) from employees
group by emp_name;

------------------------------------------
-- �μ��� ��� ������ ���Ͻÿ�
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id
;

--CLERK�� ���ԵǾ� �ִ�, MEP�� ���Ե�, MAN�� ���Ե� ���� ����� ���Ͻÿ�.
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

-- �μ���(group by department_id) �ִ����, �ּҿ���, ��տ����� ����Ͻÿ�
select department_id, max(salary), min(salary), round(avg(salary),1) avg from employees
group by department_id;

------------------------------------------------
-- �μ��� Ŀ�̼��� �޴� ��� ���� ����Ͻÿ�
select department_id,count(department_id),count(commission_pct) from employees
group by department_id;

-------------------------------------------------------------------------------------------
-- having, group by ������, where �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

-- emp_name�� �� ��° ���ڰ� a�� �����ϴ� ���� ����
select department_id, round(avg(salary),2) 
from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);

-- ��ü�μ� ��տ��޺��� ���� �μ��� ��տ��� ���
select department_id, round(avg(salary),2) 
from employees
group by department_id
having avg(salary) < (select avg(salary) from employees)
order by avg(salary);


-- �μ��� �ִ������ 8õ �̻��� �μ��� ���
select department_id, max(salary) 
from employees
group by department_id
having max(salary) > 8000
order by max(salary);

--------------------------------------------------------------------------------------------
-- ���� 

select emp_name,department_id,departmentent_name, salary from employees;

select count(*) from employees; --107��
select count(*) from departments;  --27 �� 

select department_id,department_name from eomployees;

select * from employees,departments;

-- ���̺� 2���� ������ ���� �����̶�� ��
-- 107*27 = 2889
select count(*) from employees, departments;

-- equi join
--: ���� ����� �Ǵ� �� ���̺��� ���������� �����ϴ� �÷��� ���� ��ġ�Ǵ� ���� �����Ͽ� ��� ����
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id
;

select department_id,department_name from departments;

--------------------
 select * from member;
 select * from board;

-- board ���̺� id�� name�� �ְ� ������
select id,name from member;
select id,name from member;
select id,btitle,bcontent from board;

update member set name='ȫ����'
where id = 'aaa';

select bno,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board, member
where member.id = board.id
;
-- member�� �̸��� ����Ǿ id�� �����ϱ� ������ ���� ���� ����

------------------------------------------------------------------------------------

