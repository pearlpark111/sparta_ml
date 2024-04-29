!pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache  # 데이터 캐싱을 통해 성능 향상
def load_data():
    df = pd.read_csv("your_dataset.csv")
    return df

df = load_data()

# 제목
st.title("Apartment/Condo Rental Dashboard")

# 사이드바: 가격 필터링
price_range = st.sidebar.slider("Price Range (CAD)", float(df["Price"].min()), float(df["Price"].max()), (float(df["Price"].min()), float(df["Price"].max())))

# 데이터 필터링
filtered_df = df[(df["Price"] >= price_range[0]) & (df["Price"] <= price_range[1])]

# 지도 시각화
st.subheader("Map of Apartments/Condos")
st.map(filtered_df)

# 다른 필터링 옵션 추가
# 예: 객실 수, 용적, 반려동물 허용 여부 등

# 필터링된 데이터 표시
st.subheader("Filtered Data")
st.write(filtered_df)

# 데이터 시각화: 가격 분포
st.subheader("Price Distribution")
fig = px.histogram(filtered_df, x="Price", nbins=20)
st.plotly_chart(fig, use_container_width=True)
