import requests
# 웹에 접근해서 html 소스를 가져옴
# res = requests.get("https://www.google.com/")   # Response [200]
res = requests.get("https://www.daum.net//")      # Response [200]
res = requests.get("https://www.melon.com/index.htm")    # Response [406] -> 웹서핑 과부하, 차단된거임
# 200: 정상
# 403 & 404: 페이지 없음(클라이언트 오류, 내가잘못)
# 500: 프로그램 에러(서버 오류, 상대방이잘못)
print(res) # 코드상태 출력
print("코드 : ",res.status_code)    # 리턴한 소스의 코드값을 출력
print(type(res.status_code))
if res.status_code == requests.codes.ok:   # requests.codes.ok : 200
    print("정상 페이지 호출입니다.")
else:
    print("Error코드 발생")

res.raise_for_status()  # 코드가 2XX이 아니면 오류처리해서 자동으로 멈추게 해줌


print('-'*40)
# requests를 통해 html소스를 출력
print(res.text)