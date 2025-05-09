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
### 💡 Giới thiệu:
Trang web này được xây dựng nhằm hỗ trợ học sinh THCS và THPT học tập và thực hành các kỹ năng **Tin học hiện đại** như:

- Lập trình Scratch
- Thiết kế Web cơ bản với HTML/CSS
- Tin học văn phòng (Word, Excel, PowerPoint)
- An toàn thông tin

---

### 🎯 Mục tiêu:
- Học qua thực hành
- Nâng cao tư duy logic và kỹ năng sử dụng máy tính
- Tự tin ứng dụng công nghệ trong học tập và đời sống

---

### 🗺️ Gợi ý phương pháp học tập:
1. **Bắt đầu với lý thuyết cơ bản**
2. **Xem video và làm bài tập**
3. **Làm trắc nghiệm ôn tập**
4. **Chia sẻ bài thực hành của bạn**
5. **Luyện kỹ các năng an toàn**
6. **Tăng cường mặt khẩu của bạn**
   **Lưu ý:** Bạn có thể chia sẻ các ý kiến cá nhân trong form nhaa!

---

### 🚀 Chuyên mục nổi bật:
- [🔧 Thiết kế Web cơ bản](#)
- [🔐 An toàn thông tin](#)
- [📁 Kho tài liệu thực hành](#)
- [🧠 Trắc nghiệm tự luyện](#)
- [💬 Góc chia sẻ bài làm](#)
- [🔑 Kiểm tra mặt khẩu](#)

---

### 🧭 Hướng dẫn:
- Dùng thanh bên trái để chọn chuyên mục.
- Mỗi mục có video, tài liệu và bài tập kèm theo.
- Đừng quên làm trắc nghiệm để kiểm tra kiến thức nhé!

---

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – **Ray Clifford**
""")

# --- Thiết kế Web ---
elif page == "Thiết kế Web cơ bản":
    st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")

    # Giới thiệu kiến thức
    st.markdown("""
    ### Giới thiệu nhanh:
    - **HTML**: Dùng để xây dựng cấu trúc trang web.
    - **CSS**: Dùng để tạo kiểu dáng (màu sắc, font chữ, bố cục).
    - Một số thẻ HTML cơ bản: `<h1>`, `<p>`, `<a>`, `<img>`, `<div>`
    - Một số thuộc tính CSS thường gặp: `color`, `font-size`, `margin`, `padding`, `background-color`
    """)

    # Ví dụ minh hoạ
    st.markdown("### Ví dụ đơn giản với HTML + CSS:")
    st.code("""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            h1 { color: blue; }
            p { font-size: 16px; }
        </style>
    </head>
    <body>
        <h1>Xin chào!</h1>
        <p>Đây là trang web đầu tiên của tôi.</p>
    </body>
    </html>
    """, language="html")

    # Nút tải file mẫu
    html_file = """
<!DOCTYPE html>
<html>
<head>
    <style>
        h1 { color: blue; }
        p { font-size: 16px; }
    </style>
</head>
<body>
    <h1>Xin chào!</h1>
    <p>Đây là trang web đầu tiên của tôi.</p>
</body>
</html>
"""
    st.download_button("Tải file HTML mẫu", html_file, file_name="mau_trang_web.html")

    # Thử thách thực hành
    st.markdown("""
    ### Thử thách:
    Tạo một trang web có:
    - Một tiêu đề lớn
    - Một đoạn văn mô tả
    - Một hình ảnh từ Internet
    - Một liên kết đến Google

    **Gợi ý:** Dùng các thẻ `<h1>`, `<p>`, `<img>`, `<a>`
    """)

    # Học thêm
    st.markdown("""
    ### Tài liệu thêm:
    - [Video hướng dẫn HTML cơ bản](https://www.youtube.com/watch?v=Ke90Tje7VS0)
    - [Tài liệu CSS tại W3Schools](https://www.w3schools.com/css/)
    """)

    # Mini quiz
    st.markdown("### Trắc nghiệm nhanh:")
    q1 = st.radio("1. Thẻ nào dùng để tạo tiêu đề lớn nhất?", ["<p>", "<h1>", "<title>", "<div>"], key="web_q1")
    q2 = st.radio("2. Thuộc tính nào để đổi màu chữ trong CSS?", ["font-size", "color", "background-color", "margin"], key="web_q2")
    
    if st.button("Nộp câu trả lời", key="submit_web_quiz"):
        score = 0
        if q1 == "<h1>": score += 1
        if q2 == "color": score += 1
        st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")
        if score == 2:
            st.balloons()

# --- An toàn thông tin ---
elif page == "An toàn thông tin":
    st.header("🔐 An toàn Thông tin")

    # Kiến thức cơ bản
    st.markdown("""
    ### Kiến thức cơ bản:
    - **Mật khẩu mạnh** nên có chữ hoa, chữ thường, số và ký tự đặc biệt.
    - **Không chia sẻ mật khẩu** qua email hay tin nhắn.
    - **Không nhấn vào liên kết lạ** trong email từ người lạ.
    - **Cập nhật phần mềm thường xuyên** để tránh lỗ hổng bảo mật.
    """)

    # Tình huống thực tế
    st.markdown("""
    ### Tình huống:
    Bạn nhận được email từ một địa chỉ lạ với tiêu đề "Bạn đã trúng thưởng!" và tệp đính kèm là file `.exe`.  
    **Bạn nên làm gì?**
    - Không mở tệp đính kèm
    - Kiểm tra địa chỉ người gửi
    - Báo cáo cho giáo viên hoặc quản trị mạng
    """)

    # Danh sách mẹo
    st.markdown("""
    ### Mẹo an toàn khi dùng Internet:
    - Sử dụng xác thực 2 yếu tố (2FA)
    - Không dùng chung một mật khẩu cho nhiều tài khoản
    - Không dùng Wi-Fi công cộng cho việc quan trọng
    - Đăng xuất sau khi dùng xong máy tính công cộng
    """)

    # Học thêm
    st.markdown("""
    ### Một số cách để phòng tránh:
    - [Video: Làm sao để an toàn trên mạng?](https://www.youtube.com/watch?v=1I4FZ6Nkm4A)
    - [Cẩm nang an toàn thông tin của VNPT](https://attt.vnpt.vn)
    """)

    # Trắc nghiệm nhỏ
    st.markdown("### Trắc nghiệm nhanh:")
    q1 = st.radio("1. Mật khẩu an toàn nên chứa?", [
        "Ngày sinh", "Chỉ chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Tên người thân"
    ], key="sec_q1")

    q2 = st.radio("2. Khi nhận được email lạ có tệp đính kèm, bạn nên?", [
        "Mở ngay để xem nội dung", "Xóa email và không mở tệp", "Chuyển tiếp cho bạn bè", "Trả lời email"
    ], key="sec_q2")

    if st.button("Nộp câu trả lời", key="submit_sec_quiz"):
        score = 0
        if q1 == "Ký tự đặc biệt, số, chữ hoa thường": score += 1
        if q2 == "Xóa email và không mở tệp": score += 1
        st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")

        if score == 2:
            st.balloons()

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
    st.markdown("Gửi qua Google Forms dưới đây:")
    st.markdown("[📎 Biểu mẫu gửi bài](https://forms.gle/...)")

# --- Kiểm tra mật khẩu ---
elif page == "Kiểm tra mật khẩu":
    st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")

    def calculate_strength(password):
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 5
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
