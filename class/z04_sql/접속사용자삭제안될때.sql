-- user 이름 대문자로 작성해야함
select sid,serial#,username,status from v$session where schemaname = 'ORA_USER2';

--'SID,SERIAL#'순으로 적어주기
alter system kill session '510,19477';

drop user ora_user2 cascade;