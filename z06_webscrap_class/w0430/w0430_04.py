import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

while True:
    search = input("찾고자 하는 이름을 입력하세요(종료: -1) : ")
    if search == '-1':
        print(">> 프로그램을 종료합니다.")
        break
    else:
        sql = f"select * from stu_score where name like '%{search}%' order by no"
        cursor.execute(sql)
        data = cursor.fetchall()
        print("[ 학생 성적 출력 ]")
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
    print()
print("-"*40)
conn.close()