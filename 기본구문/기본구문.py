import pandas as pd
df = pd.read_csv('score.xlsx',index_col='지원번호')
df

df['키']
df['이름']
df[['이름','키']]  # 컬럼 2개 이상부터 [[]] 이중 대괄호 사용

df.describe()  # 컬럼별 대략적 정보: min,max,mean..
df.head()      # 상단 5개 출력(개수 조절 가능)
df.tail()      # 하단 5개 출력
df.info()      # 컬럼별 타입,크기 정보
df.values      # rows 데이터 배열로 출력
df.index       # index 정보
df.columns     # 컬럼 정보
df.shape       # 데이터 크기 정보 (8,9) : 행 8개, 열 9개

# 문자열 함수
# slice :  df['key'].str.slice(0,3) 문자열로 바꿔준 후 슬라이싱

# df_str['idx'].map(lambda x:x[1:3])  # map(함수), lambda : 익명함수

# def d_map(x):
#     return x[1:3]
# df_str['idx'].map(d_map(x))
#------------------------------------------------------------

# split : 문자열 분리
a_list = ['데이터,분석가','영희,철수,바둑이','국어,영어,수학,과학,사회']
data = {"d_split":a_list}
df_str = pd.DataFrame(data)
s_data = df_str['d_split'].str.split(',')  # 쉼표로 되었는 부분을 기준으로 문자열을 분리해줘
s_data
#-------------------------------------------------------------

# replace : 문자열 처리, strip : 문자열 공백제거