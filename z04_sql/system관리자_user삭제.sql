alter session set"_ORACLE_SCRIPT"=true;

--사용자 생성 ""없애야함
create user ora_user identified by 1111;

--권한 부여
grant connect, resource, dba to ora_user;

--계정 삭제
drop user "ora_user";

drop user "ora_user1";

drop user ora_user;

drop user ora_user2;

--권한 삭제
revoke connect, resource, dba from ora_user2;
