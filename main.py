import streamlit as st
import random
import time

st.set_page_config(
    page_title="⚡ MBTI 포켓몬 매칭기",
    page_icon="⚡",
    layout="centered"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:2.5rem;
    font-weight:900;
    color:#FFCB05;
    text-shadow:2px 2px #3B4CCA;
}

.sub-title{
    text-align:center;
    color:#555;
    margin-bottom:20px;
}

.result-card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0 4px 15px rgba(0,0,0,0.15);
    text-align:center;
    margin-top:15px;
}

.float-img{
    animation: float 2s ease-in-out infinite;
}

@keyframes float{
    0% {transform:translateY(0px);}
    50% {transform:translateY(-12px);}
    100% {transform:translateY(0px);}
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# 제목
# -------------------------
st.markdown(
    '<div class="main-title">⚡ MBTI 포켓몬 매칭기 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">당신과 가장 잘 어울리는 포켓몬을 찾아보세요! 🎮</div>',
    unsafe_allow_html=True
)

# -------------------------
# 데이터
# -------------------------
pokemon_data = {
    "INTJ": {"name":"뮤츠","type":"🧠 초능력","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png","desc":"전략적이고 독립적인 천재형"},
    "INTP": {"name":"후딘","type":"🔮 초능력","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png","desc":"분석을 좋아하는 아이디어 뱅크"},
    "ENTJ": {"name":"리자몽","type":"🔥 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png","desc":"강력한 리더십의 소유자"},
    "ENTP": {"name":"팬텀","type":"👻 고스트","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png","desc":"창의적인 혁신가"},
    "INFJ": {"name":"루기아","type":"🌊 비행","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png","desc":"깊은 통찰력을 가진 수호자"},
    "INFP": {"name":"이브이","type":"🌈 노말","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png","desc":"순수하고 따뜻한 감성"},
    "ENFJ": {"name":"피카츄","type":"⚡ 전기","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png","desc":"인기 만점 친구"},
    "ENFP": {"name":"토게피","type":"🥚 페어리","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png","desc":"행복 에너지 전도사"},
    "ISTJ": {"name":"거북왕","type":"💧 물","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png","desc":"믿음직한 책임감"},
    "ISFJ": {"name":"해피너스","type":"💖 노말","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png","desc":"배려심 넘치는 힐러"},
    "ESTJ": {"name":"코뿌리","type":"🦏 땅","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png","desc":"강한 책임감의 리더"},
    "ESFJ": {"name":"푸린","type":"🎤 페어리","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png","desc":"분위기 메이커"},
    "ISTP": {"name":"한카리아스","type":"🐉 드래곤","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png","desc":"문제 해결 능력이 뛰어남"},
    "ISFP": {"name":"나인테일","type":"✨ 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png","desc":"감성적인 자유인"},
    "ESTP": {"name":"번치코","type":"🥊 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png","desc":"도전 정신이 강함"},
    "ESFP": {"name":"꼬부기","type":"😎 물","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png","desc":"즐거움을 만드는 슈퍼스타"}
}

# -------------------------
# 입력
# -------------------------
mbti = st.selectbox(
    "🎯 MBTI 선택",
    [""] + list(pokemon_data.keys())
)

friend_mbti = st.selectbox(
    "❤️ 친구 MBTI (궁합 테스트)",
    [""] + list(pokemon_data.keys())
)

# -------------------------
# 버튼
# -------------------------
if st.button("✨ 포켓몬 추천받기! ✨", use_container_width=True):

    if mbti == "":
        st.warning("⚠️ MBTI를 선택해주세요!")
    else:

        # 포켓볼 연출
        holder = st.empty()

        for ball in ["⚪🔴","🔴⚪","⚪🔴","🔴⚪"]:
            holder.markdown(
                f"<h1 style='text-align:center'>{ball}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(0.2)

        holder.empty()

        # 진행바
        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.01)

        result = pokemon_data[mbti]

        st.balloons()

        # 이미지
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{result['image']}" width="180">
            </div>
            """,
            unsafe_allow_html=True
        )

        # 결과 카드
        st.markdown(
            f"""
            <div class="result-card">
                <h2>{result['name']}</h2>
                <h4>{result['type']}</h4>
                <p>{result['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(f"🎉 당신과 가장 잘 어울리는 포켓몬은 {result['name']}!")

        # 전투력
        power = random.randint(70, 100)
        st.metric("⚔️ 전투력", f"{power}/100")

        # 트레이너 레벨
        level = random.randint(1, 100)
        st.write(f"🏆 트레이너 레벨: {level}")
        st.progress(level)

        # 궁합
        if friend_mbti:
            compatibility = random.randint(60, 100)
            st.metric("❤️ 궁합", f"{compatibility}%")

        # 운세
        fortunes = [
            "✨ 오늘은 행운이 가득한 날!",
            "🎯 목표를 이루기 좋은 날!",
            "💎 예상치 못한 좋은 일이 생길 수 있어요!",
            "🔥 자신감이 크게 상승합니다!",
            "🚀 새로운 도전을 시작하기 좋은 날!"
        ]

        st.info(random.choice(fortunes))

        # 희귀 이벤트
        if random.randint(1,100) <= 3:
            st.success("🌟 전설의 포켓몬이 당신을 주목하고 있습니다!")

        st.snow()

st.caption("Made with ❤️ Pokémon + MBTI")
