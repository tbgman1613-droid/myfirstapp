import streamlit as st
import time

st.set_page_config(
    page_title="✨ MBTI 포켓몬 매칭기 ✨",
    page_icon="⚡",
    layout="centered"
)

# CSS 꾸미기
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #ff6b6b;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #666;
}

.result-box {
    padding: 20px;
    border-radius: 20px;
    background: linear-gradient(135deg, #ffeaa7, #fab1a0);
    color: black;
    text-align: center;
    font-size: 1.1rem;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
    animation: pop 0.8s ease;
}

@keyframes pop {
    0% {transform: scale(0.7);}
    100% {transform: scale(1);}
}

.pokemon {
    font-size: 4rem;
    text-align: center;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    0%,100% {transform: translateY(0);}
    50% {transform: translateY(-12px);}
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">⚡ MBTI 포켓몬 매칭기 ⚡</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">당신의 MBTI와 가장 닮은 포켓몬은 누구일까요? 🤔✨</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

pokemon_data = {
    "INTJ": ("뮤츠 🧠", "전략적이고 독립적인 천재형! 항상 큰 그림을 생각해요."),
    "INTP": ("후딘 🔮", "호기심이 많고 분석을 좋아하는 아이디어 뱅크!"),
    "ENTJ": ("리자몽 🔥", "카리스마 넘치는 리더! 목표를 향해 돌진합니다."),
    "ENTP": ("팬텀 👻", "재치 있고 창의적인 장난꾸러기 혁신가!"),

    "INFJ": ("루기아 🌊", "조용하지만 깊은 통찰력을 가진 수호자!"),
    "INFP": ("이브이 🌈", "순수하고 따뜻한 감성을 가진 몽상가!"),
    "ENFJ": ("피카츄 ⚡", "사람들을 밝게 만드는 인기 만점 친구!"),
    "ENFP": ("토게피 🥚", "에너지 넘치고 긍정적인 행복 전도사!"),

    "ISTJ": ("거북왕 💧", "책임감 있고 믿음직한 든든한 존재!"),
    "ISFJ": ("해피너스 💖", "친절함과 배려심이 넘치는 힐러형!"),
    "ESTJ": ("코리갑 🦏", "실행력이 뛰어나고 강한 책임감을 가진 리더!"),
    "ESFJ": ("푸린 🎤", "사교적이고 모두를 챙기는 분위기 메이커!"),

    "ISTP": ("한카리아스 🐉", "냉철하고 문제 해결 능력이 뛰어난 모험가!"),
    "ISFP": ("나인테일 ✨", "감성적이고 예술적인 매력을 가진 자유인!"),
    "ESTP": ("번치코 🥊", "도전 정신이 강하고 행동력이 넘치는 승부사!"),
    "ESFP": ("꼬부기 😎", "어디서나 즐거움을 만드는 슈퍼스타!")
}

mbti = st.selectbox(
    "🎯 당신의 MBTI를 선택하세요!",
    [""] + list(pokemon_data.keys())
)

if st.button("✨ 포켓몬 추천받기! ✨", use_container_width=True):

    if mbti == "":
        st.warning("⚠️ 먼저 MBTI를 선택해주세요!")
    else:
        progress = st.progress(0)

        messages = [
            "🔍 성격 분석 중...",
            "⚡ 포켓몬 도감 검색 중...",
            "🎉 결과를 찾았습니다!"
        ]

        status = st.empty()

        for i in range(100):
            progress.progress(i + 1)

            if i < 30:
                status.info(messages[0])
            elif i < 70:
                status.info(messages[1])
            else:
                status.success(messages[2])

            time.sleep(0.01)

        pokemon, desc = pokemon_data[mbti]

        st.balloons()

        st.markdown(
            f'<div class="pokemon">🎊</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-box">
                <h1>{pokemon}</h1>
                <p>{desc}</p>
                <br>
                🌟 당신은 {pokemon.split()[0]}와 가장 잘 어울립니다! 🌟
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("🎉 포켓몬 매칭 완료!")

        st.markdown("### 🏆 당신의 특징")
        st.write(f"👉 MBTI: **{mbti}**")
        st.write(f"👉 추천 포켓몬: **{pokemon}**")
        st.write("👉 자신만의 강점을 믿고 멋지게 성장해보세요! 🚀")

        st.snow()

st.write("")
st.caption("Made with ❤️ + Pokémon + MBTI")
