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




    # --- CH trắc nghiệm
    st.subheader("🧠 Trắc nghiệm tự luyện")
    # Ngân hàng câu hỏi theo lớp và chủ đề
    question_bank = {
        "10": {
            "Chủ đề A": [
                {
                "question": "Câu 1: Thông tin là gì?",
                "options": ["Các văn bản và số liệu", 
                            "Hiểu biết của con người về một thực thể, sự vật, khái niệm, hiện tượng nào đó.", 
                            "Văn bản, Hình ảnh, âm thanh", 
                            "Hình ảnh, âm thanh"],
                "answer": "Hiểu biết của con người về một thực thể, sự vật, khái niệm, hiện tượng nào đó."
            },
            {
                "question": "Câu 2: Phát biểu nào sau đây là đúng?",
                "options": ["Dữ liệu chỉ có ở trong máy tính", 
                            "Dữ liệu là những giá trị số do con người nghĩ ra.",
                            "Dữ liệu được thể hiện dưới dạng con số, văn bản, hình ảnh, âm thanh.",
                            "Dữ liệu chỉ có thể được hiểu bởi những người có trình độ cao"],
                "answer": "Dữ liệu được thể hiện dưới dạng con số, văn bản, hình ảnh, âm thanh."
            },
            {
                "question": "Câu 3: Phát biểu nào sau đây là sai khi nói về quan hệ giữa thông tin và dữ liệu?",
                "options": ["Dữ liệu là thông tin đã được đưa vào máy tính", 
                            "Thông tin là ý nghĩa của dữ liệu",
                            "Thông tin và dữ liệu có tính độc lập tương đối",
                            "Thông tin không có tính toàn vẹn"],
                "answer": "Thông tin không có tính toàn vẹn"
            },
            {
                "question": "Câu 4: Thông tin nào không phải là thông tin cần xử lí để xếp loại các tổ cuối tuần?",
                "options": ["Số lượng bạn ăn bán trú", 
                            "Số các bạn bị ghi tên vì đi muộn",
                            "Số bạn không mặc áo đồng phục",
                            "Số bạn bị cô giáo nhắc nhở"],
                "answer": "Số lượng bạn ăn bán trú"
            },
            {
                "question": "Câu 5: Thông tin có thể được biểu diễn thành các dạng nào sau đây:",
                "options": ["Văn bản, hình ảnh", 
                            "Văn bản, hình ảnh và âm thanh", 
                            "Dãy bit", 
                            "Âm thanh, hình ảnh"],
                "answer": "Văn bản, hình ảnh và âm thanh"
            },
            {
                "question": "Câu 6: Đặc thù của ngành tin học là gì?",
                "options": ["Quá trình nghiên cứu và xử lí thông tin.", 
                            "Quá trình nghiên cứu và triển khai các ứng dụng không tách rời việc phát triển và sử dụng máy tính điện tử.",
                            "Quá trình nghiên cứu và xử lí thông tin một cách tự động.",
                            "Quá trình nghiên cứu và ứng dụng các công cụ tính toán."],
                "answer": "Quá trình nghiên cứu và xử lí thông tin một cách tự động."
            },
            {
                "question": "Câu 7: Mắt thường không thể tiếp nhận những thông tin nào dưới đây?",
                "options": ["Rác bẩn vứt ngoài hành lang lớp học", 
                            "Những con vi trùng gây bệnh lị lẫn trong thức ăn bị ôi thiu",
                            "Đàn kiến đang “tấn công” lọ đường quên đậy nắp",
                            "Bạn Phương quên không đeo khăn quàng đỏ"],
                "answer": "Những con vi trùng gây bệnh lị lẫn trong thức ăn bị ôi thiu"
            },
            {
                "question": "Câu 8: Tin học là?",
                "options": ["Ngành khoa học về xử lý thông tin tự động dựa trên máy tính điện tử", 
                            "Áp dụng máy tính trong các hoạt động xử lý thông tin", 
                            "Máy tính và các công việc liên quan đến máy tính điện tử", 
                            "Lập chương trình cho máy tính"],
                "answer": "Ngành khoa học về xử lý thông tin tự động dựa trên máy tính điện tử"
            },
            {
                "question": "Câu 9: Tin học là một ngành khoa học vì đó là ngành:",
                "options": ["Nghiên cứu máy tính điện tử", 
                            "Sử dụng máy tính điện tử",
                            "Được sinh ra trong nền văn minh thông tin",
                            "Có nội dung, mục tiêu, phương pháp nghiên cứu riêng"],
                "answer": "Có nội dung, mục tiêu, phương pháp nghiên cứu riêng"
            },
            {
                "question": "Câu 10: Cho tình huống: Em đang ngồi trong lớp chờ giờ học bắt đầu, em thấy thầy giáo bước vào lớp. Thông tin em nhận được là gì?",
                "options": ["Thầy giáo bước vào lớp", 
                            "Đứng dậy chào thầy giáo",
                            "Em đang ngồi trong lớp", 
                            "Giờ học bắt đầu"],
                "answer": "Thầy giáo bước vào lớp"
            },
            {
                "question": "Câu 11: Khẳng định nào sau đây là sai khi nói về máy tính?",
                "options": ["Máy tính có tốc độ xử lí nhanh",
                            "Máy tính có khả năng lưu trữ lượng thông tin lớn",
                            "Máy tính ngày càng nhỏ gọn",
                            "Máy tính không thể kết nối được với nhau"],
                "answer": "Máy tính không thể kết nối được với nhau"
            },
            {
                "question": "Câu 12: Đâu không phải là ưu việt của máy tính điện tử?",
                "options": ["Máy tính có thể làm việc 24/7", 
                            "Máy tính có thể lưu trữ một lượng lớn thông tin",
                            "Các máy tính liên kết tạo khả năng xử lý thông tin tốt",
                            "Đôi khi máy tính có thể cho kết quả không chính xác"],
                "answer": "Đôi khi máy tính có thể cho kết quả không chính xác"
            },
            {
                "question": "Câu 13: Trong tin học, Flops có nghĩa là gì?",
                "options": ["Tốc độ tính toán trong 1 giây", 
                            "Tốc độ tính toán trong 1 phút",
                            "Tốc độ tính toán trong 1 giờ", 
                            "Tốc độ tính toán trong một thời gian ngắn"],
                "answer": "Tốc độ tính toán trong 1 giây"
            },
            {
                "question": "Câu 14: Mạng Xã hội Facebook ra đời vào năm nào?",
                "options": ["2001", "2002", "2003", "2004"],
                "answer": "2004"
            },
            {
                "question": "Câu 15: Đặc trưng của cuộc cách mạng công nghiệp lần thứ 4 là gì?",
                "options": ["Động cơ hơi nước", 
                            "Điện và động cơ điện", 
                            "Máy tính và thiết bị điện tử", 
                            "Trí tuệ nhân tạo và công nghệ robot"],
                "answer": "Trí tuệ nhân tạo và công nghệ robot"
            },
            {
                "question": "Câu 16: Máy tính trở thành công cụ lao động không thể thiếu vì?",
                "options": ["Cho ta khả năng lưu trữ và xử lý thông tin", 
                            "Giải tất cả các bài toán khó", 
                            "Soạn thảo văn bản và truy cập Internet", 
                            "Tính toán cực nhanh và chính xác"],
                "answer": "Cho ta khả năng lưu trữ và xử lý thông tin"
            },
            {
                "question": "Câu 17: Đơn vị nào sau đây là đơn vị lưu trữ dữ liệu trong máy tính?",
                "options": ["KB", "Kg", "MG", "Gi"],
                "answer": "KB"
            },
            {
                "question": "Câu 18: Khẳng định sai về thành tựu của ngành tin học là?",
                "options": ["Trí tuệ nhân tạo tạo ra Robot", 
                            "Internet làm thay đổi xã hội", 
                            "Ra lệnh bằng lời nói", 
                            "Ngôn ngữ lập trình mới xuất hiện 2 năm gần đây"],
                "answer": "Ngôn ngữ lập trình mới xuất hiện 2 năm gần đây"
            },
            {
                "question": "Câu 19: Nền văn minh thông tin gắn liền với loại công cụ nào?",
                "options": ["Động cơ hơi nước", "Máy điện thoại", "Máy tính điện tử", "Máy phát điện"],
                "answer": "Máy tính điện tử"
            },
            {
                "question": "Câu 20: Ngành tin học gắn liền với…… và ……máy tính điện tử",
                "options": ["Sự phát triển, sử dụng", 
                            "Sử dụng, tiêu thụ", 
                            "Sự phát triển, tiêu thụ", 
                            "Tiêu thụ, sự phát triển"],
                "answer": "Sự phát triển, sử dụng"
            }
        ],
            "Chủ đề B": [
                    {
                    "question": "Câu 1: Để tránh phần mềm độc hại chúng ta cần làm gì?",
                    "options": ["Sử dụng phần mềm diệt virus.", "Mở mail có tệp lạ.", "Sử dụng phần mềm không rõ nguồn gốc.", "Tránh sử dụng USB khi chưa kiểm tra thiết bị đó."],
                    "answer": "Sử dụng phần mềm diệt virus."
                },
                {
                    "question": "Câu 2: Hạn chế của mạng Internet?",
                    "options": ["Cập nhật tin tức và xu hướng nhanh nhất; kết nối với nhiều người.", "Học hỏi được nhiều kỹ năng bổ ích.", "Tìm hiểu về các chủ đề mới; các trò chơi rèn luyện IQ.", "Dễ dàng tiếp cận với những thông tin nguy hiểm, hình ảnh bạo lực."],
                    "answer": "Dễ dàng tiếp cận với những thông tin nguy hiểm, hình ảnh bạo lực."
                },
                {
                    "question": "Câu 3: Thuật ngữ E-Payment dùng để chỉ lĩnh vực nào?",
                    "options": ["Thương mại điện tử.", "Ngân hàng điện tử.", "Thanh toán điện tử.", "Thông tin số."],
                    "answer": "Thanh toán điện tử."
                },
                {
                    "question": "Câu 4: Thuật ngữ E-Commerce dùng để chỉ lĩnh vực nào?",
                    "options": ["Thương mại điện tử.", "Ngân hàng điện tử.", "Thanh toán điện tử.", "Thông tin số."],
                    "answer": "Thương mại điện tử."
                },
                {
                    "question": "Câu 5: Thuật ngữ E-Government để chỉ dịch vụ nào?",
                    "options": ["Học liệu mở.", "Chính phủ điện tử.", "Ngân hàng điện tử.", "Y tế số."],
                    "answer": "Chính phủ điện tử."
                },
                {
                    "question": "Câu 6: Việt Nam bắt đầu cung cấp dịch vụ Internet cho người dân vào năm nào?",
                    "options": ["1996", "1997", "1998", "1999"],
                    "answer": "1997"
                },
                {
                    "question": "Câu 7: Tên tiếng Anh của điện toán đám mây là gì?",
                    "options": ["Gmail.", "Zoom Cloud Meeting.", "Cloud Computing.", "Google Meet."],
                    "answer": "Cloud Computing."
                },
                {
                    "question": "Câu 8: Mạng LAN là viết tắt của cụm từ nào?",
                    "options": ["Local Arian Network", "Lomal Area Network", "Local Area", "Local Area Network"],
                    "answer": "Local Area Network"
                },
                {
                    "question": "Câu 9: Hành vi nào có thể làm cho máy tính bị nhiễm các phần mềm độc hại?",
                    "options": ["Truy cập các nguồn học liệu mở", "Truy cập các trang mua sắm lớn", "Truy cập vào đường link lạ", "Truy cập trang nghe nhạc trực tuyến"],
                    "answer": "Truy cập vào đường link lạ"
                },
                {
                    "question": "Câu 10: Đâu không phải là dịch vụ lưu trữ qua điện toán đám mây?",
                    "options": ["Dropbox.", "Google Drive.", "iCoud.", "Paint."],
                    "answer": "Paint."
                },
                {
                    "question": "Câu 11: Đâu là từ viết tắt của Internet vạn vật?",
                    "options": ["ICT.", "CS.", "IoT.", "OST."],
                    "answer": "IoT."
                },
                {
                    "question": "Câu 12: Chọn đáp án sai khi nói về tác động tích cực của mạng Internet?",
                    "options": ["Học tập trực tuyến hiệu quả.", "Mua sắm trực tuyến dễ dàng.", "Lười suy nghĩ.", "Trò chuyện trực tuyến thuận lợi."],
                    "answer": "Lười suy nghĩ."
                },
                {
                    "question": "Câu 13: Mô tả nào sau đây sai khi nói về Internet?",
                    "options": ["Là một mạng máy tính.", "Có phạm vi bao phủ khắp thế giới.", "Hàng tỉ người truy cập và sử dụng.", "Là tài sản và hoạt động dưới sự quản lí của một công ty tin học lớn nhất thế giới."],
                    "answer": "Là tài sản và hoạt động dưới sự quản lí của một công ty tin học lớn nhất thế giới."
                },
                {
                    "question": "Câu 14: Khi sử dụng máy tính có kết nối mạng, bạn không sử dụng ứng dụng nặng mà máy tính vẫn chạy rất chậm so với bình thường. Dấu hiệu đó báo hiệu điều gì?",
                    "options": ["Máy tính có thể đã bị nhiễm virus.", "Máy tính có thể đã hỏng ổ đĩa cứng.", "Máy tính có thể đã bị hỏng loa.", "Máy tính không có kết nối Internet."],
                    "answer": "Máy tính có thể đã bị nhiễm virus."
                },
                {
                    "question": "Câu 15: Những tờ tiền giấy có thể bị bẩn, bị rách hoặc bị làm giả. Ứng dụng nào sau đây của Internet giúp khắc phục những hạn chế đó?",
                    "options": ["E – Learning", "E – Government", "Mạng xã hội", "E – Payment"],
                    "answer": "E – Payment"
                },
                {
                    "question": "Câu 16: Gia đình bạn An cần tìm hiểu và làm thủ tục đóng thuế trước bạ về đất đai, nhưng do dịch Covid-19 nên phải hạn chế đi lại. Trong trường hợp này, ứng dụng nào sau đây của mạng máy tính hữu ích?",
                    "options": ["E-Learning.", "E-Government.", "E-Payment.", "E-Commerce."],
                    "answer": "E-Government."
                },
                {
                    "question": "Câu 17: Đâu là ưu điểm của việc liên lạc qua Email?",
                    "options": ["Chi phí cao hơn.", "Bức thư không bao giờ bị thất lạc hay bị kẻ gian đọc trộm.", "Có thể gửi cả âm thanh, hình ảnh, video.", "Ít thuận tiện hơn cho người sử dụng."],
                    "answer": "Có thể gửi cả âm thanh, hình ảnh, video."
                },
                {
                    "question": "Câu 18: Hành vi nào có thể làm cho máy tính bị nhiễm các phần mềm độc hại?",
                    "options": ["Truy cập các nguồn học liệu mở.", "Truy cập các trang mua sắm lớn.", "Truy cập vào đường link lạ.", "Truy cập trang nghe nhạc trực tuyến."],
                    "answer": "Truy cập vào đường link lạ."
                },
                {
                    "question": "Câu 19: Trường hợp nào không thích hợp để sử dụng mạng LAN?",
                    "options": ["Tòa nhà.", "Cơ quan.", "Nhà riêng.", "Quận/huyện."],
                    "answer": "Quận/huyện."
                },
                {
                    "question": "Câu 20: Phát biểu đúng về điện toán đám mây?",
                    "options": ["Nó sẽ luôn rẻ hơn và an toàn hơn so với máy tính cục bộ.", "Bạn có thể truy cập dữ liệu của mình từ bất kỳ máy tính nào trên thế giới, miễn là bạn có kết nối Internet.", "Chỉ có một vài công ty nhỏ đang đầu tư vào công nghệ, làm cho nó trở thành một công việc mạo hiểm.", "Bạn có thể truy cập dữ liệu của mình từ bất kỳ máy tính nào trên thế giới."],
                    "answer": "Bạn có thể truy cập dữ liệu của mình từ bất kỳ máy tính nào trên thế giới, miễn là bạn có kết nối Internet."
                }
            ]
        },
        "11": {
            "Chủ đề C": [
                            {
                    'question': 'Câu 1: Lưu trữ trực tuyến là gì?',
                    'options': ['A. Lưu trữ dữ liệu trên một thiết bị lưu trữ ngoại vi', 'B. Lưu trữ dữ liệu trên đám mây', 'C. Lưu trữ dữ liệu trên ổ đĩa cứng', 'D. Lưu trữ dữ liệu trên USB'],
                    'answer': 'B. Lưu trữ dữ liệu trên đám mây'
                },
                {
                    'question': 'Câu 2: Dịch vụ lưu trữ trực tuyến nào được sử dụng phổ biến nhất?',
                    'options': ['A. Google Drive', 'B. Dropbox', 'C. OneDrive', 'D. iCloud'],
                    'answer': 'A. Google Drive'
                },
                {
                    'question': 'Câu 3: Google Drive là gì?',
                    'options': ['A. Dịch vụ lưu trữ trực tuyến của Google', 'B. Trình duyệt web của Google', 'C. Ứng dụng chỉnh sửa văn bản của Google', 'D. Công cụ tìm kiếm của Google'],
                    'answer': 'A. Dịch vụ lưu trữ trực tuyến của Google'
                },
                {
                    'question': 'Câu 4: Google Drive cung cấp bao nhiêu dung lượng lưu trữ miễn phí cho người dùng?',
                    'options': ['A. 5 GB', 'B. 10 GB', 'C. 15 GB', 'D. 20 GB'],
                    'answer': 'C. 15 GB'
                },
                {
                    'question': 'Câu 5: Lưu trữ trực tuyến có nhược điểm gì?',
                    'options': ['A. Tốc độ truy cập chậm hơn so với lưu trữ ngoại vi', 'B. Dữ liệu dễ bị mất hoặc bị xâm nhập', 'C. Giá cả đắt đỏ', 'D. Không thể lưu trữ tệp có kích thước lớn.'],
                    'answer': 'B. Dữ liệu dễ bị mất hoặc bị xâm nhập'
                },
                {
                    'question': 'Câu 6: Tính năng chia sẻ tệp là gì?',
                    'options': ['A. Cho phép người dùng lưu trữ tệp trên đám mây', 'B. Cho phép người dùng gửi tệp đến người khác để xem hoặc chỉnh sửa', 'C. Cho phép người dùng tải xuống tệp từ đám mây', 'D. Cho phép người dùng tạo bản sao lưu tệp trong trường hợp tệp gốc bị mất.'],
                    'answer': 'B. Cho phép người dùng gửi tệp đến người khác để xem hoặc chỉnh sửa'
                },
                {
                    'question': 'Câu 7: Tính năng đồng bộ hóa dữ liệu là gì?',
                    'options': ['A. Cho phép người dùng tải xuống tất cả các tệp từ đám mây', 'B. Cho phép người dùng lưu trữ dữ liệu trên nhiều thiết bị và đồng bộ hóa dữ liệu giữa chúng', 'C. Cho phép người dùng chia sẻ dữ liệu với người khác', 'D. Cho phép người dùng tạo bản sao lưu dữ liệu trên đám mây.'],
                    'answer': 'B. Cho phép người dùng lưu trữ dữ liệu trên nhiều thiết bị và đồng bộ hóa dữ liệu giữa chúng'
                },
                {
                    'question': 'Câu 8: Lưu trữ trực tuyến? Chọn đáp án SAI',
                    'options': ['A. Lưu trữ tài liệu cá nhân', 'B. Lưu trữ dữ liệu doanh nghiệp', 'C. Lưu trữ tệp tin đa phương tiện như video và âm thanh', 'D. Không giới hạn dung lượng lưu trữ.'],
                    'answer': 'D. Không giới hạn dung lượng lưu trữ.'
                },
                {
                    'question': 'Câu 9: Tính năng nào trên Google Drive cho phép người dùng tạo bản sao lưu tệp tự động?',
                    'options': ['A. Chế độ lịch', 'B. Chế độ xem trình diễn', 'C. Chế độ tìm kiếm', 'D. Chế độ chia sẻ.'],
                    'answer': 'A. Chế độ lịch'
                },
                {
                    'question': 'Câu 10: Khi sử dụng dịch vụ Google Drive. Phát biểu nào sai khi nói về thao tác bên dưới?',
                    'options': ['A. Gõ địa chỉ hộp thư của người muốn chia sẻ vào ô hiển thị chữ “Thêm người và nhóm”', 'B. Địa chỉ thư toantinvanquan@gmail.com là địa chỉ hộp thư người chia sẻ.', 'C. Người được chia sẻ có quyền chỉnh sửa tài liệu.', 'D. Người được chia sẻ có quyền xem tài liệu.'],
                    'answer': 'B. Địa chỉ thư toantinvanquan@gmail.com là địa chỉ hộp thư người chia sẻ.'
                },
                {
                    'question': 'Câu 11: Loại lưu trữ nào đảm bảo rằng dữ liệu được đồng bộ hóa trên nhiều thiết bị và có thể chia sẻ bởi nhiều người dùng ở các vị trí địa lý khác nhau?',
                    'options': ['A. Lưu trữ vật lí', 'B. Lưu trữ trong bộ nhớ', 'C. Lưu trữ trực tuyến', 'D. Lưu trữ đám mây'],
                    'answer': 'C. Lưu trữ trực tuyến'
                },
                {
                    'question': 'Câu 12: Lợi ích chính của lưu trữ trực tuyến là gì?',
                    'options': ['A. Tốc độ truyền dữ liệu cao', 'B. Chi phí thấp', 'C. Độ bền vật lí', 'D. Tiện lợi và chia sẻ dữ liệu'],
                    'answer': 'D. Tiện lợi và chia sẻ dữ liệu'
                },
                {
                    'question': 'Câu 13: Công ty nào cung cấp dịch vụ lưu trữ đám mây Google Drive phổ biến?',
                    'options': ['A. Microsoft', 'B. Google', 'C. Apple', 'D. Amazon'],
                    'answer': 'B. Google'
                },
                {
                    'question': 'Câu 14: Dịch vụ lưu trữ trực tuyến nào rất phổ biến tại Việt Nam?',
                    'options': ['A. Google Drive', 'B. OneDrive', 'C. Fshare', 'D. Dropbox'],
                    'answer': 'C. Fshare'
                },
                {
                    'question': 'Câu 15: Phương pháp lưu trữ nào liên quan đến việc lưu trữ dữ liệu trên các máy chủ từ xa có thể truy cập qua Internet?',
                    'options': ['A. Lưu trữ đám mây', 'B. Lưu trữ trong bộ nhớ', 'C. Lưu trữ ngoại tuyến', 'D. Lưu trữ trên băng'],
                    'answer': 'A. Lưu trữ đám mây'
                },
                {
                    'question': 'Câu 16: Vấn đề chính khi lưu trữ dữ liệu trực tuyến là gì?',
                    'options': ['A. Đồng bộ hóa dữ liệu', 'B. Độ bền vật lí', 'C. Bảo mật dữ liệu', 'D. Tốc độ truyền dữ liệu'],
                    'answer': 'C. Bảo mật dữ liệu'
                },
                {
                    'question': 'Câu 17: Dịch vụ lưu trữ trực tuyến nào liên quan đến tên miền "www.onedrive.live.com"?',
                    'options': ['A. Google Drive', 'B. OneDrive', 'C. Dropbox', 'D. iCloud'],
                    'answer': 'B. OneDrive'
                },
                {
                    'question': 'Câu 18: Thiết bị lưu trữ nào được đặc trưng bởi bộ nhớ không bay hơi và độ bền cao?',
                    'options': ['A. HDD', 'B. SSD', 'C. Ổ đĩa USB flash', 'D. Đĩa quang'],
                    'answer': 'B. SSD'
                },
                {
                    'question': 'Câu 19: Thuật ngữ nào ám chỉ việc sao lưu dữ liệu đã lưu trữ trực tuyến?',
                    'options': ['A. Đồng bộ hóa dữ liệu', 'B. Nén dữ liệu', 'C. Mã hóa dữ liệu', 'D. Sao lưu dữ liệu'],
                    'answer': 'D. Sao lưu dữ liệu'
                },
                {
                    'question': 'Câu 20: Công ty nào cung cấp dịch vụ lưu trữ đám mây được biết đến là iCloud?',
                    'options': ['A. Microsoft', 'B. Google', 'C. Apple', 'D. Dropbox'],
                    'answer': 'C. Apple'
                }
            ],
            "Chủ đề D": [
                    {
                    'question': 'Câu 1: Đâu không phải là những thủ đoạn lừa đảo trên mạng?',
                    'options': [
                        'A. Lừa đảo trúng thưởng, tặng quà để lấy tiền phí vận chuyển',
                        'B. Lừa đảo chiếm tiền đặt cọc hoặc bán hàng giả',
                        'C. Lừa đảo để lấy cắp thông tin cá nhân',
                        'D. Khai báo thông tin cá nhân khi đăng ký dịch vụ công trực tuyến'
                    ],
                    'answer': 'D. Khai báo thông tin cá nhân khi đăng ký dịch vụ công trực tuyến'
                },
                {
                    'question': 'Câu 2: Đâu không phải là dấu hiệu lừa đảo để lấy cắp thông tin cá nhân bằng trang web?',
                    'options': [
                        'A. Trang web có lỗi chính tả, lỗi hành văn thì đó có thể là lừa đảo',
                        'B. Tên miền gồm vài phần cách nhau dấu chấm',
                        'C. Những cách viết sai chính tả trong tên miền để đánh lừa người đọc như thay chữ “o” bằng số 0; thay chữ “m” bằng “r” và “n”',
                        'D. Trỏ chuột vào liên kết thấy địa chỉ đích hiện ra khớp với địa chỉ hiển thị'
                    ],
                    'answer': 'D. Trỏ chuột vào liên kết thấy địa chỉ đích hiện ra khớp với địa chỉ hiển thị'
                },
                {
                    'question': 'Câu 3: Đâu là nguyên tắc để hạn chế thiệt hại?',
                    'options': [
                        'A. Không mở bất kì liên kết hoặc tệp đính kèm nào mà hãy kiểm tra địa chỉ đích thực sự để phát hiện liên kết lừa đảo.',
                        'B. Trỏ chuột vào một liên kết nhưng không nháy chuột, ta sẽ nhìn thấy địa chỉ địch thực sự mà liên kết sẽ mở ra.',
                        'C. Nếu tài khoản bị ảnh hưởng có liên quan đến nhà trường hay một cơ quan, tổ chức, cần thông báo ngay cho người có trách nhiệm',
                        'D. Gọi điện thoại trực tiếp, truy cập địa chỉ trang web in trên các tài liệu chính thức'
                    ],
                    'answer': 'A. Không mở bất kì liên kết hoặc tệp đính kèm nào mà hãy kiểm tra địa chỉ đích thực sự để phát hiện liên kết lừa đảo.'
                },
                {
                    'question': 'Câu 4: Điều nào cho chúng ta dễ dàng nhận biết nhất là đang bị lừa đảo?',
                    'options': [
                        'A. Nhắn tin hỏi thăm sức khỏe',
                        'B. Người thân gọi điện hỏi thăm sức khỏe',
                        'C. Gửi Email đi phỏng vấn công việc',
                        'D. Tin nhắn lạ hỏi vay tiền, vay thẻ nạp điện thoại'
                    ],
                    'answer': 'D. Tin nhắn lạ hỏi vay tiền, vay thẻ nạp điện thoại'
                },
                {
                    'question': 'Câu 5: Trong tin học, Phishing là gì?',
                    'options': [
                        'A. Lừa đảo để lấy cắp thông tin cá nhân bằng các trang web giả',
                        'B. Lừa đảo nhận được quà tặng từ dịch vụ chuyển phát',
                        'C. Lừa đảo chiếm tiền đặt cọc',
                        'D. Lừa đảo để lấy phí vận chuyển'
                    ],
                    'answer': 'A. Lừa đảo để lấy cắp thông tin cá nhân bằng các trang web giả'
                },
                {
                    'question': 'Câu 6: Không tìm cách đọc mail, tin nhắn của người khác thuộc nguyên tắc ứng xử nào?',
                    'options': [
                        'A. Không lợi dụng vị thế của mình để làm việc xấu',
                        'B. Tôn trọng quyền riêng tư của người khác',
                        'C. Tôn trọng văn hóa nhóm',
                        'D. Đặt mình vào vị trí của người khác'
                    ],
                    'answer': 'B. Tôn trọng quyền riêng tư của người khác'
                },
                {
                    'question': 'Câu 7: Việc tạo lập một tài khoản giả mạo trên mạng xã hội nhằm lừa đảo, gây tổn hại đến người khác có thể bị xử lý như thế nào?',
                    'options': [
                        'A. Bị phạt tiền hoặc bị truy cứu trách nhiệm hình sự tùy theo mức độ nghiêm trọng',
                        'B. Không bị xử lý vì đó là tự do cá nhân',
                        'C. Chỉ bị nhắc nhở từ nhà cung cấp dịch vụ',
                        'D. Tài khoản bị khóa tạm thời mà không có hình phạt nào khác'
                    ],
                    'answer': 'A. Bị phạt tiền hoặc bị truy cứu trách nhiệm hình sự tùy theo mức độ nghiêm trọng'
                },
                {
                    'question': 'Câu 8: Trong môi trường số, việc chia sẻ quá nhiều thông tin cá nhân có thể dẫn đến hậu quả gì?',
                    'options': [
                        'A. Giúp bạn bè hiểu rõ hơn về bạn',
                        'B. Gây nguy cơ mất cắp thông tin, lừa đảo và xâm phạm quyền riêng tư',
                        'C. Tăng khả năng tìm kiếm việc làm',
                        'D. Giúp nâng cao uy tín cá nhân'
                    ],
                    'answer': 'B. Gây nguy cơ mất cắp thông tin, lừa đảo và xâm phạm quyền riêng tư'
                },
                {
                    'question': 'Câu 9: Tại sao chúng ta cần tôn trọng quyền riêng tư của người khác trên mạng xã hội?',
                    'options': [
                        'A. Vì luật pháp yêu cầu như vậy',
                        'B. Vì tôn trọng quyền riêng tư là một phần của đạo đức và văn hóa ứng xử trên mạng',
                        'C. Vì nó giúp tăng số lượng người theo dõi',
                        'D. Vì người khác có thể trả thù nếu quyền riêng tư bị xâm phạm'
                    ],
                    'answer': 'B. Vì tôn trọng quyền riêng tư là một phần của đạo đức và văn hóa ứng xử trên mạng'
                },
                {
                    'question': 'Câu 10: Quan điểm nào sau đây là đúng về sử dụng mạng xã hội?',
                    'options': [
                        'A. Mạng xã hội là thế giới ảo, nên luật pháp trên mạng cũng chỉ là ảo',
                        'B. Sử dụng mạng xã hội để buôn bán thì thích bán gì thì bán, không cần giấy phép kinh doanh',
                        'C. Không có điều lệ nào quy định phải sử dụng ngôn từ hợp đạo đức. Ngươi chửi mắng mình thì mình cũng chửi mắng lại',
                        'D. Thế giới ảo nhưng cuộc sống thực, nên nó sẽ ảnh hưởng đến đời sống thực'
                    ],
                    'answer': 'D. Thế giới ảo nhưng cuộc sống thực, nên nó sẽ ảnh hưởng đến đời sống thực'
                },
                {
                    'question': 'Câu 11: Theo quy định của pháp luật Việt Nam, hành vi đăng tải thông tin sai sự thật lên mạng xã hội có thể bị xử phạt như thế nào?',
                    'options': [
                        'A. Bị cảnh cáo',
                        'B. Bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự',
                        'C. Bị khóa tài khoản mạng xã hội',
                        'D. Không có hình thức xử phạt nào'
                    ],
                    'answer': 'B. Bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự'
                },
                {
                    'question': 'Câu 12: Trong trường hợp bạn nhận được email từ một nguồn không rõ yêu cầu cung cấp thông tin cá nhân, bạn nên làm gì?',
                    'options': [
                        'A. Cung cấp ngay thông tin để nhận được phần thưởng',
                        'B. Kiểm tra tính xác thực của email và không cung cấp thông tin nếu không chắc chắn',
                        'C. Bỏ qua và tiếp tục sử dụng mạng bình thường',
                        'D. Chia sẻ email đó với bạn bè để cùng nhận thưởng'
                    ],
                    'answer': 'B. Kiểm tra tính xác thực của email và không cung cấp thông tin nếu không chắc chắn'
                },
                {
                    'question': 'Câu 13: Khi đã bị lừa đảo tiền bạc và hăm dọa tinh thần trên không gian mạng, bạn My đã đăng tải lên facebook cá nhân về điều đó, tuy nhiên văn hóa mạng rất tồi tệ đã chỉ trích và nói “đấy là điều bạn đáng phải nhận, dốt thì phải tự chịu,….” Hãy cho bạn My một phương án tốt nhất?',
                    'options': [
                        'A. Lên facebook để trả lời các bình luận, và đòi lại công bằng cho bản thân',
                        'B. Nói với người thân và nên dừng sử dụng mạng xã hội facebook một thời gian. Nên có khoảng thời gian hồi phục tinh thần. Trình báo cho cơ quan chức năng về độ nghiệm trọng của sự việc',
                        'C. Tiếp tục đăng bài, chửi rủa và sử dụng vũ lực để đòi lại công bằng',
                        'D. Ngày nào cũng đăng bài công kích lại những chỉ trích đó'
                    ],
                    'answer': 'B. Nói với người thân và nên dừng sử dụng mạng xã hội facebook một thời gian. Nên có khoảng thời gian hồi phục tinh thần. Trình báo cho cơ quan chức năng về độ nghiệm trọng của sự việc'
                },
                {
                    'question': 'Câu 14: Nếu nhận một tin nhắn lạ hỏi vay tiền thì ta nên làm gì?',
                    'options': [
                        'A. Gọi điện lại ngay và kiểm tra thông tin của người hỏi',
                        'B. Chuyển tiền luôn cho người ta',
                        'C. Kệ người ta',
                        'D. Chia sẻ thông tin đó cho nhiều người biết'
                    ],
                    'answer': 'A. Gọi điện lại ngay và kiểm tra thông tin của người hỏi'
                },
                {
                    'question': 'Câu 15: Bạn Lan đang sử dụng internet để lướt web thì thấy mọt tin nhắn từ bạn thân mình là bạn B gửi đến “Cậu cho mình vay 1 triệu mình đưa mẹ đi khám”. Nếu là Lan bạn sẽ làm gì ngay lúc này?',
                    'options': [
                        'A. Gọi điện cho B và kiểm tra lại thông tin, đúng thì cho vay',
                        'B. Chuyển tiền ngay cho B để còn kịp thời đưa mẹ B đi viện',
                        'C. Không quan tâm, vì không muốn dây dưa tiền bạc',
                        'D. Đi hỏi người khác cho B vay chứ mình không cho vay'
                    ],
                    'answer': 'A. Gọi điện cho B và kiểm tra lại thông tin, đúng thì cho vay'
                }
            ]
        },
        "12": {
            "Chủ đề E": [
                        {
                    "question": "Câu hỏi 1: Phát biểu nào sau đây đúng?",
                    "options": [
                        "Website có thể được tạo ra bởi lập trình viên hoặc người không có kĩ năng lập trình.",
                        "Website chỉ có thể được tạo ra bởi lập trình viên.",
                        "Website không thể được tạo ra bởi người am hiểu về lập trình.",
                        "Người dùng không thể chỉnh sửa website."
                    ],
                    "answer": "Website có thể được tạo ra bởi lập trình viên hoặc người không có kĩ năng lập trình."
                },
                {
                    "question": "Câu hỏi 2: Dựa trên môi trường hoạt động, có thể phân chia các phần mềm tạo website thành mấy loại?",
                    "options": ["2", "1", "4", "3"],
                    "answer": "2"
                },
                {
                    "question": "Câu hỏi 3: Phần mềm tạo website được chia thành 2 loại là",
                    "options": [
                        "phần mềm tạo website ngoại tuyến và phần mềm tạo website có sẵn.",
                        "phần mềm tạo website trực tuyến và phần mềm tạo website thụ động.",
                        "phần mềm tạo website trực tuyến và phần mềm tạo website ngoại tuyến.",
                        "phần mềm tạo website thụ động và phần mềm tạo website chủ động."
                    ],
                    "answer": "phần mềm tạo website trực tuyến và phần mềm tạo website ngoại tuyến."
                },
                {
                    "question": "Câu hỏi 4: Thế nào là phần mềm tạo website ngoại tuyến?",
                    "options": [
                        "Là phần mềm cài đặt sẵn trên máy tính và cần sử dụng môi trường mạng.",
                        "Là phần mềm không được cài đặt sẵn trên máy tính và không cần sử dụng môi trường mạng.",
                        "Là phần mềm cài đặt sẵn trên máy tính và không cần sử dụng môi trường mạng.",
                        "Là phần mềm được sử dụng trực tiếp trên môi trường mạng."
                    ],
                    "answer": "Là phần mềm cài đặt sẵn trên máy tính và không cần sử dụng môi trường mạng."
                },
                {
                    "question": "Câu hỏi 5: Thế nào là phần mềm tạo website trực tuyến?",
                    "options": [
                        "Là phần mềm cài đặt sẵn trên máy tính và cần sử dụng môi trường mạng.",
                        "Là phần mềm không được cài đặt sẵn trên máy tính và không cần sử dụng môi trường mạng.",
                        "Là phần mềm cài đặt sẵn trên máy tính và không cần sử dụng môi trường mạng.",
                        "Là phần mềm được sử dụng trực tiếp trên môi trường mạng mà không yêu cầu cài đặt trên máy tính."
                    ],
                    "answer": "Là phần mềm được sử dụng trực tiếp trên môi trường mạng mà không yêu cầu cài đặt trên máy tính."
                },
                {
                    "question": "Câu hỏi 6: Đâu không phải là tính năng của phần mềm tạo website trực tuyến?",
                    "options": [
                        "Cài đặt phần mềm trên máy tính.",
                        "Chèn các biểu mẫu.",
                        "Cung cấp mẫu trang web.",
                        "Tạo các trang web với nội dung văn bản."
                    ],
                    "answer": "Cài đặt phần mềm trên máy tính."
                },
                {
                    "question": "Câu hỏi 7: Chức năng nào sau đây không được cung cấp bởi phần mềm tạo website cơ bản?",
                    "options": [
                        "Chèn hình ảnh và video.",
                        "Tạo trò chơi trực tuyến.",
                        "Xuất bản website.",
                        "Chèn liên kết."
                    ],
                    "answer": "Tạo trò chơi trực tuyến."
                },
                {
                    "question": "Câu hỏi 8: Mobirise thuộc phân loại phần mềm nào?",
                    "options": [
                        "Là phần mềm ngoại tuyến có phí.",
                        "Là phần mềm ngoại tuyến miễn phí.",
                        "Là phần mềm trực tuyến miễn phí.",
                        "Là phần mềm trực tuyến có phí."
                    ],
                    "answer": "Là phần mềm ngoại tuyến miễn phí."
                },
                {
                    "question": "Câu hỏi 9: Phần mềm Mobirise có thể hoạt động trên hệ điều hành nào?",
                    "options": ["Windows", "Android", "iOS", "Chrome OS"],
                    "answer": "Windows"
                },
                {
                    "question": "Câu hỏi 10: Phần mềm Mobirise cung cấp nhiều mẫu trang web với ____.",
                    "options": [
                        "kiểu bố cục và chủ đề đa dạng.",
                        "chức năng lập lịch.",
                        "chức năng tạo trò chơi.",
                        "khả năng phân tích dữ liệu."
                    ],
                    "answer": "kiểu bố cục và chủ đề đa dạng."
                },
                {
                    "question": "Câu hỏi 11: Màn hình làm việc của phần mềm Mobirise gồm bao nhiêu thành phần chính?",
                    "options": ["1", "2", "3", "4"],
                    "answer": "3"
                },
                {
                    "question": "Câu hỏi 12: Phát biểu nào sau đây là đúng?",
                    "options": [
                        "Các phần mềm tạo website chỉ có thể hoạt động ngoại tuyến.",
                        "Có thể đăng nhập sử dụng phần mềm Mobirise qua tài khoản Google, Facebook hoặc email.",
                        "Phần mềm Mobirise chỉ cho phép tại trang web từ các mẫu trang web theo chủ đề được cung cấp sẵn.",
                        "Sử dụng phần mềm Mobirise tạo trang web bằng cách viết mã lệnh."
                    ],
                    "answer": "Có thể đăng nhập sử dụng phần mềm Mobirise qua tài khoản Google, Facebook hoặc email."
                },
                {
                    "question": "Câu hỏi 13: Các trang web có phần mở rộng là gì?",
                    "options": [".html", ".tml", ".tlm", "tmh"],
                    "answer": ".html"
                },
                {
                    "question": "Câu hỏi 14: Về cơ bản, mỗi website gồm bao nhiêu trang web chính?",
                    "options": ["1", "2", "3", "4"],
                    "answer": "3"
                },
                {
                    "question": "Câu hỏi 15: Trang nào trong website thường chứa các mục nội dung nổi bật nhất?",
                    "options": [
                        "Trang chủ.",
                        "Trang chuyên mục.",
                        "Trang chi tiết.",
                        "Trang liên hệ."
                    ],
                    "answer": "Trang chủ."
                },
                {
                    "question": "Câu hỏi 16: Trang web nào có chức năng hiển thị thông tin cụ thể về các mục nội dung của website?",
                    "options": [
                        "Trang chủ.",
                        "Trang chuyên mục.",
                        "Trang chi tiết.",
                        "Trang giới thiệu."
                    ],
                    "answer": "Trang chi tiết."
                },
                {
                    "question": "Câu hỏi 17: Mỗi trang web thường có bao nhiêu thành phần cơ bản?",
                    "options": ["1", "4", "2", "3"],
                    "answer": "3"
                },
                {
                    "question": "Câu hỏi 18: Trang chuyên mục có ý nghĩa gì?",
                    "options": [
                        "Giúp website có tính chuyên nghiệp hơn.",
                        "Giúp người xem giới hạn phạm vi tìm kiếm thông tin thuộc chủ đề mình quan tâm trong website.",
                        "Giúp tạo ra các trang web nhỏ.",
                        "Giúp phân loại người dùng."
                    ],
                    "answer": "Giúp người xem giới hạn phạm vi tìm kiếm thông tin thuộc chủ đề mình quan tâm trong website."
                },
                {
                    "question": "Câu hỏi 19: Thành phần nào của trang web giúp người dùng dễ dàng di chuyển giữa các trang?",
                    "options": [
                        "Phần đầu trang.",
                        "Phần nội dung.",
                        "Thanh điều hướng.",
                        "Phần chân trang."
                    ],
                    "answer": "Thanh điều hướng."
                },
                {
                    "question": "Câu hỏi 20: Phần nào của trang web thường chứa các liên kết nhanh và thông tin bản quyền?",
                    "options": [
                        "Phần đầu trang.",
                        "Thanh điều hướng.",
                        "Phần nội dung.",
                        "Phần chân trang."
                    ],
                    "answer": "Phần chân trang."
                }
            ],
            "Chủ đề F": [
                    {
                    "question": "Câu 1: HTML là viết tắt của",
                    "options": [
                        "Hypertext Markup Language",
                        "Hyperlink and Text Markup Language",
                        "Hypertext Multi-language",
                        "Hypertext Media Language"
                    ],
                    "answer": "Hypertext Markup Language"
                },
                {
                    "question": "Câu 2: Ngôn ngữ đánh dấu siêu văn bản (HTML) được sử dụng chủ yếu để làm gì?",
                    "options": [
                        "Tạo bảng tính",
                        "Tạo trang web",
                        "Lập trình ứng dụng",
                        "Xử lý dữ liệu"
                    ],
                    "answer": "Tạo trang web"
                },
                {
                    "question": "Câu 3: Trong HTML, dấu “/” trong thẻ có ý nghĩa gì?",
                    "options": [
                        "Đánh dấu phần tử bị lỗi",
                        "Kết thúc thẻ",
                        "Bắt đầu thẻ",
                        "Chỉ thị kiểu chữ"
                    ],
                    "answer": "Kết thúc thẻ"
                },
                {
                    "question": "Câu 4: Tên thẻ HTML có phân biệt chữ hoa và chữ thường không?",
                    "options": [
                        "Có phân biệt",
                        "Không phân biệt",
                        "Chỉ phân biệt trong các trình duyệt khác nhau",
                        "Phân biệt trong các phiên bản khác nhau"
                    ],
                    "answer": "Không phân biệt"
                },
                {
                    "question": "Câu 5: Phần nào của tài liệu HTML chứa nội dung sẽ hiển thị trên màn hình của trình duyệt web?",
                    "options": [
                        "Phần đầu",
                        "Phần chân",
                        "Phần thân",
                        "Phần meta"
                    ],
                    "answer": "Phần thân"
                },
                {
                    "question": "Câu 6: Dòng đầu tiên của văn bản HTML thường là gì?",
                    "options": [
                        "Tiêu đề của trang web",
                        "Doctype",
                        "Nội dung của trang web",
                        "Siêu dữ liệu"
                    ],
                    "answer": "Doctype"
                },
                {
                    "question": "Câu 7: Khi soạn thảo văn bản HTML trong Sublime Text, bạn nên lưu tệp với định dạng nào?",
                    "options": [
                        ".txt",
                        ".html",
                        ".docx",
                        ".xml"
                    ],
                    "answer": ".html"
                },
                {
                    "question": "Câu 8: Phần tử nào được sử dụng để xác định phần đầu của một tài liệu HTML?",
                    "options": [
                        "<body>",
                        "<footer>",
                        "<head>",
                        "<header>"
                    ],
                    "answer": "<head>"
                },
                {
                    "question": "Câu 9: Thẻ nào trong phần đầu của tài liệu HTML dùng để khai báo tiêu đề của trang web?",
                    "options": [
                        "<title>",
                        "<header>",
                        "<footer>",
                        "<meta>"
                    ],
                    "answer": "<title>"
                },
                {
                    "question": "Câu 10: Để xem kết quả của tệp HTML, bạn cần làm gì sau khi lưu tệp?",
                    "options": [
                        "Mở tệp bằng trình soạn thảo văn bản",
                        "Gửi tệp qua email",
                        "Chạy tệp trên máy chủ",
                        "Mở tệp bằng trình duyệt web"
                    ],
                    "answer": "Mở tệp bằng trình duyệt web"
                },
                {
                    "question": "Câu 11: Số phát biểu đúng là?\n"
                                "a) Thẻ HTML thường không có thẻ kết thúc.\n"
                                "b) Tên thẻ HTML không phân biệt chữ hoa và chữ thường.\n"
                                "c) Phần đầu của một tệp HTML được xác định bởi thẻ <head> và </head>.\n"
                                "d) Thẻ <body> chứa nội dung chính hiển thị trên màn hình của trình duyệt.",
                    "options": [
                        "1",
                        "2",
                        "3",
                        "4"
                    ],
                    "answer": "3"
                },
                {
                    "question": "Câu 12: HTML hỗ trợ bao nhiêu cấp tiêu đề mục từ lớn đến nhỏ?",
                    "options": [
                        "3",
                        "4",
                        "5",
                        "6"
                    ],
                    "answer": "6"
                },
                {
                    "question": "Câu 13: Phần tử <a> trong HTML được sử dụng để làm gì?",
                    "options": [
                        "Tạo các đoạn văn bản",
                        "Tạo các tiêu đề",
                        "Tạo các siêu liên kết",
                        "Tạo các bảng"
                    ],
                    "answer": "Tạo các siêu liên kết"
                },
                {
                    "question": "Câu 14: Phần tử nào trong HTML được sử dụng để in đậm văn bản?",
                    "options": [
                        "<strong>",
                        "<em>",
                        "<mark>",
                        "<b>"
                    ],
                    "answer": "<strong>"
                },
                {
                    "question": "Câu 15: Thẻ nào dùng để chèn hình ảnh vào trang web?",
                    "options": [
                        "<img>",
                        "<picture>",
                        "<photo>",
                        "<image>"
                    ],
                    "answer": "<img>"
                },
                {
                    "question": "Câu 16: Thẻ nào được sử dụng để tạo các đoạn văn bản trên trang web trong HTML?",
                    "options": [
                        "<h1>",
                        "<a>",
                        "<p>",
                        "<div>"
                    ],
                    "answer": "<p>"
                },
                {
                    "question": "Câu 17: Thẻ nào trong HTML được sử dụng để định nghĩa tiêu đề cho một bảng?",
                    "options": [
                        "<thead>",
                        "<title>",
                        "<header>",
                        "<footer>"
                    ],
                    "answer": "<thead>"
                },
                {
                    "question": "Câu 18: Thẻ nào được dùng để tạo tiêu đề cấp 1 trong HTML?",
                    "options": [
                        "<header>",
                        "<h1>",
                        "<title>",
                        "<head>"
                    ],
                    "answer": "<h1>"
                },
                {
                    "question": "Câu 19: Để tạo một đoạn văn bản mới trong HTML, ta sử dụng thẻ",
                    "options": [
                        "<p>",
                        "<div>",
                        "<span>",
                        "<br>"
                    ],
                    "answer": "<p>"
                },
                {
                    "question": "Câu 20: Cú pháp <strong> Nội dung </strong> sử dụng để",
                    "options": [
                        "Tô màu đỏ nội dung",
                        "In nghiêng nội dung",
                        "Tô màu vàng nội dung",
                        "In đậm nội dung"
                    ],
                    "answer": "In đậm nội dung"
                }
            ]
        }
    }
    
    # Bước 1: Chọn lớp
    selected_class = st.selectbox("📚 Chọn lớp:", ["-- Chọn lớp --", "10", "11", "12"])
    
    # Bước 2: Chọn chủ đề (chỉ khi lớp hợp lệ)
    if selected_class in question_bank:
        topics = list(question_bank[selected_class].keys())
        selected_topic = st.selectbox("📂 Chọn chủ đề:", ["-- Chọn chủ đề --"] + topics)
    
        # Bước 3: Chỉ hiển thị câu hỏi khi chủ đề đã chọn hợp lệ
        if selected_topic in question_bank[selected_class]:
            questions = question_bank[selected_class][selected_topic]
            st.markdown("### 📋 Trả lời câu hỏi:")
            
            # Danh sách chứa câu trả lời của người dùng
            user_answers = []
    
            # Hiển thị câu hỏi và các lựa chọn
            for i, q in enumerate(questions):
                ans = st.radio(q["question"], q["options"], key=f"{selected_class}_{selected_topic}_{i}")
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
    
                    if is_correct:
                        score += 1
                        st.markdown(f"✅ **Câu {i+1}: Đúng**")
                    else:
                        st.markdown(f"❌ **Câu {i+1}: Sai**")
                        st.markdown(f"- Bạn chọn: `{user_answer}`")
                        st.markdown(f"- Đáp án đúng: `{correct_answer}`")
                    st.markdown("---")
    
                # Hiển thị điểm
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
