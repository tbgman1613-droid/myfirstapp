import streamlit as st
import time
import random

st.set_page_config(
    page_title="⚡ MBTI 포켓몬 매칭기 ⚡",
    page_icon="⚡",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #f8f9fa 0%,
        #fff8dc 100%
    );
}

.main-title{
    text-align:center;
    font-size:3.2rem;
    font-weight:900;
    color:#ffcb05;
    text-shadow:
        3px 3px #3b4cca,
        -1px -1px #3b4cca;
}

.sub-title{
    text-align:center;
    color:#555;
    font-size:1.1rem;
    margin-bottom:20px;
}

.result-box{
    background:white;
    padding:25px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
    animation:pop 0.7s ease;
}

.pokemon{
    text-align:center;
    font-size:5rem;
    animation:bounce 1.2s infinite;
}

@keyframes bounce{
    0%,100%{
        transform:translateY(0px);
    }
    50%{
        transform:translateY(-12px);
    }
}

@keyframes pop{
    0%{
        opacity:0;
        transform:scale(0.7);
    }
    100%{
        opacity:1;
        transform:scale(1);
    }
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<div class="main-title">⚡ MBTI 포켓몬 매칭기 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">당신의 MBTI와 가장 닮은 포켓몬을 찾아드립니다! 🎮✨</div>',
    unsafe_allow_html=True
)

# -----------------------------
# 데이터
# -----------------------------
pokemon_data = {
    "INTJ": {
        "name":"뮤츠 🧠",
        "desc":"전략적이고 독립적인 천재형!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    },
    "INTP": {
        "name":"후딘 🔮",
        "desc":"호기심이 많고 분석을 좋아하는 아이디어 뱅크!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png"
    },
    "ENTJ": {
        "name":"리자몽 🔥",
        "desc":"카리스마 넘치는 리더!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png"
    },
    "ENTP": {
        "name":"팬텀 👻",
        "desc":"재치 있고 창의적인 혁신가!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png"
    },
    "INFJ": {
        "name":"루기아 🌊",
        "desc":"깊은 통찰력을 가진 수호자!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png"
    },
    "INFP": {
        "name":"이브이 🌈",
        "desc":"순수하고 따뜻한 감성을 가진 몽상가!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png"
    },
    "ENFJ": {
        "name":"피카츄 ⚡",
        "desc":"사람들을 밝게 만드는 인기 만점 친구!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    },
    "ENFP": {
        "name":"토게피 🥚",
        "desc":"에너지 넘치고 긍정적인 행복 전도사!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png"
    },
    "ISTJ": {
        "name":"거북왕 💧",
        "desc":"책임감 있고 믿음직한 든든한 존재!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png"
    },
    "ISFJ": {
        "name":"해피너스 💖",
        "desc":"친절함과 배려심이 넘치는 힐러형!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png"
    },
    "ESTJ": {
        "name":"코뿌리 🦏",
        "desc":"강한 책임감을 가진 리더!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png"
    },
    "ESFJ": {
        "name":"푸린 🎤",
        "desc":"모두를 챙기는 분위기 메이커!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"
    },
    "ISTP": {
        "name":"한카리아스 🐉",
        "desc":"냉철하고 문제 해결 능력이 뛰어난 모험가!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png"
    },
    "ISFP": {
        "name":"나인테일 ✨",
        "desc":"감성적이고 예술적인 자유인!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png"
    },
    "ESTP": {
        "name":"번치코 🥊",
        "desc":"도전 정신이 강한 승부사!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png"
    },
    "ESFP": {
        "name":"꼬부기 😎",
        "desc":"어디서나 즐거움을 만드는 슈퍼스타!",
        "image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"
    }
}

# -----------------------------
# 입력
# -----------------------------
mbti = st.selectbox(
    "🎯 MBTI를 선택하세요",
    [""] + list(pokemon_data.keys())
)

# -----------------------------
# 버튼
# -----------------------------
if st.button("✨ 포켓몬 추천받기! ✨", use_container_width=True):

    if mbti == "":
        st.warning("⚠️ MBTI를 먼저 선택해주세요!")
    else:

        # 포켓볼 애니메이션
        pokeball = st.empty()

        for ball in ["⚪🔴", "🔴⚪", "⚪🔴", "🔴⚪"]:
            pokeball.markdown(
                f"<h1 style='text-align:center'>{ball}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(0.2)

        pokeball.empty()

        # 진행바
        progress = st.progress(0)
        status = st.empty()

        for i in range(100):
            progress.progress(i + 1)

            if i < 30:
                status.info("🔍 성격 분석 중...")
            elif i < 70:
                status.info("⚡ 포켓몬 도감 검색 중...")
            else:
                status.success("🎉 결과를 찾았습니다!")

            time.sleep(0.01)

        result = pokemon_data[mbti]

        st.balloons()

        st.image(result["image"], width=220)

        st.markdown(
            f"""
            <div class="result-box">
                <h1>{result['name']}</h1>
                <p>{result['desc']}</p>
                <hr>
                <h3>🌟 당신과 가장 잘 어울리는 포켓몬입니다! 🌟</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        quotes = [
            "⚡ 전설은 오늘도 계속된다!",
            "🔥 리자몽도 인정한 잠재력!",
            "🌈 새로운 모험이 시작된다!",
            "💎 희귀 포켓몬급 매력을 보유 중!",
            "🚀 미래의 포켓몬 마스터 등장!",
            "🎉 오늘 운세 최고 등급!"
        ]

        st.success("🎊 포켓몬 매칭 완료!")

        st.markdown("### 🏆 당신의 특징")
        st.write(f"👉 MBTI : **{mbti}**")
        st.write(f"👉 추천 포켓몬 : **{result['name']}**")
        st.write(f"👉 {random.choice(quotes)}")

        st.snow()

st.write("")
st.caption("Made with ❤️ + Pokémon + MBTI")
