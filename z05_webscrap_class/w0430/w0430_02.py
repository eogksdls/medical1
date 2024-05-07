import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성

# board 정보에서 id, name을 포함해서 데이터를 가져와 출력하시오
# # board 테이블 id, member 테이블 name
# sql = "select * from board"
# cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
# data = cursor.fetchall() # fetchall() : 모든 데이터 가져옴. fetchone() : 1개의 데이터만 가져옴.

# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data:
#    # print(d)
#     print("번호 : ",d[0])
#     print("ID : ",d[1])
#     print("제목 : ",d[2])
#     print("내용 : ",d[3])
#     print("날짜 : ",d[4])
#     print("GROUP : ",d[5])
#     print("STEP : ",d[6])
#     print("HIT : ",d[7])
#     print("FILE : ",d[8])
#     print("-"*20)    
# print("-")  
# print("타입 : ",type(data))  # list 형태로서 data[i]식으로 원하는 데이터만을 출력해낼 수 있다

#--------------------------------------------------------------------------------------

# # board 테이블 id, member 테이블 name
# sql = "select bno, a.id, name, btitle, bcontent, bdate, bgroup, bstep, bindent, bhit, bfile\
#         from board a, member b\
#         where a.id = b.id"
# cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
# data = cursor.fetchall() # fetchall() : 모든 데이터 가져옴. fetchone() : 1개의 데이터만 가져옴.

# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data:
#    # print(d)
#     print("번호 : ",d[0])
#     print("ID : ",d[1])
#     print("이름 : ",d[2])
#     print("제목 : ",d[3])
#     print("내용 : ",d[4])
#     print("날짜 : ",d[5])
#     print("GROUP : ",d[6])
#     print("STEP : ",d[7])
#     print("HIT : ",d[8])
#     print("FILE : ",d[9])
#     print("-"*20)    
# print("-")  
# print("타입 : ",type(data))  # list 형태로서 data[i]식으로 원하는 데이터만을 출력해낼 수 있다

#---------------------------------------------------------------------------------------
# stu_score avg 90점 이상 A, 80점 이상 B,C,D 60점 미만 F
# 학번 이름 합계 평균 학점을 출력하시오

# sql = '''select no,name,total,avg,
# case when avg >= 90 then 'A'
# when avg >= 80 then 'B'
# when avg >= 70 then 'C'
# when avg >= 60 then 'D'
# else 'F'
# end as grade
# from stu_score'''
# cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
# data = cursor.fetchall() # fetchall() : 모든 데이터 가져옴. fetchone() : 1개의 데이터만 가져옴.

# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data[:5]:
#    # print(d)
#     print("학번 : ",d[0])
#     print("이름 : ",d[1])
#     print("합계 : ",d[2])
#     print("평균 : ",round(d[3],1))
#     print("성적 : ",d[4])
#     print("-"*20)    
# print("-")  
# print("타입 : ",type(data))

sql = "select * from stu_score"
# 평균을 가지고 파이썬에서 프로그램하여 학점을 출력하시오
# 학번,이름,합계,평균,학점을 프로그램해서 출력하시오
cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall()

# print(data)

print("[ 학생 성적 ]")
for d in data[:20]:
    print("학번 : ",d[0])
    print("평균 : ",round(d[6],1))
    #---------------------
    # 성적부여 구문
    if d[6] >= 90 :
        print("grade : A")
    elif d[6] >= 80 :
        print("grade : B")
    elif d[6] >= 70 :
        print("grade : C")
    elif d[6] >= 60 :
        print("grade : D")
    else:
        print("grade : F")
    #----------------------
    print("-"*20)

# salary 평균을 구하시오
sql = '''select job_id,round(avg(salary),1) from employees
group by job_id'''
cursor.execute(sql)      # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall()
print(data) # 리스트 형태

for d in data[:10]:
    print("[ 부서별 평균 월급 ]")
    print("부서 이름 : ", d[0])
    print("평균 월급 : ", d[1])
    print("-"*20)
    
conn.close()  # 데이터베이스 연결 해제