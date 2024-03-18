class Tv :   # 객체선언 대문자
    channel = 0
    colocr= "black"
    size = 65
    volume = 0
    
    # 생성자 선언
    def __init__(self,chan=0,col="",size=0,vol=0):  # 위 변수와 다른 변수임(헷갈리지 않게 변수이름 다르게...)
        self.channel = chan
        self.color = col
        self.size = size
        self.volume = vol
    
    def up_volnm(self,volume):
        self.volume += volume
    def down_volnm(self,volume):
        self.volume -= volume
    
    def up_channel(self,channel):
        self.channel += channel
    def down_channel(self,channel):
        self.channel -= channel
    
# 철수 - 화이트10, 영희 - 핑크7, 반장 - 실버1
# 철수
c1 = Tv(10,"white",65,0)
c1.up_channel(2)
print("철수: ",c1.channel,c1.colocr,c1.size,c1.volume)

# 영희
c2 = Tv(7,"pink",65,0)
c2.up_channel(5)
print("영희: ",c2.channel,c2.colocr,c2.size,c2.volume)

# 반장
c3 = Tv(1,"silver",65,0)
c3.up_channel(3)
print("반장: ",c3.channel,c3.colocr,c3.size,c3.volume)

