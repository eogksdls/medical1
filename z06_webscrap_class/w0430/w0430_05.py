import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# 평균점수를 입력받아 입력한 평균점수 이상의 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력받으면 프로그램 종료



while True:
    score = input("점수를 입력하세요(종료.-1) : ")
    
    if score == '-1':
        print(">> 프로그램을 종료합니다.")
        print("-"*70)
        break
    
    else:
        while True:
            question = input("입력하신 점수의 이상/미만를 선택하세요 : ")
            
            if question == '이상':
                sql = f"select * from stu_score where avg >= {score} order by rank"
                cursor.execute(sql)
                data = cursor.fetchall()
                
                print("\t[ 학생 성적 출력 ]")
                print("-"*70)
                print("학번\t이름\t\t국어\t영어\t수학\t합계\t평균\t등수")
                print("-"*70)
                for d in data:
                    print(d[0], end="\t")
                    print(f'{d[1]:<15}', end="\t")
                    print(d[2], end="\t")
                    print(d[3], end="\t")
                    print(d[4], end="\t")
                    print(d[5], end="\t")
                    print(round(d[6],1), end="\t")
                    print(d[7])
                print("-"*70)
                print(">> 출력된 데이터 개수 : ",len(data))
                break  
                
            elif question == '미만':
                sql = f"select * from stu_score where avg < {score} order by rank"
                cursor.execute(sql)
                data = cursor.fetchall()
                
                print("\t[ 학생 성적 출력 ]")
                print("-"*70)
                print("학번\t이름\t\t국어\t영어\t수학\t합계\t평균\t등수")
                print("-"*70)
                for d in data:
                    print(d[0], end="\t")
                    print(f'{d[1]:<15}', end="\t")
                    print(d[2], end="\t")
                    print(d[3], end="\t")
                    print(d[4], end="\t")
                    print(d[5], end="\t")
                    print(round(d[6],1), end="\t")
                    print(d[7])
                print("-"*70)
                print(">> 출력된 데이터 개수 : ",len(data)) 
                break
                    
            else:
                print("* 잘못 입력하셨습니다. 다시 입력해주세요. *")
    print()
    
conn.close
        
    