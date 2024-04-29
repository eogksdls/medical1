--<9��>--
-- ���̺� ����
create table emp01 (
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- ���Ӱ� ���� ���̺� ���� ���̺� ������ �����ϱ�
desc employees;

create table emp02 as
select * from employees;
-- emp02 == employees 

-- ���̺� ������ �����ϱ�
create table emp03 as
select * from employees where 1=2;
-- �̴� 1=2�� ���� �����͸��� �������� ������ �ɾ������ν�, ������ �� ���������� �����ʹ� ������ �ʵ���
-------------------------------**
-- ���̺��� �̹� �����ϸ鼭, �����͸� �����ϱ�(1) : ������ �ٸ� ��� (emp01�� �� ���� 3�� -> employees�� 14��)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;  --select : ��� �־��شٴ� ��
--���� ��� ���� �����͸� insert�ϴ� ����
-- insert into emp01 values();
select * from emp01; --Ȯ��

--1�� �����͸� �߰�
insert into emp01 values(
207,'ȫ�浿','2024-04-26'
);

-- ���̺��� �����ϸ鼭 �����͸� ����(2) : ������ ���� ���
insert into emp03
select * from employees;

select * from emp03;
------------------------------------**
select * from employees;

------------------------------------------------------------------------------------------
--drop table s_info;
--drop table m_date;

desc memeber;
-- �÷� Ÿ�Ժ���
alter table member
modify(stu_name varchar2(30));

-- �÷� ����
alter table member
drop column pw;

-- �÷�
alter table member
add( pw varchar2(30));

select * from member;

select mno,id,stu_name,gender from member;
select * from member;

insert into member values(
seq)mno.nextval,'fff','������','male','1111'
);

--�÷� ���� ����
-------------------------------**
alter table member modify stu_name invisible;
alter table member modify gender invisible;

alter table member modify stu_name visible;
alter table member modify gender visible;

-- �÷��� �Ͻ��� ��� ����
alter table member
set unused(id);

-- ������� ����
alter table member
drop unused columns;

select * from member;
--------------------------------**
-- ���̺� �̸� ����
rename emp01 to employees01;
-----------------------------------------------------------------------------
--<10��>--
--���漺 ��������
-- not null: null����� ����
-- unique : �ߺ��� �� ��� ����, ����
-- primarykey : null ��� X, �ߺ��� �� ��� X
-- foreignkey : ���� ���̺��� Į������ ������ �� ���
-- check: ���� ������ �����Ͱ��� ������ ���� ���� �� ������ ���� ���
desc employees;

--drop table employees01;
--drop table emp02;
--drop table member;
--drop table board;

create table member ( 
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','ȫ�浿','male'
);

insert into member(id,pw,name) values(
'bbb','1111','������'
);

insert into member(id,pw) values(
'ccc','1111'
);

-- pw not null ����, id�� primary key ����(�ߺ� �ȵ�)
insert into member(id) values(
'ddd'
);  -- ����
insert into member(id,pw) values(
'aaa','1111'
);  -- ����
insert into member(id,pw) values(
'a','1111'
); -- ���� ����

select * from member;

--�ǽ�: �������� not null ------------------------------------
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02(empno,ename,job,deptno) values(
1,'ȫ�浿','�л�',12
);

insert into emp02(empno,ename) values(
2,'������'
);

insert into emp02(empno,ename,job) values(
1,'�̼���','�л�'
);

insert into emp02(empno,ename,deptno) values(
1,'������',15
);

insert into emp02(empno,ename) values(
1,'�豸'
);

select * from emp02;
---------------------------------------------------------------
-- �ǽ�: unique: �ߺ��� �� ��� X--------------------------------
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03(empno,ename,job,deptno) values(
1,'ȫ�浿','�л�',12
);

insert into emp03(ename,deptno) values(
'ȫ�浿',18
);

select * from emp03;
-- ȫ�浿�ε�, empno�� 1���� ȫ�浿 ã��
select * from emp03
where empno=1;

-- empno�� null�� ȫ�浿 
select * from emp03
where empno is null and ename = 'ȫ�浿';
--�Ǵ�
select * from (select * from emp03
                where ename='ȫ�浿')
where empno is null;

--empno�� null�� ����� ��� ����Ͻÿ�
select * from emp03
where empno is null;

---------------------------------------------------------------
create table emp01(
Empno number(4) primary key,
Ename varchar2(20) not null,
Job varchar(9),
Deptno number(2)
);

insert into emp01(Empno,Ename,Job) values(
5,'������','�ǻ�'
);

select * from emp01;
--ȫ�浿 ã��
select * from emp01
where Ename = 'ȫ�浿';

---------------------------------------------------------------------
-- foreign key (�ܷ�Ű)
--drop table emp01;

-- emp01 ���̺� ����
create table emp01 (
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);

desc emp01;

insert into emp01 values(
1,'ȫ�浿','0001',10
);

insert into emp01 values(
2,'������','0002',20
);

insert into emp01 values(
3,'�̼���','0002',30
);

--commit;

-- deptno 10-270
insert into emp01 values(
4, '�豸','0003',270
);

insert into emp01 values(
5, '������','0004',280  --�θ�Ű�� ������ �Ѿ�� ����
);


--emp01 ���̺� foreign key �߰�
-- fk_deptno�� ��Ī
-- add constraint ��Ī foreign key(�����÷�) references �ٸ� ���̺�(�÷��̸�)
alter table emp01
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;

-- foreign key ����
alter table emp01
drop constraint fk_deptno;

select * from emp01;

---------------------------------------
-- dept ���̺� ����
create table dept01 (
deptno number(2) primary key,
dept_name varchar2(20)
);

-- �÷� Ÿ�� ����
alter table dept01
modify ( dept_name varchar(80) );

desc dept01;

-- ���̺� ����
insert into dept01(deptno,dept_name)
select department_id, department_name from departments;

select * from dept01;

-------------------------------------------
create table board(
bno number(4) primary key,
id varchar(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);

insert into board values(
1,'aaa','�Խñ�1','����1'
);
insert into board values(
4,'ccc','�Խñ�4','����4'
);

commit;

select * from board;

alter table board
add constraint fk_id foreign key(id)
references member(id);

-----------------------------------------------------------------------------
-- commnet ���̺� ������̺�

-- cno number(4) primary key
-- bno number(4)
-- cpw varchar2(20)
-- ccontent varchar2(1000)

create table comments (
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);

-- ��� �ޱ�
insert into comments values(
5,2,'1111','��۳���2'
);

-- ��� �����(�Խñ� �� ����� �޷��ִ� ����, �Խñ��� �����ϸ� ��۵鵵 ��� ������ �� �ְ�)
-- fk�� ��ϵǾ� �ִ� ��� �����͸� ������Ű�� ��.
-- fkŰ�� ��ϵǾ� �ִ� �����ʹ� ��� ���� ��Ű�� ��
delete board where bno=5;

commit;

select * from board;
select * from comments;

select * from board;