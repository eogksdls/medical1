import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# sql 실행
# employees 테이블에서 사번,이름,월급,실제월급(월급+(월급*커미션)), 월급*1410 원화로 환산해서
# kor_salary만 원화표시, 천단위 표시해서 출력
sql = '''select employee_id,emp_name,salary,(salary+(salary*nvl(commission_pct,0))) real_sal,
to_char(salary*1410,'999,999,999') kor_sal from employees'''
cursor.execute(sql)
data = cursor.fetchall()

print("[ 데이터 출력 ]")
print("번호\t사원명\t\t월급\t실제월급  원화환산")
for d in data:
    print(d[0],end='\t')
    print(d[1],end='\t')
    print(d[2],end='\t')
    print(d[3],end='\t')
    print("￦",d[4].strip())
    
# 부서별 평균웕, 최대월급, 최소월급을 출력하시오
sql = '''select job_id, avg(salary), max(salary), min(salary) from employees
group by job_id'''
cursor.execute(sql)
data = cursor.fetchall()

print("[ 데이터 출력 ]")
print("부서\t\t평균월급\t최대\t\t최소")
for d in data:
    print(f'{d[0]:<11}',end='\t')
    print(d[1],end='\t\t')
    print(d[2],end='\t\t')
    print(d[3])