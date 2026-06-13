import streamlit as st
import random
import time

st.set_page_config(
page_title="⚡ MBTI 포켓몬 매칭기",
page_icon="⚡",
layout="centered"
)

st.markdown("""

<style>

.main-title{
    text-align:center;
    font-size:2.3rem;
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

.stat-box{
    background:#f7f7f7;
    padding:12px;
    border-radius:12px;
    margin-top:10px;
}

</style>

""", unsafe_allow_html=True)

st.markdown(
'<div class="main-title">⚡ MBTI 포켓몬 매칭기 ⚡</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="sub-title">나와 가장 닮은 포켓몬을 찾아보자! 🎮</div>',
unsafe_allow_html=True
)

pokemon_data = {
"INTJ":{"name":"뮤츠","type":"🧠 초능력","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png","desc":"전략적이고 독립적인 천재형"},
"INTP":{"name":"후딘","type":"🔮 초능력","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png","desc":"아이디어 뱅크"},
"ENTJ":{"name":"리자몽","type":"🔥 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png","desc":"강력한 리더"},
"ENTP":{"name":"팬텀","type":"👻 고스트","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png","desc":"창의적인 혁신가"},
"INFJ":{"name":"루기아","type":"🌊 비행","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png","desc":"깊은 통찰력"},
"INFP":{"name":"이브이","type":"🌈 노말","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png","desc":"따뜻한 감성"},
"ENFJ":{"name":"피카츄","type":"⚡ 전기","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png","desc":"인기 만점 친구"},
"ENFP":{"name":"토게피","type":"🥚 페어리","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png","desc":"행복 전도사"},
"ISTJ":{"name":"거북왕","type":"💧 물","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png","desc":"책임감 최고"},
"ISFJ":{"name":"해피너스","type":"💖 노말","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png","desc":"배려심 넘침"},
"ESTJ":{"name":"코뿌리","type":"🦏 땅","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png","desc":"강한 책임감"},
"ESFJ":{"name":"푸린","type":"🎤 페어리","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png","desc":"분위기 메이커"},
"ISTP":{"name":"한카리아스","type":"🐉 드래곤","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png","desc":"문제 해결 능력"},
"ISFP":{"name":"나인테일","type":"✨ 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png","desc":"감성적인 자유인"},
"ESTP":{"name":"번치코","type":"🥊 불꽃","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png","desc":"도전 정신"},
"ESFP":{"name":"꼬부기","type":"😎 물","image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png","desc":"즐거움을 만드는 스타"}
}

mbti = st.selectbox(
"🎯 나의 MBTI",
[""] + list(pokemon_data.keys())
)

friend_mbti = st.selectbox(
"❤️ 친구 MBTI (궁합 테스트)",
[""] + list(pokemon_data.keys())
)

if st.button("⚡ 포켓몬 찾기", use_container_width=True):

```
if mbti == "":
    st.warning("MBTI를 선택해주세요!")
    st.stop()

holder = st.empty()

for ball in ["⚪🔴","🔴⚪","⚪🔴","🔴⚪","✨⚪🔴✨"]:
    holder.markdown(
        f"<h1 style='text-align:center'>{ball}</h1>",
        unsafe_allow_html=True
    )
    time.sleep(0.25)

holder.empty()

progress = st.progress(0)

for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.01)

result = pokemon_data[mbti]

st.balloons()

st.image(result["image"], width=180)

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

attack = random.randint(60,100)
defense = random.randint(60,100)
speed = random.randint(60,100)

st.markdown("### ⚔️ 포켓몬 능력치")

st.write(f"공격력 {attack}")
st.progress(attack)

st.write(f"방어력 {defense}")
st.progress(defense)

st.write(f"스피드 {speed}")
st.progress(speed)

rank = random.choice([
    "🥉 브론즈 트레이너",
    "🥈 실버 트레이너",
    "🥇 골드 트레이너",
    "💎 다이아 트레이너",
    "👑 챔피언"
])

st.success(f"🏆 나의 등급: {rank}")

level = random.randint(1,100)
st.metric("🎮 트레이너 레벨", level)

dex = random.randint(20,100)
st.write(f"📖 포켓몬 도감 완성률 {dex}%")
st.progress(dex)

if friend_mbti:
    compatibility = random.randint(60,100)

    st.metric(
        "❤️ 궁합",
        f"{compatibility}%"
    )

    if compatibility >= 90:
        st.success("💖 소울메이트!")
    elif compatibility >= 80:
        st.success("💕 최고의 친구!")
    elif compatibility >= 70:
        st.info("😊 잘 맞는 편!")
    else:
        st.warning("😅 가끔 싸울 수도 있어요!")

fortunes = [
    "✨ 오늘은 행운이 가득!",
    "🔥 새로운 도전에 좋은 날!",
    "💎 좋은 소식이 찾아올지도!",
    "🎯 목표 달성 확률 상승!",
    "⚡ 자신감이 최고조!"
]

st.info(random.choice(fortunes))

if random.randint(1,100) <= 3:
    st.success("🌟 전설의 포켓몬이 당신을 지켜보고 있습니다!")
    st.balloons()
```

st.caption("Made with ❤️ Pokémon + MBTI")
