--������ �ִ� ���̺� �˻�
--F5: consoleâ ���(��ũ��Ʈ ���, ���� �ű��� ��ü����), F9: ���̺� ����(���� ���, �� �پ� ����)
--�����ϸ� F9�� ���� �� �پ� �����ϱ�
--console â���� ���� ������ �� �ٸ� �巡���ؼ� F5 ������ ��
select * from tab;

select * from employees;

--���̺� ���� Ȯ��(consoleâ���� �� �� �ִ�)
desc employees;

--���̺� ����
create table stu_score(
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2) -- 5�ڸ� �� 2���� �Ҽ������� ǥ���ض�
);

insert into stu_score(no,kor,eng,avg) values(
1,100,99,(100+99)/2
);

insert into stu_score values( --������ ��� ä��� ��ó�� (no,kor,eng,avg)�ۼ� ���ص� ��!
1,95,98,(95+98)/2
);

insert into stu_score values(
    1,80,70.223,(80+70.223)/2
);

select * from stu_score;
-- ������ �ݿ�(���� ������ ����,���� �Ұ���)
commit;

create table num (
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);

-----------------------------------------------------------------------------
--���� ��¥(�⺻ ����)
-- dual�̶� �������̺��� �������� ��
select sysdate from dual;
-- ������� ����
-- ��¥ ���˺��� :  to_char ����ȯ -> ������ ����
select to_char(sysdate,'yyyy-mm-dd') from dual;
select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'hh:mi:ss') from dual;

--����κ��� +1000�� ���� ��¥�� ������
select sysdate+1000 from dual;

select sysdate - to_date('24/01/01') from dual;
