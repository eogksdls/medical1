--<9장>--
-- 테이블 생성
create table emp01 (
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

-- 새롭게 만든 테이블에 기존 테이블 데이터 복사하기
desc employees;

create table emp02 as
select * from employees;
-- emp02 == employees 

-- 테이블 구조만 복사하기
create table emp03 as
select * from employees where 1=2;
-- 이는 1=2일 때의 데이터만을 가져오는 조건을 걸어줌으로써, 구조는 다 가져오지만 데이터는 들고오지 않도록
-------------------------------**
-- 테이블은 이미 존재하면서, 데이터만 복사하기(1) : 구조가 다른 경우 (emp01는 열 개수 3개 -> employees는 14개)
insert into emp01(emp_id,emp_name,hire_date)
select employee_id, emp_name, hire_date from employees;  --select : 골라서 넣어준다는 뜻
--보통 모든 열의 데이터를 insert하는 것은
-- insert into emp01 values();
select * from emp01; --확인

--1개 데이터만 추가
insert into emp01 values(
207,'홍길동','2024-04-26'
);

-- 테이블이 존재하면서 데이터만 복사(2) : 구조가 같은 경우
insert into emp03
select * from employees;

select * from emp03;
------------------------------------**
select * from employees;

------------------------------------------------------------------------------------------
--drop table s_info;
--drop table m_date;

desc memeber;
-- 컬럼 타입변경
alter table member
modify(stu_name varchar2(30));

-- 컬럼 삭제
alter table member
drop column pw;

-- 컬러
alter table member
add( pw varchar2(30));

select * from member;

select mno,id,stu_name,gender from member;
select * from member;

insert into member values(
seq)mno.nextval,'fff','김유신','male','1111'
);

--컬럼 순서 변경
-------------------------------**
alter table member modify stu_name invisible;
alter table member modify gender invisible;

alter table member modify stu_name visible;
alter table member modify gender visible;

-- 컬럼은 일시적 사용 제한
alter table member
set unused(id);

-- 사용제한 해제
alter table member
drop unused columns;

select * from member;
--------------------------------**
-- 테이블 이름 변경
rename emp01 to employees01;
-----------------------------------------------------------------------------
--<10장>--
--무경성 제약조건
-- not null: null허용을 안함
-- unique : 중복된 값 허용 안함, 유일
-- primarykey : null 허용 X, 중복된 값 허용 X
-- foreignkey : 참조 테이블의 칼럼값이 존재할 시 허용
-- check: 저장 가능한 데이터값의 범위나 조건 지정 후 설정한 값만 허용
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
'aaa','1111','홍길동','male'
);

insert into member(id,pw,name) values(
'bbb','1111','유관순'
);

insert into member(id,pw) values(
'ccc','1111'
);

-- pw not null 적용, id는 primary key 적용(중복 안됨)
insert into member(id) values(
'ddd'
);  -- 오류
insert into member(id,pw) values(
'aaa','1111'
);  -- 오류
insert into member(id,pw) values(
'a','1111'
); -- 삽입 가능

select * from member;

--실습: 제약조건 not null ------------------------------------
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02(empno,ename,job,deptno) values(
1,'홍길동','학생',12
);

insert into emp02(empno,ename) values(
2,'유관순'
);

insert into emp02(empno,ename,job) values(
1,'이순신','학생'
);

insert into emp02(empno,ename,deptno) values(
1,'강감찬',15
);

insert into emp02(empno,ename) values(
1,'김구'
);

select * from emp02;
---------------------------------------------------------------
-- 실습: unique: 중복된 값 허용 X--------------------------------
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);

insert into emp03(empno,ename,job,deptno) values(
1,'홍길동','학생',12
);

insert into emp03(ename,deptno) values(
'홍길동',18
);

select * from emp03;
-- 홍길동인데, empno가 1번인 홍길동 찾기
select * from emp03
where empno=1;

-- empno가 null인 홍길동 
select * from emp03
where empno is null and ename = '홍길동';
--또는
select * from (select * from emp03
                where ename='홍길동')
where empno is null;

--empno가 null인 사람을 모두 출력하시오
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
5,'유관순','의사'
);

select * from emp01;
--홍길동 찾기
select * from emp01
where Ename = '홍길동';

---------------------------------------------------------------------
-- foreign key (외래키)
--drop table emp01;

-- emp01 테이블 생성
create table emp01 (
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(6)
);

desc emp01;

insert into emp01 values(
1,'홍길동','0001',10
);

insert into emp01 values(
2,'유관순','0002',20
);

insert into emp01 values(
3,'이순신','0002',30
);

--commit;

-- deptno 10-270
insert into emp01 values(
4, '김구','0003',270
);

insert into emp01 values(
5, '강감찬','0004',280  --부모키의 범위를 넘어서서 오류
);


--emp01 테이블에 foreign key 추가
-- fk_deptno는 별칭
-- add constraint 별칭 foreign key(현재컬럼) references 다른 테이블(컬럼이름)
alter table emp01
add constraint fk_deptno foreign key(deptno)
references dept01(deptno)
;

-- foreign key 삭제
alter table emp01
drop constraint fk_deptno;

select * from emp01;

---------------------------------------
-- dept 테이블 생성
create table dept01 (
deptno number(2) primary key,
dept_name varchar2(20)
);

-- 컬럼 타입 변경
alter table dept01
modify ( dept_name varchar(80) );

desc dept01;

-- 테이블 복사
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
1,'aaa','게시글1','내용1'
);
insert into board values(
4,'ccc','게시글4','내용4'
);

commit;

select * from board;

alter table board
add constraint fk_id foreign key(id)
references member(id);

-----------------------------------------------------------------------------
-- commnet 테이블 댓글테이블

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

-- 댓글 달기
insert into comments values(
5,2,'1111','댓글내용2'
);

-- 댓글 지우기(게시글 내 댓글이 달려있는 상태, 게시글을 삭제하면 댓글들도 모두 지워질 수 있게)
-- fk를 등록되어 있는 모든 데이터를 삭제시키는 것.
-- fk키로 등록되어 있는 데이터는 모두 존재 시키는 것
delete board where bno=5;

commit;

select * from board;
select * from comments;

select * from board;