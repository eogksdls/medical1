-- trunc ����, round �ݿø�
select sysdate, hire_date, trunc(sysdate-hire_date) as �ټӱⰣ from employees;

-- ���� sysdate-1, ���� sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ����, sysdate+100 from dual;

-- ���� : m_yesterday, m_today, m_tomorrow,m_year�� ��¥�÷��� ���� ���̺� ����
create sequence mno_seq
    increment by 1
    start with 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache
;

create table m_date(
    m_no varchar2(15),
    m_today varchar2(15),
    m_tomorrow varchar2(15),
    m_year varchar2(15)
    
);
insert into m_date values(
mno_seq.nextval, sysdate, sysdate+1, sysdate+365);

select m_no no,m_today today,m_tomorrow tomorrow,m_year as afteryear from m_date;

-----------------------------------------------------------------------------------
-- abs: ����, ceil: �ø�, round: �ݿø�(�ڸ��� ����), floor: ����, trunc: ����(�ڸ��� ����)
select abs(hire_date-sysdate) from employees;

select hire_date,round(hire_date,'month') from employees;

--��¥�� ���� �������� ����
select hire_date, trunc(hire_date,'month'), round(hire_date,'month') from employees;

select trunc(hire_date,'month') ������, hire_date from employees
order by hire_date;

------------------------------------------------------------------------------------
select * from channels;

select period,count(period) from kor_loan_status
group by period --�Ⱓ ���� ���� �� ��
order by period;

select period from kor_loan_status
where period='201111';

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) from students -- �����ڸ� �� ����
group by trunc(kor,-1)
order by t_kor;

-- ��¥�� ���� �������� ����
select trunc(hire_date,'month') m_hire_date, count(trunc(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by trunc(hire_date,'month');

-----------------------------------------------------------------------------------------------
--drop table stu_score;
--drop table emp01;
--drop table board;

select * from stu_score
order by no;

update stu_score set name = '������'
where no = 10;

select * from stu_score;

update stu_score set avg=round(total/3,3);
select * from stu_score;

----------------------------------------------------------------------------------------------------
-- 2���� ��¥���� �� ������ Ȯ��
select hire_date, floor(months_between(sysdate,hire_date)), trunc(sysdate-hire_date,2) from employees;

-- ���� �߰�
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date, last_day(hire_date), round(hire_date,'d') from employees;

-- �� �ָ� �������� �Ͽ��� or ����� ��� (�ݿø�)
select sysdate,round(sysdate, 'd') from employees;

-- ��¥�� �������� ������, ó����, ��������
select sysdate ������, trunc(sysdate,'month') ó����, last_day(sysdate) �������� from dual;

-- Ư�� ������ ��¥�� Ȯ��
select sysdate, next_day(sysdate,'������') from dual;

-- ������ ó����
select sysdate,trunc(sysdate,'d'), next_day(sysdate,'�����') from dual;

---------------------------------------------------------------------------------------------
-- board ���̺� default�� �Է��� ���� �� ������ �����Ͱ� �ڵ����� �Էµȴ�.
create table board(
bno number(4) primary key, -- �ߺ��� �ȵ�, null ������� ����. �⺻Ű�� ����
id varchar2(30),
btitle varchar(1000),
bcontent clob,  -- varchar2(3000)������ ���� but clob�� ������(type�� varchar�� ����)
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);

--default ���� �����Ǿ� �־�, ���� �ȳ־��൵ ���� ��µȴ�.
insert into board(bno,id,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�.',board_seq.currval,'2.jpg'
);

select * from board;

--------------------------------------------------------------------------------------
--����ȯ : number(������), character(������), date(��¥��)

select sysdate from dual;

--���ڿ��� �����ؾ� ��¥ ��������� �ٲ� �� �ִ�.
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

--���� ko20240001 �������� ����ϱ�(���ڳ����� + ����� �� �� ����. ||�� �������~)
select 'ko'||to_char(sysdate, 'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'),to_char(sysdate,'day') from dual; -- �� // ������

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

--���� hire_date�� ����� �ð� �� ���� �������� ����ϱ�
select to_char(hire_date, 'yyyy-mm-dd hh:mi:ss mon day') from employees;

-----------------------------------------------------------------------------------------
--am, pm ����, ���� ���� ��� hh24  24�ð����� ǥ��
select to_char(sysdate, 'pm hh24:mi:ss') from dual;

--drop table stu_score;
select * from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

--��¥���� ��� �����Ͱ� ���ִ��� ����Ͻÿ�
select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') c_date_, count(to_char(c_date,'yyyy-mm-dd hh:mi:ss day')) count from stu_score
group by to_char(c_date,'yyyy-mm-dd hh:mi:ss day')
order by c_date_
;
-------------------------------------------------------------------------------------
-- �������� ��Ģ����(+,-,*,/)�� �Ұ���. ������ �ڸ��� ǥ��, ��ǥ ǥ�� ����
-- ������ ��Ģ���� ����/ �÷��� ��Ģ���� ����/ �ڸ��� ǥ��(0001->�ȵ�), ��ǥǥ�� �ȵ�.
-- ��¥�� +,- ������ ����, months_between 2�� ��¥ ���� ���� �� ��갡��, ������ ��¥������ �����ؼ� ����� �ȵ�

-- ������ �ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȯ�ؼ� �������
-- ������ �ȿ� ���ڰ� ������ �ڵ� ����ȯ �Ұ�
select 10 a, 100 b, (10+100) ab, to_char(100), 10+'100' from dual;
select 10 a, 100 b,(10+100) ab, to_char(100),10+'100��'  from dual;

-- '0000' ���ڸ��� 0���� ä��, '9999' ���ڸ��� �������� ��.
select 12340000, to_char(12340000), length(to_char(12340000,'999,999,999')) from dual;
select length(12340000), to_char(12340000), to_char(12340000,'999,999,999'),
length(to_char(12340000,'999,999,999')) from dual;

-- L �� ��ȭ ǥ��
select 12340000, to_char(12340000,'L999,999,999') from dual;
-- $ �� $ ǥ��
select 12340000, to_char(12340000,'$999,999,999') from dual;
-- 
select 1234.1234, to_char(1234.1234),to_char(1234.1234, '000,999.99') from dual;

--10�� �ڸ��� ǥ��
-- ���������ؼ� �ڸ��� Ȯ�� trim ���
select length(trim(to_char(12345, '0000000000'))), length(trim(to_char(12345,'999,999'))) from dual;

--����
--123,456,789 + 100,000 ���� ����Ͻÿ�/ õ���� ǥ��
--123,556,789
------------------------------
--1. 123,456,789 ��ǥ ����
select replace('123,456,789',',','') from dual;
--2. Ÿ���� number�� ����
select to_number(replace('123,456,789',',','')) from dual;
--3. ���ϱ�
--4. ������ Ÿ������ �����ؼ� ��ȭ, ��ǥ ǥ��
select to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')),'L999,999,999') sum from dual;

select '123,456,789' n1, '100,000' n2,
to_char(to_number(replace('123,456,789',',','')) + to_number(replace('100,000',',','')),'L999,999,999') sum from dual; 

----------------------------------------------------------------------------------------------------------------------------
-- ������ ���� �Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

select to_number('0001234') from dual; -- 1234�� ���

----------------------------------------------------------------------------------------
-- ��¥��
-- ������ +,- �ȵ�
select '2024-04-24 11:00:00'-'2024-04-01 10:00:00' from dual; --����
select to_date('2024-04-24')-to_date('2024-04-01') from dual;
select to_date('2024/04/24')-to_date('2024/04/01') from dual;
select to_date('24/04/24')-to_date('24/04/01') from dual;

select to_date('2024-04-24 11:00:00') from dual;

-- ���� 
-- '20240401'���¸� 2024-04-01 Ÿ������ �����ؼ� ���
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd hh:mi:ss') from dual;

select hire_date from employees
where hire_date >= '20080101'
;

select * from stu_score;

--������������ ��¥���� ��� �˾Ƽ� �ν��� �� �� �ִ�.
select c_date from stu_score
where c_date = '2024/04/05';

select sysdate-to_date('2024/04/01') from dual;

-- ����
-- 20,000 / 10,000 ���������� 
select '20,000', '10,000' from dual;
-- �޸� ����
select replace('20,000',',',''), replace('10,000',',','') from dual;
select to_number('20,000','99,999') from dual; -- �ٷ� ���������� ����ȯ
-- ���������� ����ȯ �� ������
select to_number(replace('20,000',',',''))/to_number(replace('10,000',',','')) from dual;
select to_number('20,000','99,999') / to_number('10,000','99,999') from dual;

-- ����
select commission_pct from employees;
-- �������� = ���� + (���� * Ŀ�̼�) ���������ؼ� ����Ͻÿ�
select salary, salary+(salary*nvl(commission_pct,0)),commission_pct from employees;

-- commission_pct null���� ����Ͻÿ�
-- is null
select commission_pct from employees
where commission_pct is null ;

-------------------------------------------------------------------------------------
select manager_id from employees
order by manager_id desc;

-- ���� �Ŵ������̵� null�̸� 0���� ��� -> nvl(�����͸�,0)
select nvl(manager_id,0) from employees
order by manager_id desc;

-- ���� manager_id�� null�̸� ceo�� �Է��Ͻÿ�
-- ceo�� ���ڿ��̱� ������ manager_id ���� ���ڿ��� ��ȯ���־�� �Ѵ�. 
select nvl(to_char(manager_id), 'ceo') from employees
order by manager_id desc;




