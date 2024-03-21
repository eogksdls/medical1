import requests

# 웹 크롤링 형태
# res = requests.get("https://www.google.com/")
res = requests.get("https://www.naver.com/")
res.raise_for_status()  # 에러코드이면 자동 멈춤
print(res.text)
print("총 문자 길이 : ",len(res.text))

with open("google.html","w",encoding="utf-8") as f:
    f.write(res.text)
