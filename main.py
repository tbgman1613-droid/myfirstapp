import streamlit as st
import random
import time

st.set_page_config(
    page_title="포켓몬 MBTI 매칭기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": ("뮤츠", "🧠 전략적인 천재"),
    "INTP": ("후딘", "🔮 분석가"),
    "ENTJ": ("리자몽", "🔥 리더"),
    "ENTP": ("팬텀", "👻 혁신가"),
    "INFJ": ("루기아", "🌊 수호자"),
    "INFP": ("이브이", "🌈 몽상가"),
    "ENFJ": ("피카츄", "⚡ 인기만점"),
    "ENFP": ("토게피", "🥚 행복 전도사"),
    "ISTJ": ("거북왕", "💧 책임감"),
    "ISFJ": ("해피너스", "💖 배려왕"),
    "ESTJ": ("코뿌리", "🦏 관리자"),
    "ESFJ": ("푸린", "🎤 분위기 메이커"),
    "ISTP": ("한카리아스", "🐉 해결사"),
    "ISFP": ("나인테일", "✨ 예술가"),
    "ESTP": ("번치코", "🥊 승부사"),
    "ESFP": ("꼬부기", "😎 슈퍼스타")
}

st.title("⚡ 포켓몬 MBTI 매칭기 ⚡")
st.write("나와 가장 닮은 포켓몬을 찾아보자!")

mbti = st.selectbox(
    "MBTI 선택",
    [""] + list(pokemon_data.keys())
)

if st.button("✨ 포켓몬 찾기"):

    if mbti == "":
        st.warning("MBTI를 선택해주세요!")
    else:

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.01)

        pokemon, desc = pokemon_data[mbti]

        st.balloons()

        st.success(f"🎉 당신의 포켓몬은 {pokemon}!")

        st.markdown(f"## {pokemon}")
        st.write(desc)

        attack = random.randint(60, 100)
        defense = random.randint(60, 100)
        speed = random.randint(60, 100)

        st.subheader("⚔️ 능력치")

        st.write(f"공격력 {attack}")
        st.progress(attack)

        st.write(f"방어력 {defense}")
        st.progress(defense)

        st.write(f"스피드 {speed}")
        st.progress(speed)

        rank = random.choice([
            "🥉 브론즈",
            "🥈 실버",
            "🥇 골드",
            "💎 다이아",
            "👑 챔피언"
        ])

        st.success(f"🏆 트레이너 등급 : {rank}")
