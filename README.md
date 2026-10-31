# Trang Web Trắc Nghiệm Kiến Trúc Máy Tính - Ôn Thi Giữa Kỳ

Ứng dụng web trắc nghiệm thông minh được xây dựng từ tài liệu ôn thi giữa kỳ môn Kiến trúc máy tính (Trường Đại học Cần Thơ - CTU): `[studocu.com] - Tài liệu kiến trúc máy tính giữa kỳ - Tóm tắt và câu hỏi ôn tập 2023.pdf`.

---

## 🚀 Cách Mở Và Sử Dụng Trang Web

Bạn có thể chạy ứng dụng theo bất kỳ cách nào dưới đây:

### Cách 1: Mở trực tiếp (Nhanh nhất)
1. Nhấp đúp chuột vào file **`start_quiz.bat`** (hoặc mở trực tiếp file **`index.html`** bằng trình duyệt bất kỳ: Chrome, Edge, Cốc Cốc, Firefox).
2. Trang web sẽ mở ra ngay lập tức với đầy đủ tính năng mà không cần cài đặt thêm bất cứ phần mềm hay thư viện nào.

### Cách 2: Chạy qua Local HTTP Server (Tùy chọn)
Mở terminal tại thư mục dự án và chạy:
```powershell
python -m http.server 8000
```
Sau đó truy cập: `http://localhost:8000`

---

## 🌟 Các Tính Năng Nổi Bật

### 1. Mục 1: Chọn Chế Độ Ôn Theo Từng Đề
- Hệ thống chia thành **5 bộ đề thi** chuẩn hóa:
  - **Đề 1** (17 câu): Ngăn xếp Stack, số thực dấu phẩy động, định dạng lệnh MIPS, bus hệ thống, mảng trong bộ nhớ, tính toán hiệu suất CPI.
  - **Đề 2** (18 câu): Phân cấp bộ nhớ, CPU & Datapath, hiệu suất CPI & IPS, mã hóa lệnh MIPS sang Hex, mô phỏng vòng lặp Assembly.
  - **Đề 3** (20 câu): Thao tác biến 32-bit trong bộ nhớ, chu trình nạp lệnh CPU, biểu diễn số âm bù 2, thứ tự Little-Endian, bus địa chỉ tối thiểu.
  - **Đề 4** (20 câu): Bus điều khiển, số dấu phẩy động 32-bit IEEE 754, so sánh hiệu năng CPU theo chu kỳ xung nhịp, cơ chế ngắt hệ thống.
  - **Đề 5** (17 câu): Các thành phần phần cứng cơ bản, so sánh IPS giữa các CPU, tính toán dung lượng ảnh 2K, quy trình thủ tục MIPS, mã máy addi & srl.
- Mỗi đề đều có nút **"Làm bài ngay"** và nút **"⚙️ Tùy chọn"** để cấu hình riêng.

### 2. Mục 2: Ôn Tổng Hợp Tất Cả Các Đề
- Tổng hợp toàn bộ **92 câu hỏi** trắc nghiệm của cả 5 bộ đề.
- **Tùy chọn số lượng câu linh hoạt**:
  - 10 câu nhanh
  - 20 câu tiêu chuẩn
  - 40 câu nâng cao
  - Toàn bộ 92 câu
- **Lọc theo chuyên đề kiến thức**:
  - Kiến trúc tập lệnh MIPS & Hợp ngữ
  - Hiệu suất máy tính, CPI, IPS & Chu kỳ clock
  - Hệ thống số & Biểu diễn dữ liệu (Bù 2, Phép toán bit, Dấu phẩy động IEEE 754)
  - Phân cấp bộ nhớ & Ngăn xếp (Stack, RAM, Cache, SSD)
  - Bus & Giao tiếp hệ thống (Bus địa chỉ, dữ liệu, điều khiển)
  - Chu trình thực thi lệnh của CPU

### 3. Các Tùy Chọn Tùy Biến Mỗi Lần Thi
- **Tùy chọn xáo trộn**:
  - 🔀 **Xáo trộn toàn bộ**: Xáo trộn ngẫu nhiên vị trí câu hỏi VÀ thứ tự đáp án A/B/C/D mỗi lần làm bài (đảm bảo không bao giờ bị trùng lặp vị trí).
  - 🔀 **Chỉ xáo trộn câu hỏi**: Thay đổi thứ tự câu hỏi, giữ nguyên thứ tự đáp án.
  - 📋 **Thứ tự mặc định**: Giữ nguyên 100% theo thứ tự gốc của tài liệu.
- **Chế độ làm bài**:
  - 💡 **Chế độ Luyện tập (Study Mode)**: Biết ngay kết quả Đúng (xanh lá) / Sai (đỏ) ngay khi chọn và hiện khung **Giải thích chi tiết cặn kẽ từng bước** (công thức, giải mã MIPS, tính toán nhị phân).
  - ⏱️ **Chế độ Thi thử (Exam Mode)**: Có đồng hồ đếm ngược thời gian, làm xong mới bấm "Nộp bài" để tính điểm trên thang điểm 10, xếp loại học lực và phân tích năng lực theo từng chuyên đề.
- **Thời gian làm bài**:
  - Gợi ý tự động theo đề (1.5 phút/câu)
  - 15 phút, 30 phút, 45 phút hoặc Không giới hạn thời gian.

### 4. Công Cụ Hỗ Trợ Học Tập Nâng Cao
- **Bảng điều hướng câu hỏi (Question Palette)**: Nhấp chuột nhảy ngay đến bất kỳ câu nào; hiển thị màu sắc trực quan (Đã làm, Chưa làm, Đã gắn cờ, Đúng/Sai).
- **Đánh dấu câu hỏi (Flag / Bookmark ⭐)**: Lưu lại các câu khó hoặc cần chú ý để xem lại bất cứ lúc nào.
- **Ôn lại câu làm sai (Mistakes Practice 🔄)**: Tự động gom những câu bạn từng trả lời sai vào mục riêng để bạn luyện lại cho đến khi thành thạo 100%.
- **Lịch sử làm bài (History 📊)**: Lưu lại điểm số, tỷ lệ % và thời gian làm bài của các lần thi trước vào bộ nhớ trình duyệt (LocalStorage).
- **Giao diện Sáng / Tối (Dark / Light Mode 🌙/☀️)**: Giúp học tập lâu không mỏi mắt.
- **Hỗ trợ phím tắt bàn phím**:
  - `A`, `B`, `C`, `D` hoặc `1`, `2`, `3`, `4`: Chọn nhanh đáp án
  - `←`, `→` hoặc `J`, `K`: Chuyển câu trước / câu sau
  - `F`: Đánh dấu / Gỡ cờ câu hỏi
  - `T`: Đổi giao diện Sáng / Tối
  - `Esc`: Đóng hộp thoại / modal

---

## 📁 Cấu Trúc Thư Mục

```
Bot-QTHT/
├── index.html          # Giao diện chính của ứng dụng
├── styles.css          # Hệ thống giao diện, hiệu ứng và Dark/Light mode
├── app.js              # Toàn bộ logic ứng dụng, xáo trộn, timer, chấm điểm
├── quiz_data.js        # Dữ liệu 92 câu hỏi trắc nghiệm kèm giải thích chi tiết
├── questions.json      # File dữ liệu JSON chuẩn hóa
├── start_quiz.bat      # Phím tắt mở nhanh trên Windows
└── README.md           # Hướng dẫn sử dụng chi tiết
```
