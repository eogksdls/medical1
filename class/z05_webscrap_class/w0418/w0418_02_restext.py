import requests
url = "http://www.google.com"
res = requests.get(url) # 동기식 방식
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

print("페이지의 글자수 : ",len(res.text))
print("[웹페이지 소스코드]")
print(res.text) # 소스를 가져옴. 타입 : str

# 파일 저장
with open('google.html','w',encoding='utf-8') as f:
    f.write(res.text)

