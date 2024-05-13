from datetime import datetime
# from 모듈 import 함수
import time



# strftime : 특정한 형태로 출력
for i in range(10):
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)



