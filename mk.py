import streamlit as st
import random
import string
import hashlib
from PIL import Image

# --- Cấu hình trang ---
st.set_page_config(page_title="Học Tin Học", layout="wide")

# Hiển thị ảnh góc trên bên trái
col1, col2 = st.columns([10, 1])
with col1:
    st.image("https://github.com/TuanHoang1229/web2/blob/main/IMG_2935.JPG", width=80)

# --- Khởi tạo session ---
if "page" not in st.session_state:
    st.session_state.page = "Trang chủ"

# --- Sidebar Navigation ---
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

# --- Trang Chủ ---
if page == "Trang chủ":
    st.title("📘 Chào mừng đến với Góc Tự Học Tin học")
    st.markdown("""
    ### 🎯 Mục tiêu:
    Trang web hỗ trợ học sinh tiếp cận kiến thức Tin học thông qua các chuyên đề học tập, tài liệu, video và bài thực hành.

    ### 🔗 Liên kết nhanh:
    - [Thiết kế Web](https://www.youtube.com/watch?v=f_YT3hqi6hc)
    - [An toàn thông tin](#)

    ### 📰 Tin mới:
    - ✅ Cập nhật thêm 5 bài trắc nghiệm mới về An toàn thông tin
    - ✅ Thêm file mẫu Word/Excel mới
    """)

# --- Thiết kế Web ---
elif page == "Thiết kế Web cơ bản":
    st.header("💻 Thiết kế Web với HTML/CSS")
    st.markdown("""
    #### Ví dụ cơ bản:
    ```html
    <!DOCTYPE html>
    <html>
    <head><title>Trang của tôi</title></head>
    <body><h1>Xin chào!</h1></body>
    </html>
    ```
    """)
    st.download_button("⬇️ Tải mẫu trang web", "<html><body><h1>Xin chào!</h1></body></html>", file_name="index.html")

# --- An toàn thông tin ---
elif page == "An toàn thông tin":
    st.header("🔐 An toàn Thông tin")
    st.markdown("""
    ### 🧩 Tình huống:
    **Bạn nhận được email từ người lạ với tệp đính kèm. Bạn nên làm gì?**
    - ❌ Không mở tệp đính kèm không rõ nguồn gốc.
    - ✅ Kiểm tra kỹ địa chỉ người gửi.
    """)



# --- Kho tài liệu ---
elif page == "Kho tài liệu":
    st.header("📚 Kho tài liệu")
    st.markdown("### Tài liệu PDF:")
    st.download_button("⬇️ Tải PDF bài giảng", "Nội dung giả định", file_name="baigiang.pdf")

# --- Trắc nghiệm tự luyện ---
elif page == "Trắc nghiệm tự luyện":
    st.header("🧠 Trắc nghiệm tự luyện")

    question_bank = {
        "An toàn thông tin": [
            {
                "question": "Câu hỏi 1: Bạn nên làm gì khi nhận được email từ người lạ kèm tệp đính kèm?",
                "options": ["Mở ngay tệp để xem", "Chuyển tiếp", "Không mở và xoá email", "Trả lời email"],
                "answer": "Không mở và xoá email"
            },
            {
                "question": "Câu hỏi 2: Mật khẩu mạnh nên bao gồm?",
                "options": ["Tên", "Chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Dễ nhớ"],
                "answer": "Ký tự đặc biệt, số, chữ hoa thường"
            },
            {
                "question": "Câu hỏi 3. Khi truy cập Wi-Fi công cộng, bạn nên?",
                "options": ["Ngân hàng online", "Không dùng dịch vụ quan trọng", "Gửi mật khẩu", "Cập nhật hệ điều hành"],
                "answer": "Không dùng dịch vụ quan trọng"
            }
        ],
        "Thiết kế web cơ bản": [
            {
                "question": "Câu hỏi 1: Thẻ nào tạo tiêu đề lớn nhất trong HTML?",
                "options": ["<title>", "<head>", "<h1>", "<header>"],
                "answer": "<h1>"
            },
            {
                "question": "Câu hỏi 2: CSS thuộc tính nào đổi màu chữ?",
                "options": ["font-size", "background-color", "color", "text-align"],
                "answer": "color"
            },
            {
                "question": "Câu hỏi 3: Thẻ nào tạo liên kết web?",
                "options": ["<img>", "<a>", "<link>", "<div>"],
                "answer": "<a>"
            }
        ]
    }

    topic = st.selectbox("Chọn chuyên đề:", list(question_bank.keys()))
    questions = question_bank[topic]

    st.markdown("### 📋 Trả lời câu hỏi:")

    user_answers = []
    for i, q in enumerate(questions):
        ans = st.radio(q["question"], q["options"], key=f"{topic}_{i}")
        user_answers.append(ans)

    if st.button("📤 Nộp bài"):
        score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["answer"])
        st.success(f"✅ Bạn được {score}/{len(questions)} điểm")
        if score == len(questions):
            st.balloons()

        st.markdown("### ✅ Đáp án:")
        for i, q in enumerate(questions):
            st.markdown(f"**Câu {i+1}:** {q['answer']}")

# --- Góc chia sẻ ---
elif page == "Góc chia sẻ":
    st.header("📬 Góc chia sẻ - Gửi bài thực hành")
    st.markdown("Gửi bài qua Google Forms:")
    st.markdown("[📎 Biểu mẫu gửi bài](https://forms.gle/...)")

# --- Kiểm tra mật khẩu ---
elif page == "Kiểm tra mật khẩu":
    st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")

    def calculate_strength(password):
        score = 0
        if len(password) >= 8: score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        return score

    def strength_text(score):
        if score <= 2: return "❌ Yếu", "red"
        elif score <= 4: return "⚠️ Trung bình", "orange"
        else: return "✅ Mạnh", "green"

    tab1, tab2 = st.tabs(["🔎 Kiểm tra mật khẩu", "⚙️ Tạo mật khẩu mới"])

    with tab1:
        pwd = st.text_input("Nhập mật khẩu:", type="password")
        if pwd:
            score = calculate_strength(pwd)
            text, color = strength_text(score)
            st.markdown(f"**Đánh giá:** <span style='color:{color}'>{text}</span>", unsafe_allow_html=True)
            st.progress(score * 20)

    with tab2:
        length = st.slider("Chọn độ dài mật khẩu", 6, 50, 12)
        if st.button("🎲 Tạo mật khẩu"):
            chars = string.ascii_letters + string.digits + string.punctuation
            gen_pwd = ''.join(random.choice(chars) for _ in range(length))
            st.text_input("🔑 Mật khẩu đã tạo:", gen_pwd)

            score = calculate_strength(gen_pwd)
            text, color = strength_text(score)
            st.markdown(f"**Độ mạnh:** <span style='color:{color}'>{text}</span>", unsafe_allow_html=True)
            st.progress(score * 20)

            if st.button("💾 Lưu mật khẩu SHA-256"):
                hashed = hashlib.sha256(gen_pwd.encode()).hexdigest()
                with open("saved_passwords.txt", "a") as f:
                    f.write(hashed + "\n")
                st.success("Đã lưu mật khẩu dưới dạng SHA-256!")

                with open("saved_passwords.txt", "r") as f:
                    st.download_button("📥 Tải file SHA-256", f.read(), file_name="saved_passwords.txt")
