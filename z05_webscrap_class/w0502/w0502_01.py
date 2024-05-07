import oracledb
import math
# ip: 인터넷 상의 내 컴퓨터의 주소(유일함)
# port: 컴퓨터 프로그램 접속장소
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# 최초 번호
number = 1
perCount = 10
startrow = (number-1) * perCount + 1 #1,11,21,31,...
endrow = startrow + perCount - 1 # 10개씩 가져오기, 10,20,30,...

#---------------------------------------------------------------------------
def program(search):
    sql = f'''select * from (select row_number() over(order by no) rnum, a.* 
                        from stu_score a where id like '%{search}%') 
                        where rnum >= {startrow} and rnum <= {endrow}'''
    cursor.execute(sql)
    data = cursor.fetchall()

    # 10개씩 나눠서 보여주도록 구성
    print("[ 학생 검색 데이터 ]")
    for d in data:
        print(d)
        
    print("-"*80)
    print("검색된 페이지 : ",number," / ","검색된 데이터 수 : ",all_count[0])
    
    return number,startrow,endrow
#--------------------------------------------------------------------------

# 프로그램 시작
while True:
    search = input("찾고자 하는 학생의 이름을 입력하세요(0.종료) : ")
    sql = f'''select count(*) from 
            (select * from (select row_number() over(order by no) rnum, a.* 
            from stu_score a where id like '%{search}%'))'''
    cursor.execute(sql)
    all_count = cursor.fetchone()
    
    if search == '0':
        print(">> 프로그램을 종료합니다.")
        print("-"*30)
        break
    
    else:
        while True:
            if number == 1:  # 처음엔 무조건 페이지 1이 나올 수 있게
                program(search)
            
            else:
                print("1.< 이전 ",end= "\t")
                print("2. 다음 > ", end="\t")
                print("0. 종료")
                no = int(input("원하는 번호를 입력하세요 : "))
                if no == 0:
                    print("성적 데이터 찾기를 종료합니다.")
                    print("-"*30)
                    break
                #----------------------------------------------------------------------
                elif no == 1: # 이전
                    if number == 2:   # 한 바퀴 돌면 무조건 +1이 되기 때문에 2가 됨
                        number = 1
                        startrow = (number-1) * perCount + 1 #1,11,21,31,...
                        endrow = startrow + perCount - 1 # 10개씩 가져오기, 10,20,30,...
                        program(search)
                    
                    else:
                        number -= 2
                        startrow = (number-1) * perCount + 1 
                        endrow = startrow + perCount - 1
                        program(search)
                #----------------------------------------------------------------------
                elif no == 2: # 다음
                    # startrow = (number-1) * perCount + 1 
                    # endrow = startrow + perCount - 1 
                    limit = math.ceil(((all_count[0])/perCount))
                    if number > limit:  # page수가 limit을 넘어가지 않도록 제한
                        number = limit
                        startrow = (number-1) * perCount + 1 
                        endrow = startrow + perCount - 1 
                        program(search)
                    else:
                        startrow = (number-1) * perCount + 1 
                        ndrow = startrow + perCount - 1
                        program(search)
                #-----------------------------------------------------------------------
                else:
                    print("*** 선택된 서비스가 없습니다. 다시 입력해주세요 ***")
            
            number += 1   
            