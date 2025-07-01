
import streamlit as st
from ocr import extract_words
from quiz import make_quiz

st.set_page_config(page_title="영어 단어 암기앱", layout="centered")
st.title("📘 영어 단어 외우기 앱")

step = st.radio("단계 선택", ['1단계: 단어장 이미지 업로드', '2단계: 퀴즈 풀기'])

if step == '1단계: 단어장 이미지 업로드':
    uploaded_file = st.file_uploader("📷 단어장 이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        words = extract_words("temp.jpg")
        st.success(f"✅ {len(words)}개의 단어 인식 완료!")
        st.json(words)

elif step == '2단계: 퀴즈 풀기':
    mode = st.selectbox("모드 선택", ['영어 → 뜻', '뜻 → 영어', '랜덤'])
    mode_map = {'영어 → 뜻': 1, '뜻 → 영어': 2, '랜덤': 3}
    quiz = make_quiz(mode_map[mode])

    score = 0
    user_answers = []

    with st.form("quiz_form"):
        for i, (question, answer) in enumerate(quiz):
            user_input = st.text_input(f"Q{i+1}. {question}", key=i)
            user_answers.append((user_input.strip(), answer))
        submitted = st.form_submit_button("채점하기")

    if submitted:
        correct = 0
        for user, answer in user_answers:
            if user.lower() == answer.lower():
                correct += 1
        st.success(f"🎉 총 {len(user_answers)}문제 중 {correct}개 정답!\n점수: {int(correct/len(user_answers)*100)}점")
