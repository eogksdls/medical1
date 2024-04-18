--테이블 생성
--number() 자리수
--primary 대표키 설정
--char 고정 문자열(읽어내는데 속도가 varchar보다 빠름)
--varchar2  가변길이 문자열
------------------------------------------------------------------
create table stu_score(
  no number(4) primary key,
  name varchar2(30),
  kor number(3),
  eng number(3),
  math number(3),
  total number(3),
  avg number(6)
);

--1개의 데이터 입력: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
 1,'홍길동',58,99,95,(58+99+95),(58+99+95)/3
 );
 --------------------------------------------------------------------
 --데이터 검색: select
 select * from stu_score;
 --데이터 최종저장 :  commit -> 다시 전으로 못되돌림(중요!!!!!!!!!!!!)
 commit;
----------------------------------------------------------------------- 
 -- 1개 데이터 수정: update ->no가 1인 데이터의 name을 홍길자로 바꿔줘(''쓰기)
 update stu_score set name='홍길자' where no=1;
 --수정 후 확인
 select * from stu_score;
----------------------------------------------------------------------- 
 --커밋하기 전까진 데이터테이블에 반영이 되지 않기 때문에 수정,복원이 가능하다.
 rollback;
 --데이터 스크립트 출력
 desc stu_score;
-----------------------------------------------------------------------  
 --삭제 : delete
 delete stu_score where no=1;
 --삭제 후 확인해보기
 select * from stu_score;
 commit; 
 ----------------------------------------------------------------------
 --테이블 삭제
 drop table stu_score;
 
 