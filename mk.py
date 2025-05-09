import streamlit as st
import string

st.set_page_config(page_title="Kiểm tra mật khẩu", layout="centered")

# CSS tuỳ chỉnh cho giao diện giống Locker.io
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        padding: 3rem 2rem;
        border-radius: 10px;
        max-width: 600px;
        margin: auto;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .password-input input {
        font-size: 20px !important;
        padding: 0.75rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>🔐 Kiểm tra độ mạnh của mật khẩu</h1>", unsafe_allow_html=True)
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Hàm đánh giá mật khẩu
def calculate_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    return score

# Hàm đánh giá chữ + màu
def get_strength_feedback(score):
    if score <= 2:
        return "❌ Mật khẩu yếu", "red"
    elif score == 3 or score == 4:
        return "⚠️ Mật khẩu trung bình", "orange"
    else:
        return "✅ Mật khẩu mạnh", "green"

# Ô nhập mật khẩu
password = st.text_input("Nhập mật khẩu của bạn:", type="password", key="password", help="Không lưu trữ mật khẩu bạn nhập")

if password:
    score = calculate_strength(password)
    feedback, color = get_strength_feedback(score)

    # Hiển thị kết quả
    st.markdown(f"<h4 style='color:{color}'>{feedback}</h4>", unsafe_allow_html=True)
    st.progress(score * 20)

    # Mẹo cải thiện
    if score < 5:
        st.markdown("**Mẹo để cải thiện mật khẩu:**")
        tips = []
        if len(password) < 8:
            tips.append("- Tăng độ dài lên ít nhất 8 ký tự")
        if not any(c.islower() for c in password):
            tips.append("- Thêm chữ thường")
        if not any(c.isupper() for c in password):
            tips.append("- Thêm chữ in hoa")
        if not any(c.isdigit() for c in password):
            tips.append("- Thêm số")
        if not any(c in string.punctuation for c in password):
            tips.append("- Thêm ký tự đặc biệt (!@#$...)")
        st.markdown("\n".join(tips))

st.markdown("</div>", unsafe_allow_html=True)
