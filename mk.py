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
    st.header("🔐 An toàn Thông tin")
    st.markdown("""
    ### 🧩 Tình huống:
    **Bạn nhận được email từ người lạ với tệp đính kèm. Bạn nên làm gì?**
    - ❌ Không mở tệp đính kèm không rõ nguồn gốc.
    - ✅ Kiểm tra kỹ địa chỉ người gửi.
    """)

    if st.button("👉 Trắc nghiệm ôn tập"):
        st.session_state.page = "Trắc nghiệm tự luyện"
        st.experimental_rerun()

elif page == "Kho tài liệu":
    st.header("Kho tài liệu")
    st.markdown("### Tài liệu PDF:")
    st.download_button("Tải PDF bài giảng", "fake_pdf", file_name="baigiang.pdf")

elif page == "Trắc nghiệm tự luyện":
    st.header("🧠 Trắc nghiệm tự luyện")

    # Dictionary lưu trữ danh sách câu hỏi cho từng chuyên đề
    question_bank = {
        "An toàn thông tin": [
            {
                "question": "1. Bạn nên làm gì khi nhận được email từ người lạ kèm tệp đính kèm?",
                "options": ["Mở ngay tệp để xem nội dung", "Chuyển tiếp cho bạn bè", "Không mở và xoá email", "Trả lời email đó"],
                "answer": "Không mở và xoá email"
            },
            {
                "question": "2. Mật khẩu mạnh nên bao gồm?",
                "options": ["Tên và ngày sinh", "Chỉ chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Mật khẩu dễ nhớ"],
                "answer": "Ký tự đặc biệt, số, chữ hoa thường"
            },
            {
                "question": "3. Khi truy cập Wi-Fi công cộng, bạn nên?",
                "options": ["Truy cập ngân hàng online", "Không dùng các dịch vụ quan trọng", "Gửi mật khẩu qua email", "Cập nhật hệ điều hành"],
                "answer": "Không dùng các dịch vụ quan trọng"
            }
        ],
        "Thiết kế web cơ bản": [
            {
                "question": "1. Thẻ nào dùng để tạo tiêu đề lớn nhất trong HTML?",
                "options": ["<title>", "<head>", "<h1>", "<header>"],
                "answer": "<h1>"
            },
            {
                "question": "2. Thuộc tính nào của CSS dùng để đổi màu chữ?",
                "options": ["font-size", "background-color", "color", "text-align"],
                "answer": "color"
            },
            {
                "question": "3. Cặp thẻ nào dùng để tạo liên kết đến trang web khác?",
                "options": ["<img>", "<a>", "<link>", "<div>"],
                "answer": "<a>"
            }
        ]
    }

    topic = st.selectbox("Chọn chuyên đề:", list(question_bank.keys()))
    questions = question_bank[topic]

    st.markdown("### Trả lời các câu hỏi:")

    user_answers = []
    for i, q in enumerate(questions):
        answer = st.radio(q["question"], q["options"], key=f"{topic}_q_{i}")
        user_answers.append(answer)

    if st.button("Nộp bài", key=f"{topic}_submit"):
        score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["answer"])
        st.success(f"✅ Bạn được {score}/{len(questions)} điểm")

        st.markdown("### Đáp án đúng:")
        for i, q in enumerate(questions):
            st.markdown(f"**Câu {i+1}:** {q['answer']}")


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
    
        
        
