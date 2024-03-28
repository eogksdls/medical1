## 파일을 읽어와서 출력하시오

# 파일 열기
# medical1 폴더 안 mem.csv
# 상대 경로: medical1>HTML_class>h0327>aaa 폴더 안 medical1/HTML_class/h0327/aaa/mem2.csv
# 절대 경로: c:/workspace/medical1/HTML_class/h0327/aaa/mem2.csv
with open("c:/workspace/medical1/HTML_class/h0327/aaa/mem2.csv","r",encoding="UTF-8") as f:
    while True:
        text = f.readline().strip()
        if text == "": break
        mem = text.split(",")
        print(mem[1])
