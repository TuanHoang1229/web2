import streamlit as st
from PIL import Image

st.set_page_config(page_title="Học Tin Học", layout="wide")

# Sidebar navigation
pages = {
    "Trang chủ": "home",
    "Lập trình Scratch": "scratch",
    "Thiết kế Web cơ bản": "web_design",
    "An toàn thông tin": "cyber_security",
    "Tin học văn phòng": "office",
    "Kho tài liệu": "resources",
    "Liên kết học tập mở": "external_links",
    "Trắc nghiệm tự luyện": "quiz",
    "Góc chia sẻ": "sharing"
}

page = st.sidebar.radio("Chọn chuyên mục:", list(pages.keys()))

if page == "Trang chủ":
    st.title("Chào mừng đến với Website Học Tin Học")
    st.markdown("""
    ### Mục tiêu:
    Trang web hỗ trợ học sinh tiếp cận kiến thức Tin học thông qua các chuyên đề học tập, tài liệu, video và bài thực hành.

    ### Liên kết nhanh:
    - [Lập trình Scratch](#)
    - [Thiết kế Web](#)
    - [An toàn thông tin](#)
    - [Văn phòng](#)

    ### Tin mới:
    - Cập nhật thêm 5 bài trắc nghiệm mới về An toàn thông tin
    - Thêm file mẫu Word/Excel mới
    """)

elif page == "Lập trình Scratch":
    st.header("Lập trình Scratch")
    st.video("https://www.youtube.com/watch?v=OjV63cPSzco")  # ví dụ
    st.markdown("### Tải bài thực hành:")
    st.download_button("Tải bài tập mẫu (.sb3)", "fake_sb3_data", file_name="baitap.sb3")

    st.markdown("### Trắc nghiệm:")
    st.markdown("[Làm bài trên Google Forms](https://forms.gle/...)")

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

elif page == "Tin học văn phòng":
    st.header("Tin học Văn phòng")
    st.markdown("### File mẫu và hướng dẫn")
    st.download_button("Tải File Word mẫu", "fake_word_data", file_name="baitap.docx")
    st.download_button("Tải File Excel mẫu", "fake_excel_data", file_name="baitap.xlsx")

elif page == "Kho tài liệu":
    st.header("Kho tài liệu")
    st.markdown("### Tài liệu PDF:")
    st.download_button("Tải PDF bài giảng", "fake_pdf", file_name="baigiang.pdf")

elif page == "Liên kết học tập mở":
    st.header("Liên kết học tập mở")
    st.markdown("""
    - [Kênh YouTube học lập trình](https://www.youtube.com/@codekid)
    - [Khan Academy](https://www.khanacademy.org/)
    - [Sách giáo khoa Tin học lớp 6](https://hanhtrangso.nxbgd.vn/)
    """)

elif page == "Trắc nghiệm tự luyện":
    st.header("Trắc nghiệm tự luyện")
    st.markdown("Chọn chuyên đề:")
    topic = st.selectbox("Chuyên đề", ["Scratch", "An toàn thông tin", "Tin học văn phòng"])
    st.markdown("Làm bài trắc nghiệm:")
    st.markdown(f"[Bắt đầu bài trắc nghiệm về {topic}](https://forms.gle/...)")

elif page == "Góc chia sẻ":
    st.header("Góc chia sẻ - Gửi bài thực hành")
    st.markdown("Gửi bài qua Google Forms:")
    st.markdown("[Biểu mẫu gửi bài](https://forms.gle/...)")
    st.markdown("Hoặc chia sẻ trên Notion (nếu có tài khoản).")

