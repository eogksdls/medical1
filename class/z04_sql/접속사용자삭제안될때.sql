-- user �̸� �빮�ڷ� �ۼ��ؾ���
select sid,serial#,username,status from v$session where schemaname = 'ORA_USER2';

--'SID,SERIAL#'������ �����ֱ�
alter system kill session '510,19477';

drop user ora_user2 cascade;