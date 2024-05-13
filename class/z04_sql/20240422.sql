select * from employees;

select employee_id,emp_name from employees;

select salary from employees;

--Ÿ�� : numebr +,-,*,/ ����
select salary, salary * 1400 as m_sal, salary*1400*12 as y_sal from employees;

select * from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score;

--���̽�.

select department_id from employees;

select nvl(department_id,0) from employees; --null�� ���� 0�� ���� �ƴϱ� ������ ���� ã�Ƽ� 0���� �ٲ������

select * from employees;

--����(����+Ŀ�̼�)
select salary, salary + (salary*commission_pct) from employees; --null�� ����
select salary, salary + (salary*nvl(commission_pct,0)) as real_sal from employees;
--����Ŭ�� ��ҹ��� ������ ���� ������, �����ؼ� ���� ������ 
--""�� ����ϱ�(�ִ� �״�� ��°���) *��Ī
select salary, salary + (salary*nvl(commission_pct,0)) as "Real_sal" from employees;

--��Ī ��뿡 �ѱ۵� ����������, �����ϸ� ������� �ʴ°� ����.(�����߻� ���ɼ�����)
select salary as ���� from employees; 

--

select * from departments;

--�μ� ��ȣ, �μ� �̸��� ����Ͻÿ�.

select department_id as "�μ� ��ȣ",department_name as "�μ� �̸�" from departments;

-- �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� concat�� ���
-- concat : ȫ�浿, ������, �̼���, ������, �豸 - > split(",") : �и�

select * from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

--distinct : �ߺ�����
--where : ������ not �����ϰ� �˻��Ϸ��� is not null -> null�� �ƴ� ���鸸 �ҷ��Ͷ�
select distinct department_id from employees where department_id is not null;

-- manager_id

select manager_id from employees;
select distinct manager_id from employees;
select distinct manager_id from employees where manager_id is not null;

select * from employees;
select employee_id, salary from employees 
where employee_id = 200 or employee_id = 201 or employee_id = 202;

-- where : ������ ����
select * from employees
where employee_id >= 200 and employee_id <=203;

select * from employees
where employee_id >= 200 or employee_id <= 150;

--�μ� ��ȣ : 10,30,50 ���� �ش��ϴ� ��� ���
select employee_id, department_id from employees
where department_id = 10 or department_id = 30 or department_id = 50;

--���� 6000 ~ 9000 ������ ����� ����Ͻÿ�
select * from employees;
select employee_id, salary from employees
where salary >= 6000 and salary <= 9000;

--���� 6000,7000,8000 �� ����� ����Ͻÿ�
select employee_id, salary from employees
where salary = 6000 or salary = 7000 or salary = 8000;

--�μ���ȣ�� 50���̸鼭, ������ 8000�̻��� ��� ���
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
1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values (
5,'�豸',100,100,100,300,100,1
);
commit;

--stu_score �̸��� ȫ�浿�� ����� ����Ͻÿ�
select * from stu_score;

-- ��������
select hire_date from employees
order by hire_date desc;

--��������
select emp_name, hire_date from employees
where hire_date >='02/01/01'
order by hire_date asc;

--��¥ ��Ģ���� ����
select hire_date, hire_date+100 from employees;
--�ݿø� round
select round(sysdate-hire_date,2) from employees;

select * from employees;

--���� ��ġ��� +������ �Ұ���, ||��ɾ� ���
select emp_name||email from employees;

--�Ի��� 05�� �̻� 06�� �����̸鼭 ������ 6000 �޷� �̻��� ����� �������ķ� ����Ͻÿ�
select * from employees;
select emp_name, salary, hire_date from employees
where hire_date >='05/01/01' and hire_date <='06/12/31' and salary >= 6000
order by hire_date desc;

-- not ǥ��: !=, ^=, <>
select department_id from employees
where department_id <> 10 and department_id <> 50 
order by department_id
;

--5000 �̻� 9000 ����
select emp_name, salary from employees
where salary >= 5000 and salary <=9000
order by salary
;

-- ����� 99�� �̻��� �л��� �˻��Ͻÿ�
select name, avg from stu_score
where avg >= 99
;

select * from students;

-- �̸� ����
update students set name='ȫ����' 
where no = 8
;

commit;

select * from students;

--students
-- ��� 70��, ����� 75�� �̻��� �л� ���
select name,kor,avg from students
where kor >=70 and avg >=75
;

--�������� 80, ���� ���� 70, ���� ���� 90 �� �л��� ����Ͻÿ�
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

-- ����
update students set kor=100, total = 100+eng+math, avg =(100+eng+math)/3
where no =1;
select * from students
where no = 1;
commit;

-- ���� ���� 70~90���� �л��� ����Ͻÿ�
select name, kor from students
where kor >=80 and kor <=90
order by kor
;

-- 100��
select * from students;

-- 27��
--between a and b : a���� ũ�ų� ����, b���� �۰ų� ���� �� �˻�  
--> >,<�� ������ �߻��� ���ɼ��� �־� between�� �����
select name, kor from students
where kor between 70 and 90
order by kor
;

-- 73��
-- not between a and b : a���� ũ�ų�, b���� ���� �� �˻�(a,b ���� �ȵ�)
select name, kor from students
where kor not between 70 and 90
;

-- ��¥�� between ��� ���
select emp_name, hire_date from employees
order by hire_date;

--95�� �̻�, 01�� ���� �Ի��� ��� �˻�
select emp_name, hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date asc;

-- �̸� �˻�
select * from students
where name='ȫ�浿';

-- like �˻� : Ư�� �ܾ ���ԵǾ� �ִ� ������ �˻�
select * from students
where name like '%ȫ%';

-- ���� �����ڰ� ȫ�� �ܾ �˻��ϼ���
select * from students
where name like '%ȫ';
-- ���� �ܾ� ȫ : 'ȫ%'
-- �� �ܾ� ȫ : '%ȫ'
-- Ư�� �ܾ� ȫ : '%ȫ%'

-- '��'�� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '%��%';

-- _: �� ĭ ������ ���, �� �տ� 1���� �ܾ �����鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '_��%';

--3��° ĭ�� t�� ���� �̸� �˻�
select * from students
where name like '__t%';

--���̰� 4�̰�, 3��° r�� �� �ִ� �̸� �˻�
--1) �ڵ�� ª�� ���� ����
select * from students
where name like '__r_';
--2)
select * from students
where name like '__r%' and length(name) = 4;

-- �̸��� A�� ���۵Ǵ� �л� �̸��� �˻��ϼ���
select * from students
where name like 'A%';

-- �̸��� a�� �� �ִ� �л� �˻�
select * from students
where name like '%a%'
order by name;

-- ��ҹ��� ���� ���� a�� �� �ִ� �л� �˻�
-- �ҹ��� ġȯ(lower), �빮�� ġȯ(upper), ù���� �빮�� (initcap)
select * from students
where lower(name) like '%a%';

-- �̸��� a�� ���Ե��� ���� �л� �˻�
select no,name from students
where lower(name) not like '%a%';


select manager_id from employees;
--manager_id�� 100 �� ��� �˻�
select employee_id, emp_name, manager_id from employees
where manager_id = 100;

--null�� ��񱳰� �ȵ�
select employee_id, emp_name, manager_id from employees
where manager_id = null;

--null���� ã�� �� is ���
select employee_id, emp_name, manager_id from employees
where manager_id is null;

select * from employees
where manager_id is not null;
--------------------------------------------------------------------------
select * from stu_score;

-- �ѱ� ���ĵ� ����
select * from stu_score
order by name asc;

-------------------------------------------------------------------------
select * from students;

--kor ���� ������ ���, eng ���� �������� ����
select * from students
order by kor desc, eng asc;

-- total�� ��������(desc)
select * from students
order by total desc;

--------------------------------------------------------------------------
-- �÷��߰�
alter table students add rank number(3);
-- �÷�Ÿ��
desc students;

select * from students;

update students set rank = 0;

commit;

--------------------------------------------------------------------------
-- ��� �ű��(����������, table�� ������ �ȵ�)
select no,name,total,rank() over(order by total desc) as rank from students;

select * from students; 
-- no=1�� 13�� ������Ʈ
update students set rank = 13
where no = 1;

select * from students
where no =1;

-- 2��° ���
update students s1 set rank = 13
where no = 1;

-- ��ü ��� ������Ʈ
update students s1 set rank = (select ranks from 
( select no no2, rank() over(order by total desc) as ranks from students) s2
where s1.no = s2.no2);

select * from students;
commit;

-- select * from (���̺�);
-- ����� 60�� �̻��� �л��� �� ������� 70�� �̻��� �л� �˻�
select * from (select * from students where avg >= 60)
where kor >= 70;

----------------------------------------------------------------------