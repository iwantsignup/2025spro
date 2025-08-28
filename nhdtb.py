import streamlit as st
import random

# 식사 메뉴 데이터 (카테고리별)
menu_db = [
    {"name": "김치찌개", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "비빔밥", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "토스트", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "우동", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "파스타", "time": ["점심", "저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "샐러드", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "짜장면", "time": ["점심", "저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "삼겹살", "time": ["저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "불닭볶음면", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운"]},
    {"name": "오므라이스", "time": ["아침", "점심"], "type": "일식", "mood": ["가벼운"]},
]

# Streamlit UI
st.title("🍱 식사 메뉴 추천기")

# 사용자 입력 받기
meal_time = st.selectbox("🍽️ 식사 시간", ["아침", "점심", "저녁"])
food_type = st.selectbox("🌏 음식 종류", ["한식", "중식", "일식", "양식"])
mood = st.selectbox("😋 식사 기분", ["가벼운", "든든한", "매운"])

# 추천 버튼
if st.button("🥄 메뉴 추천받기"):
    # 조건에 맞는 메뉴 필터링
    filtered_menu = [
        item["name"] for item in menu_db
        if meal_time in item["time"]
        and item["type"] == food_type
        and mood in item["mood"]
    ]
    
    if filtered_menu:
        recommended = random.choice(filtered_menu)
        st.success(f"👉 오늘 추천 메뉴: **{recommended}** 🍽️")
    else:
        st.warning("😥 조건에 맞는 메뉴가 없어요. 다른 옵션으로 시도해보세요!")

