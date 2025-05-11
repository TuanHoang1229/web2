import streamlit as st
import random
import string
import hashlib
import io
from PIL import Image

# --- Cấu hình trang ---
st.set_page_config(page_title="Tin Học Online", layout="wide")

# --- Logo & Tiêu đề ---
logo_url = "https://raw.githubusercontent.com/TuanHoang1229/web2/refs/heads/main/IMG_2935.JPG"
st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0;">
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" width="60" style="margin-right: 10px;">
            <h2 style="margin: 0; color: #40E0D0;">Tin Học Online</h2>
        </div>
    </div>
    <hr style="margin-top: 0;">
""", unsafe_allow_html=True)

# --- Tabs ---
tabs = st.tabs([
    "🏠 Trang chủ",
    "🔑 Kiểm tra mật khẩu",
    "🌐 Thiết kế Web cơ bản", 
    "🔐 An toàn thông tin",
    "📂 Kho tài liệu",
    "🧠 Trắc nghiệm",
    "💬 Góc chia sẻ",
])

# --- Trang Chủ ---
with tabs[0]:
    st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
    st.markdown("""
### 💡 Giới thiệu:
Trang web này được xây dựng nhằm hỗ trợ học sinh THPT học tập và thực hành các kỹ năng **Tin học hiện đại** như:

- Thiết kế Web cơ bản với HTML/CSS
- An toàn thông tin
- Kiểm tra mật khẩu

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
6. **Tăng cường mật khẩu của bạn**  
**Lưu ý:** Bạn có thể chia sẻ các ý kiến cá nhân trong form nhé!

---

### 🚀 Các chuyên mục nổi bật:
- [🔑 Kiểm tra mặt khẩu]
- [🔧 Thiết kế Web cơ bản]
- [🔐 An toàn thông tin]
- [📁 Kho tài liệu thực hành]
- [🧠 Trắc nghiệm tự luyện]
- [💬 Góc chia sẻ bài làm]

---

###  Hướng dẫn:
- Chọn các chuyên mục ở đầu trang.
- Mỗi mục có video, tài liệu và bài tập kèm theo.
- Đừng quên làm trắc nghiệm để kiểm tra kiến thức nhé!

---

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – **Ray Clifford**
""")

# --- Thiết kế Web ---
with tabs[2]:
    st.header("🖥️ Thiết kế Web cơ bản với HTML & CSS")
    st.markdown("""
### Giới thiệu nhanh:
- **HTML**: Dùng để xây dựng cấu trúc trang web.
- **CSS**: Dùng để tạo kiểu dáng (màu sắc, font chữ, bố cục).
- Một số thẻ HTML cơ bản: `<h1>`, `<p>`, `<a>`, `<img>`, `<div>`
- Một số thuộc tính CSS thường gặp: `color`, `font-size`, `margin`, `padding`, `background-color`
    """)

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

    st.markdown("""
### Thử thách:
Tạo một trang web có:
- Một tiêu đề lớn
- Một đoạn văn mô tả
- Một hình ảnh từ Internet
- Một liên kết đến Google

**Gợi ý:** Dùng các thẻ `<h1>`, `<p>`, `<img>`, `<a>`
    """)

    st.markdown("""
### Tài liệu thêm:
- [Video hướng dẫn HTML cơ bản](https://www.youtube.com/watch?v=Ke90Tje7VS0)
- [Tài liệu CSS tại W3Schools](https://www.w3schools.com/css/)
    """)

    st.markdown("### Trắc nghiệm nhanh:")
    q1 = st.radio("1. Thẻ nào dùng để tạo tiêu đề lớn nhất?", ["<p>", "<h1>", "<title>", "<div>"], key="web_q1")
    q2 = st.radio("2. Thuộc tính nào để đổi màu chữ trong CSS?", ["font-size", "color", "background-color", "margin"], key="web_q2")
    if st.button("Nộp câu trả lời", key="submit_web_quiz"):
        score = int(q1 == "<h1>") + int(q2 == "color")
        st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")
        if score == 2: st.balloons()

# --- An toàn thông tin ---
with tabs[3]:
    st.header("🔐 An toàn Thông tin")
    st.markdown("""
### Kiến thức cơ bản:
- **Mật khẩu mạnh** nên có chữ hoa, chữ thường, số và ký tự đặc biệt.
- **Không chia sẻ mật khẩu** qua email hay tin nhắn.
- **Không nhấn vào liên kết lạ** trong email từ người lạ.
- **Cập nhật phần mềm thường xuyên** để tránh lỗ hổng bảo mật.
    """)
    st.markdown("""
### Tình huống:
Bạn nhận được email từ một địa chỉ lạ với tiêu đề "Bạn đã trúng thưởng!" và tệp đính kèm là file `.exe`.  
**Bạn nên làm gì?**
- Không mở tệp đính kèm
- Kiểm tra địa chỉ người gửi
- Báo cáo cho giáo viên hoặc quản trị mạng
    """)
    st.markdown("""
### Mẹo an toàn khi dùng Internet:
- Sử dụng xác thực 2 yếu tố (2FA)
- Không dùng chung một mật khẩu cho nhiều tài khoản
- Không dùng Wi-Fi công cộng cho việc quan trọng
- Đăng xuất sau khi dùng xong máy tính công cộng
    """)
    st.markdown("""
### Một số cách để phòng tránh:
- [Video: Làm sao để an toàn trên mạng?](https://www.youtube.com/watch?v=1I4FZ6Nkm4A)
- [Cẩm nang an toàn thông tin của VNPT](https://attt.vnpt.vn)
    """)

    st.markdown("### Trắc nghiệm nhanh:")
    q1 = st.radio("1. Mật khẩu an toàn nên chứa?", [
        "Ngày sinh", "Chỉ chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Tên người thân"
    ], key="sec_q1")
    q2 = st.radio("2. Khi nhận được email lạ có tệp đính kèm, bạn nên?", [
        "Mở ngay để xem nội dung", "Xóa email và không mở tệp", "Chuyển tiếp cho bạn bè", "Trả lời email"
    ], key="sec_q2")
    if st.button("Nộp câu trả lời", key="submit_sec_quiz"):
        score = int(q1 == "Ký tự đặc biệt, số, chữ hoa thường") + int(q2 == "Xóa email và không mở tệp")
        st.success(f"✅ Bạn trả lời đúng {score}/2 câu.")
        if score == 2: st.balloons()

# --- Kho tài liệu ---
with tabs[4]:
    st.header("📚 Kho tài liệu")
    st.download_button("⬇️ Tải PDF bài giảng", "Nội dung giả định", file_name="baigiang.pdf")

# --- Trắc nghiệm tự luyện ---
with tabs[5]:
    st.header("🧠 Trắc nghiệm tự luyện")
    question_bank = {
        "An toàn thông tin": [...],
        "Thiết kế web cơ bản": [...],
    }
    topic = st.selectbox("Chọn chuyên đề:", list(question_bank.keys()))
    questions = question_bank[topic]
    st.markdown("### 📋 Trả lời câu hỏi:")
    user_answers = [st.radio(q["question"], q["options"], key=f"{topic}_{i}") for i, q in enumerate(questions)]
    if st.button("📤 Nộp bài"):
        score = sum(ua == q["answer"] for ua, q in zip(user_answers, questions))
        st.success(f"✅ Bạn được {score}/{len(questions)} điểm")
        if score == len(questions): st.balloons()
        st.markdown("### ✅ Đáp án:")
        for i, q in enumerate(questions):
            st.markdown(f"**Câu {i+1}:** {q['answer']}")

# --- Góc chia sẻ ---
with tabs[6]:
    st.header("📬 Góc chia sẻ - Gửi bài thực hành")
    st.markdown("📎 **Biểu mẫu sẽ được cập nhật sớm tại đây.**")

# --- Kiểm tra mật khẩu ---
with tabs[1]:
    st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")

    def calculate_strength(password):
        score = 0
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 2
        if any(c.isdigit() for c in password): score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
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
                buffer = io.StringIO()
                buffer.write(hashed + "\n")
                buffer.seek(0)
                st.success("Đã lưu mật khẩu dưới dạng SHA-256!")
                st.download_button("📥 Tải file SHA-256", buffer, file_name="saved_passwords.txt")
