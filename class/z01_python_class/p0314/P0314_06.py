a_list = [1,2,3]
try:
    raise "에러발생" # 강제 에러 발생구문
    print(a_list[5])
    print(1/0)
    txt = int(input("숫자를 입력하세요:  "))
    print(txt)

except IndexError:  # 에러 종류에 따라서 세부적인 예외처리 가능
    print("리스트 주소가 잘못 입력되었습니다.")
except Exception as e:
    print("-- 예외가 발생했습니다.")
    print("타입: ",type(e))
    print(e)