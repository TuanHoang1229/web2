import streamlit as st
from PIL import Image
import random
import string
import hashlib

st.set_page_config(page_title="Học Tin Học", layout="wide")

# Sidebar navigation
pages = {
    "Trang chủ": "home",
    "Thiết kế Web cơ bản": "web_design",
    "An toàn thông tin": "cyber_security",
    "Kho tài liệu": "resources",
    "Trắc nghiệm tự luyện": "quiz",
    "Góc chia sẻ": "sharing",
    "Kiểm tra mật khẩu": "password_checker"
}

page = st.sidebar.radio("Chọn chuyên mục:", list(pages.keys()))

if page == "Trang chủ":
    st.title("Chào mừng đến với Website Học Tin Học")
    st.markdown("""
    ### Mục tiêu:
    Trang web hỗ trợ học sinh tiếp cận kiến thức Tin học thông qua các chuyên đề học tập, tài liệu, video và bài thực hành.

    ### Liên kết nhanh:
    - [Thiết kế Web](https://www.youtube.com/watch?v=f_YT3hqi6hc)
    - [An toàn thông tin](#)

    ### Tin mới:
    - Cập nhật thêm 5 bài trắc nghiệm mới về An toàn thông tin
    - Thêm file mẫu Word/Excel mới
    """)

elif page == "Thiết kế Web cơ bản":
    st.header("Thiết kế Web với HTML/CSS")
    st.markdown("""
    #### Hướng dẫn:
    ```html
    <!DOCTYPE html>
    <html>
    <head><title>Trang của tôi</title></head>
    <body><h1>Xin chào!</h1></body>
    </html>
    ```
    """)
    st.download_button("Tải mẫu trang web", "<html>...</html>", file_name="index.html")

elif page == "An toàn thông tin":
    st.header("An toàn Thông tin")
    st.markdown("""
    ### Tình huống:
    **Bạn nhận được email từ người lạ với tệp đính kèm. Bạn nên làm gì?**
    - Không mở tệp
    - Kiểm tra kỹ địa chỉ email
    """)
    st.markdown("[Trắc nghiệm ôn tập](https://forms.gle/...)")

elif page == "Kho tài liệu":
    st.header("Kho tài liệu")
    st.markdown("### Tài liệu PDF:")
    st.download_button("Tải PDF bài giảng", "fake_pdf", file_name="baigiang.pdf")

elif page == "Trắc nghiệm tự luyện":
    st.header("Trắc nghiệm tự luyện")
    st.markdown("Chọn chuyên đề:")
    topic = st.selectbox("Chuyên đề", [ "An toàn thông tin","Thiết kế web cơ bản"])
    st.markdown("Làm bài trắc nghiệm:")
    st.markdown(f"[Bắt đầu bài trắc nghiệm về {topic}](https://forms.gle/...)")

elif page == "Góc chia sẻ":
    st.header("Góc chia sẻ - Gửi bài thực hành")
    st.markdown("Gửi bài qua Google Forms:")
    st.markdown("[Biểu mẫu gửi bài](https://forms.gle/...)")
    st.markdown("Hoặc chia sẻ trên Notion (nếu có tài khoản).")

elif page == "Kiểm tra mật khẩu":
    # Tính độ mạnh mật khẩu
    def calculate_strength(password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in string.punctuation for c in password):
            strength += 1
        return strength
    
    # UI
    st.header("🔐 Trình tạo mật khẩu mạnh")
    
    length = st.number_input("Độ dài mật khẩu", min_value=6, max_value=100, value=12)
    
    if st.button("Tạo mật khẩu"):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        st.text_input("Mật khẩu của bạn", password)
        
        strength = calculate_strength(password)
        strength_labels = ["Rất yếu", "Yếu", "Trung bình", "Mạnh", "Rất mạnh"]
        st.progress(strength * 20)
        st.success(f"Độ mạnh: {strength_labels[strength - 1] if strength else 'Rất yếu'}")
    
        if st.button("Lưu mật khẩu (SHA-256)"):
            hashed = hashlib.sha256(password.encode()).hexdigest()
            with open("saved_passwords.txt", "a") as f:
                f.write(hashed + "\n")
            st.success("Đã lưu mật khẩu (dạng SHA-256) vào file.")
            
    def calculate_strength(password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1
        if any(c in string.punctuation for c in password):
            strength += 1
        return strength
    
    def password_strength_text(score):
        if score <= 2:
            return "❌ Yếu", "red"
        elif score == 3 or score == 4:
            return "⚠️ Trung bình", "orange"
        else:
            return "✅ Mạnh", "green"
    
    st.title("🔐 Kiểm tra độ mạnh của mật khẩu")
    
    password = st.text_input("Nhập mật khẩu:", type="password")
    
    if password:
        score = calculate_strength(password)
        strength_text, color = password_strength_text(score)
        
        st.markdown(f"**Đánh giá:** <span style='color:{color}'>{strength_text}</span>", unsafe_allow_html=True)
        st.progress(score * 20)
    
        
        
