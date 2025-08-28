import streamlit as st
import random
import time

menu_db = [
    # 한식
    {"name": "비빔밥", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "김치찌개", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "된장찌개", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "불고기", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "제육볶음", "time": ["점심"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "갈비탕", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "떡볶이", "time": ["점심", "저녁"], "type": "한식", "mood": ["가벼운", "매운"]},
    {"name": "냉면", "time": ["점심"], "type": "한식", "mood": ["가벼운"]},
    {"name": "칼국수", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "부대찌개", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "삼계탕", "time": ["점심", "저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "콩나물국밥", "time": ["아침", "점심"], "type": "한식", "mood": ["든든한"]},
    {"name": "불닭볶음면", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운"]},
    {"name": "잔치국수", "time": ["점심"], "type": "한식", "mood": ["가벼운"]},
    {"name": "김밥", "time": ["아침", "점심"], "type": "한식", "mood": ["가벼운"]},
    {"name": "육개장", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "오징어볶음", "time": ["점심"], "type": "한식", "mood": ["매운"]},
    {"name": "닭갈비", "time": ["저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "감자탕", "time": ["저녁"], "type": "한식", "mood": ["든든한"]},
    {"name": "해장국", "time": ["아침", "점심"], "type": "한식", "mood": ["든든한"]},
    {"name": "곰탕", "time": ["아침", "점심"], "type": "한식", "mood": ["든든한"]},
    {"name": "순두부찌개", "time": ["점심", "저녁"], "type": "한식", "mood": ["매운", "든든한"]},
    {"name": "잡채", "time": ["점심", "저녁"], "type": "한식", "mood": ["가벼운"]},
    {"name": "콩국수", "time": ["점심"], "type": "한식", "mood": ["가벼운"]},
    {"name": "파전", "time": ["저녁"], "type": "한식", "mood": ["가벼운"]},
    {"name": "순대국", "time": ["아침", "점심"], "type": "한식", "mood": ["든든한"]},

    # 중식
    {"name": "짜장면", "time": ["점심", "저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "짬뽕", "time": ["점심", "저녁"], "type": "중식", "mood": ["매운", "든든한"]},
    {"name": "탕수육", "time": ["점심", "저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "깐풍기", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "마라탕", "time": ["점심", "저녁"], "type": "중식", "mood": ["매운"]},
    {"name": "마파두부", "time": ["저녁"], "type": "중식", "mood": ["매운"]},
    {"name": "볶음밥", "time": ["점심"], "type": "중식", "mood": ["든든한"]},
    {"name": "유산슬", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "양장피", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "마라샹궈", "time": ["저녁"], "type": "중식", "mood": ["매운", "든든한"]},
    {"name": "고추잡채", "time": ["저녁"], "type": "중식", "mood": ["매운"]},
    {"name": "동파육", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "팔보채", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "유린기", "time": ["점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "멘보샤", "time": ["점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "계란볶음밥", "time": ["아침", "점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "꿔바로우", "time": ["저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "고추기름면", "time": ["점심"], "type": "중식", "mood": ["매운"]},
    {"name": "홍콩식 완탕면", "time": ["점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "새우볶음밥", "time": ["점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "짬뽕밥", "time": ["점심"], "type": "중식", "mood": ["매운", "든든한"]},
    {"name": "볶음우동", "time": ["점심", "저녁"], "type": "중식", "mood": ["든든한"]},
    {"name": "고추잡채밥", "time": ["점심"], "type": "중식", "mood": ["매운"]},
    {"name": "계란탕", "time": ["아침", "점심"], "type": "중식", "mood": ["가벼운"]},
    {"name": "탕수육소스볶음밥", "time": ["점심"], "type": "중식", "mood": ["든든한"]},

    # 일식
    {"name": "돈카츠", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "규동", "time": ["점심"], "type": "일식", "mood": ["든든한"]},
    {"name": "스시", "time": ["점심", "저녁"], "type": "일식", "mood": ["가벼운"]},
    {"name": "우동", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "라멘", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한", "매운"]},
    {"name": "오므라이스", "time": ["아침", "점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "냉모밀", "time": ["점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "카레라이스", "time": ["점심"], "type": "일식", "mood": ["든든한"]},
    {"name": "타코야키", "time": ["점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "유부초밥", "time": ["아침", "점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "가츠동", "time": ["점심"], "type": "일식", "mood": ["든든한"]},
    {"name": "텐동", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "소바", "time": ["점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "멘치카츠", "time": ["저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "닭고기덮밥", "time": ["점심"], "type": "일식", "mood": ["든든한"]},
    {"name": "에비프라이", "time": ["저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "가라아게", "time": ["저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "일본식 샐러드", "time": ["아침", "점심"], "type": "일식", "mood": ["가벼운"]},
    {"name": "미소된장국", "time": ["아침"], "type": "일식", "mood": ["가벼운"]},
    {"name": "나또 정식", "time": ["아침"], "type": "일식", "mood": ["가벼운"]},
    {"name": "가츠카레", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "야키소바", "time": ["점심", "저녁"], "type": "일식", "mood": ["든든한"]},
    {"name": "돈부리", "time": ["점심"], "type": "일식", "mood": ["든든한"]},
    {"name": "오코노미야키", "time": ["점심", "저녁"], "type": "일식", "mood": ["가벼운"]},
    {"name": "모찌", "time": ["아침", "점심"], "type": "일식", "mood": ["가벼운"]},

    # 양식
    {"name": "파스타", "time": ["점심", "저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "스테이크", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "햄버거", "time": ["점심", "저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "피자", "time": ["점심", "저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "샐러드", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "수프", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "토스트", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "베이글", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "팬케이크", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "스무디", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "오믈렛", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "치킨샐러드", "time": ["점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "프렌치토스트", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "라자냐", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "크로와상 샌드위치", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "치킨랩", "time": ["점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "리조또", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "그릴치킨", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "에그베네딕트", "time": ["아침"], "type": "양식", "mood": ["가벼운"]},
    {"name": "미트볼 스파게티", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "리코타 치즈 샐러드", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "바질 페스토 파스타", "time": ["점심", "저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "치킨 알프레도", "time": ["저녁"], "type": "양식", "mood": ["든든한"]},
    {"name": "퀴노아 샐러드", "time": ["아침", "점심"], "type": "양식", "mood": ["가벼운"]},
    {"name": "클럽 샌드위치", "time": ["점심"], "type": "양식", "mood": ["든든한"]},
]

time_choice = st.selectbox("식사 시간 선택", ["아침", "점심", "저녁"])
type_choice = st.selectbox("음식 종류 선택", ["한식", "중식", "일식", "양식"])
mood_choice = st.selectbox("기분 선택", ["가벼운", "든든한", "매운"])

# 필터링
filtered_menus = [
    m for m in menu_db
    if time_choice in m["time"]
    and type_choice == m["type"]
    and mood_choice in m["mood"]
]

if not filtered_menus:
    st.warning("조건에 맞는 메뉴가 없습니다! 다른 옵션을 선택해보세요.")
else:
    roulette_placeholder = st.empty()

    if st.button("🎡 룰렛 돌리기!"):
        for i in range(20):
            choice = random.choice(filtered_menus)
            roulette_placeholder.markdown(f"### 🎯 {choice['name']}")
            time.sleep(0.1 + i * 0.02)

        final_choice = random.choice(filtered_menus)
        roulette_placeholder.markdown(f"## 🎉 오늘의 메뉴는? **{final_choice['name']}** 🎉")
