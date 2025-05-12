import streamlit as st
import random
import string
import hashlib
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


st.image(
    "https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/304851178_540789087851004_9097165287000760892_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=gHy6kXCaw2AQ7kNvwE-PviU&_nc_oc=Admrg-I1Ihfs1OeVmhVMDCN2WjDhY-G92J9d7FWnfMrm3PH2DaIHFPtWsp3spMJ7lTA&_nc_zt=23&_nc_ht=scontent.fhan3-2.fna&_nc_gid=zUR1Tl_81MyfEa2IiZydTg&oh=00_AfJdAFQuQ6pb2wh4fVJ3RBHgdKJnQDRy9rhd0jvLBUbplQ&oe=6825F9BA",
    use_container_width=True,
    caption="📸 Trường THPT Lương Văn Tri"
)

# --- Tabs ---
tabs = st.tabs([
    "🏠 Trang chủ",
    "🔑 Kiểm tra mật khẩu",
    "🌐 Thiết kế Web cơ bản", 
    "🔐 An toàn thông tin",
    "📂 Kho tài liệu",
    "💬 Góc chia sẻ",
])

# --- Trang Chủ ---
with tabs[0]:
    st.title("📘 Chào mừng bạn đến với Góc Tự Học Tin học")
    st.markdown("""
## 💡 Giới thiệu:
Trang web này được xây dựng nhằm hỗ trợ học sinh THPT học tập và thực hành các kỹ năng **Tin học hiện đại** như:

 - Kiểm tra độ an toàn của mặt khẩu
 - Thiết kế Web cơ bản với HTML/CSS
 - An toàn thông tin
 - Tự học và kiểm tra kiến thức đã học

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
6. **Tăng cường mặt khẩu của bạn**\n**Lưu ý:** Bạn có thể chia sẻ các ý kiến cá nhân trong form nhaa!

---

### 🚀 Các chuyên mục nổi bật:
- [🔑 Kiểm tra mặt khẩu]
- [🔧 Thiết kế Web cơ bản]
- [🔐 An toàn thông tin]
- [📁 Kho tài liệu thực hành]
- [🧠 Trắc nghiệm tự luyện]
- [💬 Góc chia sẻ và nộp bài]

---

###  Hướng dẫn:
- Chọn các chuyên mục ở đầu trang.
- Mỗi mục có video, tài liệu và bài tập kèm theo.
- Đừng quên làm trắc nghiệm để kiểm tra kiến thức nhé!

---

> **“Công nghệ sẽ không thay thế giáo viên, nhưng giáo viên biết công nghệ sẽ thay thế người không biết.”**  
> – **Ray Clifford**
""")

     # --- Gạch ngang ---
    st.markdown("<hr style='margin-top: 0;'>", unsafe_allow_html=True)

    # Nội dung "Liên hệ + Góp ý"
    st.markdown('<div class="box">', unsafe_allow_html=True)
    
    # Thông tin liên hệ
    st.markdown("<h3>Liên hệ</h3>", unsafe_allow_html=True)
    st.markdown('<div class="contact-item">📍 <strong>Địa chỉ:</strong> Trường THPT Lương Văn Tri</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">📧 <strong>Email:</strong> ContactLVT@edu.vn</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">📞 <strong>Số điện thoại:</strong> 0966 813 528</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">👤 <strong>Người thực hiện:</strong> Hoàng Minh Tuấn</div>', unsafe_allow_html=True)
    
    # Góp ý kiến
    st.markdown("<h3 style='margin-top:40px;'>Góp ý kiến</h3>", unsafe_allow_html=True)
    feedback = st.text_area("Nhập ý kiến của bạn", height=120, label_visibility="collapsed")
    
    if st.button("Gửi"):
        if feedback.strip():
            st.success("✅ Cảm ơn bạn đã góp ý!")
        else:
            st.warning("⚠️ Vui lòng nhập nội dung góp ý.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- Thiết kế Web ---
with tabs[2]:
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
    st.download_button("⬇️ Tải file HTML mẫu", html_file, file_name="mau_trang_web.html")

    # Thử thách thực hành
    st.markdown("""
    ### 🧪 Thử thách:
    Tạo một trang web có:
    - Một tiêu đề lớn
    - Một đoạn văn mô tả
    - Một hình ảnh từ Internet
    - Một liên kết đến Google

    **Gợi ý:** Dùng các thẻ `<h1>`, `<p>`, `<img>`, `<a>`
    """)

    # Học thêm
    st.markdown("""
    ### 📘 Tài liệu thêm:
    - [🎥 Video hướng dẫn HTML cơ bản](https://www.youtube.com/watch?v=Ke90Tje7VS0)
    - [🌐 Tài liệu CSS tại W3Schools](https://www.w3schools.com/css/)
    """)

    # Mini quiz
    st.markdown("### 🧠 Trắc nghiệm nhanh:")

    q1 = st.radio("1. Thẻ nào dùng để tạo tiêu đề lớn nhất?", ["<p>", "<h1>", "<title>", "<div>"], key="web_q1")
    q2 = st.radio("2. Thuộc tính nào để đổi màu chữ trong CSS?", ["font-size", "color", "background-color", "margin"], key="web_q2")
    q3 = st.radio("3. Thẻ nào dùng để chèn hình ảnh vào trang web?", ["<a>", "<img>", "<picture>", "<div>"], key="web_q3")
    q4 = st.radio("4. Trong CSS, thuộc tính `padding` dùng để làm gì?", ["Tạo khoảng cách bên trong phần tử", "Đổi màu nền", "Tạo đường viền", "Tăng cỡ chữ"], key="web_q4")
    q5 = st.radio("5. Đoạn mã nào tạo liên kết đến Google?", [
        "<link href='google.com'>Google</link>", 
        "<a>Google</a>", 
        "<a href='https://google.com'>Google</a>", 
        "<p href='google.com'>Google</p>"
    ], key="web_q5")

    if st.button("✅ Nộp câu trả lời", key="submit_web_quiz"):
        score = 0
        if q1 == "<h1>": score += 1
        if q2 == "color": score += 1
        if q3 == "<img>": score += 1
        if q4 == "Tạo khoảng cách bên trong phần tử": score += 1
        if q5 == "<a href='https://google.com'>Google</a>": score += 1

        st.success(f"📊 Bạn trả lời đúng {score}/5 câu.")
        if score == 5:
            st.balloons()
            st.markdown("🎉 **Xuất sắc! Bạn đã nắm chắc kiến thức HTML & CSS cơ bản.**")
        elif score >= 3:
            st.info("👍 Khá ổn! Bạn đã hiểu phần lớn nội dung.")
        else:
            st.warning("🔄 Nên ôn tập lại phần HTML & CSS phía trên nhé.")

# --- An toàn thông tin ---
with tabs[3]:
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
    Bạn nhận được email từ một địa chỉ lạ với tiêu đề "Bạn đã trúng thưởng!" và tệp đính kèm là file .exe.  
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
    st.markdown("### 🧠 Trắc nghiệm nhanh:")

    q1 = st.radio("1. Mật khẩu an toàn nên chứa?", [
        "Ngày sinh", "Chỉ chữ thường", "Ký tự đặc biệt, số, chữ hoa thường", "Tên người thân"
    ], key="sec_q1")

    q2 = st.radio("2. Khi nhận được email lạ có tệp đính kèm, bạn nên?", [
        "Mở ngay để xem nội dung", "Xóa email và không mở tệp", "Chuyển tiếp cho bạn bè", "Trả lời email"
    ], key="sec_q2")

    q3 = st.radio("3. Cách bảo vệ tài khoản hiệu quả nhất là?", [
        "Đặt mật khẩu dễ nhớ", "Dùng mật khẩu giống nhau cho mọi tài khoản", "Bật xác thực 2 yếu tố (2FA)", "Không đặt mật khẩu"
    ], key="sec_q3")

    q4 = st.radio("4. Khi dùng Wi-Fi công cộng, bạn nên?", [
        "Mua hàng online và nhập thẻ ngân hàng", "Kiểm tra email cá nhân", "Tránh truy cập tài khoản quan trọng", "Tải phần mềm lạ"
    ], key="sec_q4")

    q5 = st.radio("5. Đâu là ví dụ về phần mềm độc hại?", [
        "Microsoft Word", "Trình duyệt Chrome", "Phần mềm virus giả mạo", "Zoom"
    ], key="sec_q5")

    # Nút nộp bài và chấm điểm
    if st.button("✅ Nộp câu trả lời", key="submit_sec_quiz"):
        score = 0
        if q1 == "Ký tự đặc biệt, số, chữ hoa thường": score += 1
        if q2 == "Xóa email và không mở tệp": score += 1
        if q3 == "Bật xác thực 2 yếu tố (2FA)": score += 1
        if q4 == "Tránh truy cập tài khoản quan trọng": score += 1
        if q5 == "Phần mềm virus giả mạo": score += 1

        st.success(f"🎯 Bạn đã trả lời đúng {score}/5 câu.")

        if score == 5:
            st.balloons()
            st.balloons()
            st.markdown("🎉 **Xuất sắc! Bạn đã nắm vững kiến thức an toàn thông tin.**")
        elif score >= 3:
            st.info("👍 Khá tốt! Bạn đã hiểu phần lớn kiến thức.")
        else:
            st.warning("⚠️ Cần ôn lại kiến thức về an toàn thông tin. Hãy xem lại phần trên nhé.")


# --- Kho tài liệu ---
with tabs[4]:
    st.header("📚 Kho tài liệu học Tin học")

    # --- Sách lật trang ---
    st.subheader("📖 Sách lật trang")
    st.markdown("- [Giáo trình Tin học căn bản (FlipBook)](https://online.fliphtml5.com/irxmh/xiua/)")

    # --- CH Trắc nghiệm
    st.header("🧠 Trắc nghiệm tự luyện")
    question_bank = {
    "An toàn thông tin": [
        {
            "question": "Câu hỏi 1: Bạn nên làm gì khi nhận được email từ người lạ kèm tệp đính kèm?",
            "options": ["Mở ngay tệp để xem", "Chuyển tiếp", "Không mở và xoá email", "Trả lời email"],
            "answer": "Không mở và xoá email"
        },
    ],
    "Thiết kế web cơ bản": [
        {
            "question": "Câu hỏi 1: Thẻ nào tạo tiêu đề lớn nhất trong HTML?",
            "options": ["<title>", "<head>", "<h1>", "<header>"],
            "answer": "<h1>"
        },
    ]
}
        # Chọn chuyên đề
    topic = st.selectbox("Chọn chuyên đề:", list(question_bank.keys()))
    questions = question_bank[topic]
    
    st.markdown("### 📋 Trả lời câu hỏi:")
    
    # Danh sách chứa câu trả lời của người dùng
    user_answers = []
    
    # Hiển thị câu hỏi và các lựa chọn
    for i, q in enumerate(questions):
        ans = st.radio(q["question"], q["options"], key=f"{topic}_{i}")
        user_answers.append(ans)
    
    # Khi nhấn nút "Nộp bài"
    if st.button("📤 Nộp bài"):
        score = 0
        st.markdown("## 🎯 Kết quả:")
    
        # Kiểm tra từng câu trả lời
        for i, q in enumerate(questions):
            user_answer = user_answers[i]
            correct_answer = q["answer"]
            is_correct = user_answer == correct_answer
    
            # Thông báo kết quả từng câu
            if is_correct:
                score += 1
                st.markdown(f"✅ **Câu {i+1}: Đúng**")
            else:
                st.markdown(f"❌ **Câu {i+1}: Sai**")
                st.markdown(f"- Bạn chọn: `{user_answer}`")
                st.markdown(f"- Đáp án đúng: `{correct_answer}`")
    
            st.markdown("---")
    
        # Hiển thị điểm và kết quả
        st.success(f"🎉 Bạn được {score}/{len(questions)} điểm.")
        
        # Nếu đúng hết, hiển thị bóng bay
        if score == len(questions):
            st.balloons()


    # --- Website học lập trình (quốc tế) ---
    st.subheader("🌐 Website học lập trình")
    st.markdown("""
    - [W3Schools](https://www.w3schools.com/) – Học lập trình cơ bản HTML, CSS, JS,...
    - [GeeksforGeeks](https://www.geeksforgeeks.org/) – Thuật toán, cấu trúc dữ liệu, phỏng vấn.
    - [FreeCodeCamp](https://www.freecodecamp.org/) – Khóa học miễn phí có chứng chỉ.
    - [Coursera](https://www.coursera.org/) – Khóa học từ đại học lớn (một số miễn phí).
    - [Codecademy](https://www.codecademy.com/) – Học lập trình tương tác.
    """)

    # --- Website tiếng Việt ---
    st.subheader("🇻🇳 Website tiếng Việt")
    st.markdown("""
    - [HowKteam.vn](https://www.howkteam.vn/) – Học C#, Python, Android bằng tiếng Việt.
    - [Viblo.asia](https://viblo.asia/) – Bài viết kỹ thuật, lập trình, DevOps,...
    - [Hoclaptrinh.vn](https://hoclaptrinh.vn/) – Khóa học lập trình cơ bản – nâng cao.
    - [Codelearn.io](https://codelearn.io/) – Học lập trình qua thử thách (game hoá).
    """)

    # --- Sách & nguồn mở ---
    st.subheader("📘 Sách lập trình miễn phí")
    st.markdown("""
    - [Free Programming Books (GitHub)](https://github.com/EbookFoundation/free-programming-books) – Hàng nghìn sách lập trình miễn phí, có cả tiếng Việt.
    - [O'Reilly Online Learning](https://www.oreilly.com/) – Thư viện sách lập trình cao cấp (trả phí).
    """)

    # --- Gợi ý ---
    st.markdown("---")
    st.info("💡 Mẹo: Dành 15 phút mỗi ngày học lập trình từ W3Schools hoặc FreeCodeCamp để duy trì thói quen!")

# --- Góc chia sẻ ---
with tabs[5]:
    st.header("📬 Góc chia sẻ - Gửi bài thực hành")
    
    st.markdown("""
    **Chào bạn!** Đây là nơi bạn có thể gửi các bài thực hành, đề tài hoặc sản phẩm bạn đã hoàn thành trong quá trình học.
    
    Bằng cách gửi bài qua Google Forms, bạn sẽ nhận được:
    - **Phản hồi từ giảng viên** giúp cải thiện kỹ năng.
    - **Cơ hội nhận xét và đánh giá** từ cộng đồng.
    - **Cải thiện kỹ năng thực hành** qua các bài tập thực tế.
    
    Để gửi bài, vui lòng điền vào biểu mẫu dưới đây.
    """)

    st.markdown("### 📝 Biểu mẫu gửi bài thực hành:")
    st.markdown("[📎 Gửi bài qua Google Forms](https://forms.gle/...)")

    st.markdown("""
    **Lưu ý:**
    - Hãy chắc chắn rằng bài thực hành của bạn đã được hoàn thiện và kiểm tra kỹ lưỡng trước khi gửi.
    - Nếu bạn có bất kỳ câu hỏi nào hoặc gặp phải vấn đề khi gửi bài, đừng ngần ngại liên hệ với giảng viên hoặc hỗ trợ kỹ thuật.
    
    **Chúc bạn học tốt và đạt kết quả xuất sắc!**
    """)

# --- Kiểm tra mật khẩu ---
with tabs[1]:
    
    st.header("🔐 Kiểm tra & Tạo mật khẩu mạnh")
    
    # Hàm tính độ mạnh mật khẩu
    def calculate_strength(password):
        score = 0
        if len(password) >= 8: score += 1  # Độ dài mật khẩu tối thiểu 8 ký tự
        if len(password) >= 12: score += 2  # Mật khẩu dài hơn 12 ký tự thì mạnh hơn
        if any(c.isdigit() for c in password): score += 1  # Mật khẩu có ít nhất 1 số
        if any(c.islower() for c in password): score += 1  # Mật khẩu có ít nhất 1 chữ thường
        if any(c.isupper() for c in password): score += 1  # Mật khẩu có ít nhất 1 chữ hoa
        if any(c in string.punctuation for c in password): score += 1  # Mật khẩu có ký tự đặc biệt
        return score
    
    # Hàm đánh giá độ mạnh mật khẩu
    def strength_text(score):
        if score <= 2: return "❌ Yếu", "red"  # Mật khẩu yếu
        elif score <= 4: return "⚠️ Trung bình", "orange"  # Mật khẩu trung bình
        else: return "✅ Mạnh", "green"  # Mật khẩu mạnh
    
    tab1, tab2 = st.tabs(["🔎 Kiểm tra mật khẩu", "⚙️ Tạo mật khẩu mới"])
    
    # Tab kiểm tra mật khẩu
    with tab1:
        st.markdown("### 🔍 Kiểm tra độ mạnh mật khẩu:")
        st.markdown("""
        Mật khẩu mạnh là mật khẩu có độ dài tối thiểu 8 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.
        
                                     Vậy mật khẩu của bạn đã đủ mạnh chưa?
                                     
                           Nhập mật khẩu của bạn vào ô bên dưới để kiểm tra độ mạnh.
        """)
    
        pwd = st.text_input("Nhập mật khẩu:", type="password")
        if pwd:
            score = calculate_strength(pwd)
            text, color = strength_text(score)
            st.markdown(f"**Đánh giá:** <span style='color:{color}'>{text}</span>", unsafe_allow_html=True)
            st.progress(score * 20)  # Hiển thị tiến trình mạnh yếu
    
    # Tab tạo mật khẩu
    with tab2:
        st.markdown("### 🔑 Tạo mật khẩu mạnh:")
        st.markdown("""
        Bạn có thể sử dụng công cụ này để tạo mật khẩu ngẫu nhiên với độ dài tùy chỉnh. 
        Một mật khẩu mạnh là một mật khẩu dài, kết hợp chữ hoa, chữ thường, số và ký tự đặc biệt.
        """)
    
        length = st.slider("Chọn độ dài mật khẩu", 6, 50, 12)
        if st.button("🎲 Tạo mật khẩu"):
            chars = string.ascii_letters + string.digits + string.punctuation
            gen_pwd = ''.join(random.choice(chars) for _ in range(length))
            st.text_input("🔑 Mật khẩu đã tạo:", gen_pwd)
            score = calculate_strength(gen_pwd)
            text, color = strength_text(score)
            st.markdown(f"**Độ mạnh:** <span style='color:{color}'>{text}</span>", unsafe_allow_html=True)
            st.progress(min(score * 20, 100))  # Tỷ lệ tiến trình từ 0 đến 100
    
            # Lưu mật khẩu đã tạo dưới dạng SHA-256
            st.markdown("""
            Bạn có thể lưu mật khẩu đã tạo dưới dạng SHA-256 để đảm bảo an toàn. 
            SHA-256 là thuật toán mã hóa mật khẩu giúp bảo vệ thông tin của bạn.
            """)
            
            if st.button("💾 Lưu mật khẩu SHA-256"):
                hashed = hashlib.sha256(gen_pwd.encode()).hexdigest()
                buffer = io.StringIO()
                buffer.write(hashed + "\n")
                buffer.seek(0)
                st.success("Đã lưu mật khẩu dưới dạng SHA-256!")
                st.download_button("📥 Tải file SHA-256", buffer, file_name="saved_passwords.txt")
