import json

# Complete verified question bank from [studocu.com] - Tài liệu kiến trúc máy tính giữa kỳ - Tóm tắt và câu hỏi ôn tập 2023.pdf
# Cleaned, deduplicated, verified answers, detailed step-by-step explanations

exams = [
    {
        "id": 1,
        "title": "Đề số 1: Đề ôn thi Giữa kỳ Kiến trúc máy tính",
        "description": "Các kiến thức về ngăn xếp Stack, số thực dấu phẩy động, định dạng lệnh MIPS, bus hệ thống, mảng trong bộ nhớ, tính toán hiệu suất CPI.",
        "duration_minutes": 30,
        "questions": [
            {
                "id": "d1_q1",
                "question_num": 1,
                "content": "Vùng nhớ Stack có cấu trúc lưu trữ theo kiểu nào?",
                "code": "",
                "options": [
                    "LIFO (Last In First Out)",
                    "LILO (Last In Last Out)",
                    "FIFO (First In First Out)",
                    "FILO (First In Last Out)"
                ],
                "correct_index": 0,
                "explanation": "Ngăn xếp (Stack) lưu trữ dữ liệu theo nguyên lý LIFO (Last In First Out - Vào sau ra trước). Phần tử được đẩy vào cuối cùng sẽ là phần tử đầu tiên được lấy ra.",
                "category": "Bộ nhớ & Ngăn xếp"
            },
            {
                "id": "d1_q2",
                "question_num": 2,
                "content": "Số dấu phẩy động không thể biểu diễn chính xác được số nào?",
                "code": "",
                "options": [
                    "0.5",
                    "0.4",
                    "12",
                    "2"
                ],
                "correct_index": 1,
                "explanation": "Trong hệ nhị phân, số thập phân 0.4 chuyển sang nhị phân là 0.011001100110... (tuần hoàn vô hạn). Do đó chuẩn dấu phẩy động IEEE 754 với số bit hữu hạn không thể biểu diễn chính xác hoàn toàn số 0.4 mà chỉ có giá trị xấp xỉ.",
                "category": "Biểu diễn số thực"
            },
            {
                "id": "d1_q3",
                "question_num": 3,
                "content": "Mã máy của 1 lệnh dạng I được viết ở hệ 16 là 0x2149001A. Hãy cho biết toán hạng hằng số bằng bao nhiêu?",
                "code": "",
                "options": [
                    "2149001A (viết ở hệ 16)",
                    "26 (viết ở hệ 10)",
                    "19 (viết ở hệ 10)",
                    "33 (viết ở hệ 10)"
                ],
                "correct_index": 1,
                "explanation": "Định dạng lệnh I trong kiến trúc MIPS có trường hằng số / địa chỉ (Immediate) nằm ở 16 bit cuối. Với mã máy 0x2149001A, 16 bit cuối là 0x001A (hệ 16) = 1 * 16 + 10 = 26 (ở hệ 10).",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d1_q4",
                "question_num": 4,
                "content": "Lớp học Kiến trúc máy tính có 150 sinh viên. Vậy biến số nguyên để đếm số sinh viên cần có tối thiểu mấy bit?",
                "code": "",
                "options": [
                    "10",
                    "7",
                    "9",
                    "8"
                ],
                "correct_index": 3,
                "explanation": "Số trạng thái biểu diễn bởi n bit là 2^n. Với n = 7 bit biểu diễn tối đa 2^7 = 128 < 150 sinh viên. Với n = 8 bit biểu diễn được 2^8 = 256 >= 150 sinh viên. Vậy cần tối thiểu 8 bit.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d1_q5",
                "question_num": 5,
                "content": "Với lệnh hợp ngữ sw $t2, 4($t4) giá trị 4+$t4 sẽ được truyền đi từ CPU tới bộ nhớ chính trên đường bus nào?",
                "code": "",
                "options": [
                    "bus dữ liệu",
                    "bus địa chỉ",
                    "bus điều khiển",
                    "bus ngoại vi"
                ],
                "correct_index": 1,
                "explanation": "Lệnh sw (Store Word) ghi dữ liệu từ thanh ghi $t2 vào ô nhớ có địa chỉ là 4 + $t4. Vì 4 + $t4 là địa chỉ ô nhớ cần truy xuất nên nó phải được truyền trên Bus địa chỉ (Address Bus). Giá trị thanh ghi $t2 mới được truyền trên Bus dữ liệu.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d1_q6",
                "question_num": 6,
                "content": "Mảng số nguyên 32-bit A có phần tử A[6] ở địa chỉ 0x20200508. Hỏi phần tử A[9] ở địa chỉ nào?",
                "code": "",
                "options": [
                    "0x20200514",
                    "0x2020051C",
                    "0x202005C0",
                    "0x20200511"
                ],
                "correct_index": 0,
                "explanation": "Mỗi phần tử số nguyên 32-bit chiếm 4 byte. Khoảng cách giữa A[9] và A[6] là (9 - 6) = 3 phần tử, tương ứng 3 * 4 = 12 bytes (hệ 16 là 0xC). Địa chỉ A[9] = 0x20200508 + 0xC = 0x20200514.",
                "category": "Địa chỉ bộ nhớ & Mảng"
            },
            {
                "id": "d1_q7",
                "question_num": 7,
                "content": "Hỏi khi thực hiện đoạn hợp ngữ MIPS sau, thanh ghi $t0 nhận giá trị nào của mảng? Biết rằng mảng số nguyên 32-bit A có địa chỉ cơ sở là 0x20201234.",
                "code": "lui  $s0, 0x2020\naddi $s0, $s0, 0x1230\nlw   $t0, 8($s0)",
                "options": [
                    "A[2]",
                    "A[0]",
                    "A[1]",
                    "A[3]"
                ],
                "correct_index": 2,
                "explanation": "Sau lệnh lui và addi, thanh ghi $s0 chứa địa chỉ: 0x20200000 + 0x1230 = 0x20201230. Lệnh lw $t0, 8($s0) đọc dữ liệu tại địa chỉ 0x20201230 + 8 = 0x20201238. Mảng A có địa chỉ cơ sở A[0] = 0x20201234. Mỗi phần tử 32-bit cách nhau 4 byte: A[1] nằm tại 0x20201234 + 4 = 0x20201238. Vậy $t0 nhận giá trị A[1].",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d1_q8",
                "question_num": 8,
                "content": "Số nguyên 8-bit nào sau đây có dạng biểu diễn ở hệ 16 là 0xB2?",
                "code": "",
                "options": [
                    "Là số 10110010 ở hệ 2",
                    "Là số 177 ở hệ 10, không dấu",
                    "Là số 00100010 ở hệ 2",
                    "Là số 179 ở hệ 10, không dấu"
                ],
                "correct_index": 0,
                "explanation": "Chuyển từng ký tự hex sang 4 bit nhị phân: 'B' = 11(10) = 1011(2), '2' = 2(10) = 0010(2). Do đó 0xB2 = 10110010(2). (Ở hệ 10 không dấu, 0xB2 = 11*16 + 2 = 178).",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d1_q9",
                "question_num": 9,
                "content": "Biểu thức logic giữa 2 số 8-bit là: 0x3F = 0x3C ??? 0x0F bị thiếu mất phép toán logic. Phép toán đó là gì?",
                "code": "",
                "options": [
                    "AND",
                    "XOR",
                    "NOT",
                    "OR"
                ],
                "correct_index": 3,
                "explanation": "Đổi sang nhị phân: 0x3C = 0011 1100(2), 0x0F = 0000 1111(2). Khi thực hiện phép OR bit: 0011 1100 OR 0000 1111 = 0011 1111(2) = 0x3F. Vậy phép toán còn thiếu là OR.",
                "category": "Đại số Boole & Phép toán bit"
            },
            {
                "id": "d1_q10",
                "question_num": 10,
                "content": "Bộ xử lý MIPS có tần số xung nhịp 2GHz thực hiện phần mềm gồm 400.000 lệnh máy trong 0.0003 giây. Hỏi phần mềm đó có CPI trung bình bằng bao nhiêu?",
                "code": "",
                "options": [
                    "1.4",
                    "1.6",
                    "1.8",
                    "1.5"
                ],
                "correct_index": 3,
                "explanation": "Thời gian CPU = (Số lệnh * CPI) / Clock Rate => CPI = (Thời gian * Clock Rate) / Số lệnh. Thay số: CPI = (0.0003 * 2 * 10^9) / 400.000 = 600.000 / 400.000 = 1.5.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d1_q11",
                "question_num": 11,
                "content": "Tổng của 2 số 8-bit có dấu nào sau đây sẽ bị hiện tượng tràn số học (Overflow)? (Số được viết ở hệ 2)",
                "code": "",
                "options": [
                    "01010001 + 00101100",
                    "01010001 + 01001100",
                    "00101100 + 11000010",
                    "10010001 + 11010011"
                ],
                "correct_index": 3,
                "explanation": "Hiện tượng tràn số học có dấu xảy ra khi cộng 2 số cùng dấu nhưng kết quả ra trái dấu. Ở lựa chọn 4: 10010001 (-111) và 11010011 (-45) đều là 2 số âm (bit MSB = 1). Tổng của chúng là -156, vượt quá ngưỡng biểu diễn của số 8-bit có dấu [-128, 127], kết quả phép cộng bit MSB bị biến thành 0 (dương) => Tràn số.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d1_q12",
                "question_num": 12,
                "content": "Trong kiến trúc máy tính, khái niệm USB nói về điều gì?",
                "code": "",
                "options": [
                    "Ổ lưu trữ",
                    "Bus ngoại vi giữa module I/O và thiết bị",
                    "Khe cắm mở rộng",
                    "Nhà sản xuất linh kiện"
                ],
                "correct_index": 1,
                "explanation": "USB là viết tắt của Universal Serial Bus - chuẩn bus ngoại vi nối tiếp dùng để kết nối và truyền thông tin giữa máy tính (thông qua module I/O) và các thiết bị ngoại vi.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d1_q13",
                "question_num": 13,
                "content": "Hỏi máy tính có địa chỉ 24 bit. Biết rằng máy tính đã cắm 1 thanh RAM 8 MiB. Hỏi máy tính có thể lắp thêm 1 thanh RAM kích thước LỚN NHẤT là bao nhiêu và KHÔNG THỪA? (Giả định máy tính này không có cổng vào ra)",
                "code": "",
                "options": [
                    "2 MiB",
                    "4 MiB",
                    "16 MiB",
                    "8 MiB"
                ],
                "correct_index": 3,
                "explanation": "Với 24 bit địa chỉ, không gian bộ nhớ tối đa CPU có thể quản lý được là 2^24 Bytes = 16 MiB. Máy tính đã cắm 1 thanh RAM 8 MiB, do đó dung lượng còn trống tối đa là 16 MiB - 8 MiB = 8 MiB.",
                "category": "Địa chỉ bộ nhớ & Mảng"
            },
            {
                "id": "d1_q14",
                "question_num": 14,
                "content": "Lệnh nào có định dạng lệnh (R / I / J) không giống với các lệnh còn lại?",
                "code": "",
                "options": [
                    "lui $t1, 9",
                    "xori $t1, $t5, 2",
                    "ori $t1, $t2, 6",
                    "add $t1, $t2, $t3"
                ],
                "correct_index": 3,
                "explanation": "Các lệnh lui, xori, ori đều là lệnh dạng I (Immediate). Riêng lệnh add $t1, $t2, $t3 là lệnh dạng R (Register) thao tác hoàn toàn trên các thanh ghi.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d1_q15",
                "question_num": 15,
                "content": "Một hệ thống máy tính có không gian địa chỉ bộ nhớ là 64 GiB. Hỏi bus địa chỉ có độ rộng tối thiểu bằng bao nhiêu bit?",
                "code": "",
                "options": [
                    "37",
                    "34",
                    "35",
                    "36"
                ],
                "correct_index": 3,
                "explanation": "64 GiB = 64 * 2^30 Bytes = 2^6 * 2^30 Bytes = 2^36 Bytes. Để định vị được 2^36 ô nhớ (mỗi ô 1 byte), Bus địa chỉ cần độ rộng tối thiểu bằng 36 bit.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d1_q16",
                "question_num": 16,
                "content": "Một chương trình hợp ngữ MIPS có 8 lệnh ADDI, 5 lệnh SUB, 1 lệnh LUI, 3 lệnh XORI. Hỏi mã máy của phần mềm trên chiếm bao nhiêu byte dung lượng?",
                "code": "",
                "options": [
                    "18",
                    "72",
                    "17",
                    "68"
                ],
                "correct_index": 3,
                "explanation": "Tổng số lệnh của chương trình = 8 + 5 + 1 + 3 = 17 lệnh. Trong kiến trúc MIPS 32-bit, mỗi lệnh máy có độ dài cố định 32 bit = 4 byte. Dung lượng mã máy = 17 * 4 = 68 byte.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d1_q17",
                "question_num": 17,
                "content": "Đoạn hợp ngữ MIPS sau có lệnh đầu tiên ở địa chỉ 0xBCDE8004. Hỏi lệnh cuối cùng ở địa chỉ nào?",
                "code": "lui  $s0, 0x2020\naddi $s0, $s0, 0x1238\nlw   $t0, 4($s0)",
                "options": [
                    "không xác định",
                    "0xBCDE8006",
                    "0x20201238",
                    "0xBCDE800C"
                ],
                "correct_index": 3,
                "explanation": "Mỗi lệnh máy MIPS chiếm 4 byte:\n- Lệnh 1 (lui) tại địa chỉ: 0xBCDE8004\n- Lệnh 2 (addi) tại địa chỉ: 0xBCDE8004 + 4 = 0xBCDE8008\n- Lệnh 3 (lw - lệnh cuối) tại địa chỉ: 0xBCDE8008 + 4 = 0xBCDE800C.",
                "category": "Kiến trúc tập lệnh MIPS"
            }
        ]
    },
    {
        "id": 2,
        "title": "Đề số 2: Bài tập trắc nghiệm Kiến trúc máy tính G6.2 & G2.1",
        "description": "Phân cấp bộ nhớ, định dạng lệnh R/I, hiệu suất tính toán CPI & IPS, mã hóa lệnh MIPS sang Hex và mô phỏng thực thi đoạn mã.",
        "duration_minutes": 35,
        "questions": [
            {
                "id": "d2_q1",
                "question_num": 1,
                "content": "Sắp xếp các bộ nhớ có tốc độ truy xuất chậm dần?",
                "code": "",
                "options": [
                    "Register > RAM > Cache > SSD",
                    "Register > Cache > SSD > RAM",
                    "Cache > Register > RAM > SSD",
                    "Register > Cache > RAM > SSD"
                ],
                "correct_index": 3,
                "explanation": "Theo tháp phân cấp bộ nhớ (Memory Hierarchy), tốc độ từ nhanh nhất đến chậm dần: Thanh ghi (Register) -> Bộ nhớ đệm (Cache: L1, L2, L3) -> Bộ nhớ chính (RAM) -> Ổ lưu trữ thứ cấp (SSD / HDD).",
                "category": "Phân cấp bộ nhớ"
            },
            {
                "id": "d2_q2",
                "question_num": 2,
                "content": "Trong ngữ cảnh máy tính, \"CPU\" là viết tắt của từ gì?",
                "code": "",
                "options": [
                    "Computer Processing Unit",
                    "Central Processor Unit",
                    "Central Processing Unit",
                    "Control Processing Unit"
                ],
                "correct_index": 2,
                "explanation": "CPU là từ viết tắt của Central Processing Unit (Đơn vị xử lý trung tâm).",
                "category": "Tổng quan kiến trúc máy tính"
            },
            {
                "id": "d2_q3",
                "question_num": 3,
                "content": "Bộ nhớ SSD hoặc HDD thuộc loại nào trong phân cấp bộ nhớ?",
                "code": "",
                "options": [
                    "Cache memory",
                    "Secondary memory",
                    "Primary memory",
                    "Volatile Memory"
                ],
                "correct_index": 1,
                "explanation": "SSD và HDD là bộ nhớ thứ cấp (Secondary Memory / Secondary Storage) dùng để lưu trữ lâu dài không bay hơi, trong khi RAM là Primary Memory.",
                "category": "Phân cấp bộ nhớ"
            },
            {
                "id": "d2_q4",
                "question_num": 4,
                "content": "Câu lệnh assembly MIPS “addi $s3, $s5, 8” có định dạng như thế nào trong các lựa chọn sau?",
                "code": "",
                "options": [
                    "opcode (6bits) - rs(5bits) - rt(5 bits) - const/address(16bits)",
                    "opcode (6bits) - address(26bits)",
                    "opcode (6bits) - rd(5bits) - rs(5 bits) - shamt(5bits) - funct(6bits)",
                    "opcode (6bits) - rs(5bits) - rt(5 bits) - rd(5bits) - shamt(5bits) - funct(6bits)"
                ],
                "correct_index": 0,
                "explanation": "Lệnh addi thuộc kiểu I (Immediate Type). Định dạng lệnh I gồm: opcode (6 bits) - rs (5 bits) - rt (5 bits) - const/address (16 bits).",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d2_q5",
                "question_num": 5,
                "content": "Thành phần nào dưới đây là thành phần phần cứng cơ bản của bộ xử lý (Processor)?",
                "code": "",
                "options": [
                    "Compiler",
                    "Input/Output",
                    "Datapath",
                    "Operating System"
                ],
                "correct_index": 2,
                "explanation": "Bộ vi xử lý (Processor) bao gồm hai thành phần phần cứng nền tảng: Datapath (đường truyền dữ liệu gồm ALU, thanh ghi,...) và Control Unit (khối điều khiển). Compiler và OS là phần mềm, I/O là ngoại vi.",
                "category": "Tổng quan kiến trúc máy tính"
            },
            {
                "id": "d2_q6",
                "question_num": 6,
                "content": "Một bức ảnh có độ phân giải 4K kích thước 3840x2160 pixels. Mỗi pixel chứa 3 màu cơ bản Đỏ, Xanh lá, Xanh lam (RGB). Mỗi màu cơ bản được thể hiện bởi 8 bits. Để lưu trữ bức ảnh đó trên bộ nhớ thì dung lượng tối thiểu là bao nhiêu Mbytes?",
                "code": "",
                "options": [
                    "21",
                    "22",
                    "23",
                    "24"
                ],
                "correct_index": 3,
                "explanation": "Số pixel = 3840 * 2160 = 8.294.400 pixel. Mỗi pixel có 3 kênh màu * 8 bit = 24 bit = 3 byte. Tổng dung lượng = 8.294.400 * 3 = 24.883.200 Bytes. Tính theo MBytes chuẩn thương mại: 24.88 MB hoặc 24.883.200 / 1.048.576 ≈ 23.73 MiB làm tròn xấp xỉ 24 Mbytes.",
                "category": "Biểu diễn dữ liệu đa phương tiện"
            },
            {
                "id": "d2_q7",
                "question_num": 7,
                "content": "Câu lệnh hợp ngữ MIPS “lw $s3, 40($s2)” (Biết địa chỉ cơ sở của mảng A lưu trữ trong thanh ghi $s2) dùng để làm gì?",
                "code": "",
                "options": [
                    "Đọc dữ liệu từ ô nhớ A[40], lưu vào thanh ghi $s2.",
                    "Đọc dữ liệu từ ô nhớ A[160], lưu vào thanh ghi $s3.",
                    "Đọc dữ liệu từ ô nhớ A[10], lưu vào thanh ghi $s3.",
                    "Lưu dữ liệu từ thanh ghi $s3 sau khi cộng với 40 vào thanh ghi $s2."
                ],
                "correct_index": 2,
                "explanation": "Trong MIPS, mỗi phần tử mảng nguyên 32-bit (word) có kích thước 4 byte. Độ lệch offset 40 byte tương ứng với chỉ số index = 40 / 4 = 10. Do đó lệnh đọc dữ liệu từ ô nhớ phần tử A[10] và lưu vào thanh ghi đích $s3.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d2_q8",
                "question_num": 8,
                "content": "Cho một bộ xử lý với Clock rate = 2 GHz và CPI = 4. Hỏi tổng số lệnh thực thi trong một giây (instructions per second - IPS) là bao nhiêu?",
                "code": "",
                "options": [
                    "2 x 10^9",
                    "0.5 x 10^9",
                    "4 x 10^9",
                    "1 x 10^9"
                ],
                "correct_index": 1,
                "explanation": "Số lệnh trên mỗi giây (IPS) = Clock Rate / CPI = (2 * 10^9) / 4 = 0.5 * 10^9 (lệnh/giây).",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d2_q9",
                "question_num": 9,
                "content": "Máy tính có tần số xung clock là 4.0 GHz. Để thực thi một chương trình gồm 2024 lệnh thì máy tính thực hiện trong bao lâu? Biết trung bình mỗi lệnh kéo dài 2 chu kỳ.",
                "code": "",
                "options": [
                    "1012 ns",
                    "1012 ms",
                    "1012 s",
                    "1012 µs"
                ],
                "correct_index": 0,
                "explanation": "Tổng số chu kỳ clock = 2024 lệnh * 2 chu kỳ/lệnh = 4048 chu kỳ. Thời gian thực thi = Tổng chu kỳ / Tần số = 4048 / (4.0 * 10^9) = 1012 * 10^-9 giây = 1012 ns.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d2_q10",
                "question_num": 10,
                "content": "Cho bộ xử lý với Clock Rate = 3GHz. Giả sử bộ xử lý này thực thi một chương trình có 30 x 10^9 lệnh trong thời gian 4 giây. Tính số lệnh được thực thi trong một chu kỳ (instructions per cycle - IPC)?",
                "code": "",
                "options": [
                    "1",
                    "1.67",
                    "2",
                    "2.5"
                ],
                "correct_index": 3,
                "explanation": "Tổng số chu kỳ xung clock trong 4 giây = 4 s * (3 * 10^9 chu kỳ/s) = 12 * 10^9 chu kỳ. IPC = Số lệnh / Số chu kỳ = (30 * 10^9) / (12 * 10^9) = 2.5 lệnh/chu kỳ.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d2_q11",
                "question_num": 11,
                "content": "Giả sử lệnh toán học (Arith) cần 4 chu kỳ; đọc/ghi bộ nhớ (Store/Load) cần 5 chu kỳ; lệnh nhánh (Branch) cần 3 chu kỳ. Tìm thời gian thực thi của một chương trình chạy trên bộ xử lý 1 GHz với bảng số lệnh: Arith: 50, Store: 20, Load: 30, Branch: 50?",
                "code": "",
                "options": [
                    "350 ns",
                    "450 ns",
                    "600 ns",
                    "500 ns"
                ],
                "correct_index": 2,
                "explanation": "Tổng chu kỳ = (50 Arith * 4) + (20 Store * 5) + (30 Load * 5) + (50 Branch * 3) = 200 + 100 + 150 + 150 = 600 chu kỳ. Với bộ xử lý 1 GHz (1 chu kỳ = 1 ns), thời gian thực thi = 600 * 1 ns = 600 ns.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d2_q12",
                "question_num": 12,
                "content": "Trong các mã máy biểu diễn dưới dạng thập lục phân bên dưới. Câu lệnh nào dùng để biểu diễn lệnh “slt $t2, $t0, $t7”?",
                "code": "",
                "options": [
                    "0x010F502A",
                    "0x010E502A",
                    "0x010F402A",
                    "0x010E402A"
                ],
                "correct_index": 0,
                "explanation": "Lệnh slt rd, rs, rt có định dạng R: opcode=0 (6b), rs=$t0=8 (5b: 01000), rt=$t7=15 (5b: 01111), rd=$t2=10 (5b: 01010), shamt=0 (5b: 00000), funct=0x2A=42 (6b: 101010). Ghép nhị phân: 000000 01000 01111 01010 00000 101010 = 0000 0001 0000 1111 0101 0000 0010 1010 = 0x010F502A.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d2_q13",
                "question_num": 13,
                "content": "Cho đoạn chương trình sau. Sau khi thực thi xong thì giá trị trong thanh ghi $t1 là bao nhiêu?",
                "code": "addi $t0, $0, 8\naddi $t1, $0, 1\nloop:\nslt  $t2, $t1, $t0\nbeq  $t2, $zero, end\naddi $t1, $t1, 2\naddi $t0, $t0, 1\nj    loop\nend:\nadd  $t0, $t0, $t1",
                "options": [
                    "0x0F",
                    "0x1E",
                    "0x2F",
                    "0x2E"
                ],
                "correct_index": 0,
                "explanation": "Lặp khi $t1 < $t0: ban đầu t0=8, t1=1. Lần 1: t1=3, t0=9. Lần 2: t1=5, t0=10. Lần 3: t1=7, t0=11. Lần 4: t1=9, t0=12. Lần 5: t1=11, t0=13. Lần 6: t1=13, t0=14. Lần 7: t1=15, t0=15. Lúc này $t1 < $t0 là sai (15 < 15 false) => beq nhảy đến end. Giá trị thanh ghi $t1 khi kết thúc là 15 = 0x0F.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d2_q14",
                "question_num": 14,
                "content": "Hãy cho biết giá trị của thanh ghi $t1 sau khi chạy hết đoạn lệnh sau:",
                "code": "addi $t0, $0, 0x2024\nori  $t1, $t0, 0xCEEC\nand  $t2, $t0, $t1",
                "options": [
                    "0x00020224",
                    "0x000CEEC",
                    "0x0000EEEC",
                    "0x2024CEEC"
                ],
                "correct_index": 2,
                "explanation": "Lệnh addi nạp 0x2024 vào $t0. Lệnh ori $t1, $t0, 0xCEEC thực hiện phép OR giữa 0x00002024 và 0x0000CEEC. Ta có: 0x2 OR 0xC = 0010 OR 1100 = 1110 = 0xE; 0x0 OR 0xE = 0xE; 0x2 OR 0xE = 0xE; 0x4 OR 0xC = 0100 OR 1100 = 1100 = 0xC. Kết quả: 0x0000EEEC.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d2_q15",
                "question_num": 15,
                "content": "Câu lệnh bằng ngôn ngữ C: a = b - 27, với biến a, b lưu trữ trong thanh ghi tương ứng $s4, $s2. Câu lệnh assembly MIPS nào bên dưới tương đương với lệnh C này?",
                "code": "",
                "options": [
                    "addi $s4, $s2, -27",
                    "subi $s4, $s2, 27",
                    "sub $s2, $s4, 10",
                    "add $s4, $s2, -27"
                ],
                "correct_index": 0,
                "explanation": "Tập lệnh MIPS chuẩn không có lệnh 'subi'. Để trừ cho một hằng số tức thì, kiến trúc MIPS sử dụng lệnh addi cộng với số âm: addi $s4, $s2, -27.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d2_q16",
                "question_num": 16,
                "content": "Trong các mã máy biểu diễn dưới dạng thập lục phân bên dưới. Câu lệnh nào dùng để biểu diễn lệnh “andi $0, $s7, 123”?",
                "code": "",
                "options": [
                    "0x32E0005B",
                    "0x32E0007B",
                    "0x32F0005B",
                    "0x32F0007B"
                ],
                "correct_index": 1,
                "explanation": "andi là lệnh dạng I: opcode=12 (0x0C = 001100), rs=$s7=23 (10111), rt=$0=0 (00000), hằng số imm=123 (0x007B = 0000 0000 0111 1011). Ghép lại: 0011 0010 1110 0000 0000 0000 0111 1011 = 0x32E0007B.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d2_q17",
                "question_num": 17,
                "content": "Trong các câu lệnh assembly MIPS bên dưới. Câu lệnh nào dùng để biểu diễn lệnh mã máy 0x02D7A024?",
                "code": "",
                "options": [
                    "and $s4, $s6, $s7",
                    "addi $s4, $s5, $s7",
                    "or $s4, $s6, $s7",
                    "sub $s4, $s6, $s7"
                ],
                "correct_index": 0,
                "explanation": "0x02D7A024 sang nhị phân: 0000 0010 1101 0111 1010 0000 0010 0100. Tách các trường: opcode=000000 (R-type), rs=10110 (22 = $s6), rt=10111 (23 = $s7), rd=10100 (20 = $s4), shamt=00000, funct=100100 (0x24 = and). Cú pháp R-type: and rd, rs, rt => and $s4, $s6, $s7.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d2_q18",
                "question_num": 18,
                "content": "Cho đoạn chương trình Assembly sau: Sau khi chạy hết đoạn lệnh thì giá trị của thanh ghi $t1 là bao nhiêu?",
                "code": "addi $t0, $0, 0x10010008\naddi $t1, $0, 0x1001000C\nlw   $t1, 8($t0)\n\nBảng dữ liệu bộ nhớ:\nAddress      | Data\n0x10010008   | 0x00000004\n0x1001000C   | 0x00000005\n0x10010010   | 0x00000006\n0x10010014   | 0x00000007\n0x10010018   | 0x00000008",
                "options": [
                    "0x00000005",
                    "0x00000006",
                    "0x00000007",
                    "0x00000008"
                ],
                "correct_index": 1,
                "explanation": "Thanh ghi $t0 có giá trị 0x10010008. Lệnh lw $t1, 8($t0) tính địa chỉ truy xuất ô nhớ: $t0 + 8 = 0x10010008 + 8 = 0x10010010. Tra trong bảng dữ liệu bộ nhớ, tại địa chỉ 0x10010010 giá trị Data là 0x00000006. Do đó thanh ghi $t1 nhận giá trị 0x00000006.",
                "category": "Mô phỏng chương trình MIPS"
            }
        ]
    },
    {
        "id": 3,
        "title": "Đề số 3: Đề ôn thi Giữa kỳ Kiến trúc máy tính (Bộ đề 3)",
        "description": "Thao tác biến 32-bit trong bộ nhớ, chu trình nạp lệnh CPU, biểu diễn số âm bù 2, thứ tự Little-Endian, bus địa chỉ tối thiểu.",
        "duration_minutes": 35,
        "questions": [
            {
                "id": "d3_q1",
                "question_num": 1,
                "content": "Biến X thuộc kiểu word 32-bit nằm ở địa chỉ 0xAFB028C4. Đoạn chương trình nào sau đây tương đương với lệnh trong ngôn ngữ C: X = X + 1?",
                "code": "Lựa chọn 1:\naddi $t3, $0, 0xAFB028C4\nlw   $s3, 0($t3)\naddi $s3, $s3, 1\nsw   $s3, 0($t3)\n\nLựa chọn 2:\nlui  $t3, 0xAFB0\nori  $t3, $t3, 0x28C4\nlw   $s3, 0($t3)\naddi $s3, $s3, 1\nsw   $s3, 0($t3)",
                "options": [
                    "Lựa chọn 1",
                    "Lựa chọn 2",
                    "Dùng lw sau khi addi",
                    "Không thể thực hiện"
                ],
                "correct_index": 1,
                "explanation": "Địa chỉ 0xAFB028C4 là hằng số 32-bit. Lệnh addi chỉ chấp nhận hằng số 16-bit (mở rộng dấu). Do đó phải dùng cặp lệnh lui $t3, 0xAFB0 và ori $t3, $t3, 0x28C4 để nạp đủ 32-bit địa chỉ vào $t3, sau đó lw nạp giá trị, addi tăng 1, rồi sw ghi ngược lại ô nhớ.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d3_q2",
                "question_num": 2,
                "content": "Biến X, Y, Z nằm ở các thanh ghi $s1, $s2, $s3 tương ứng. Hỏi đoạn mã sau thực hiện phép toán nào?",
                "code": "add $t1, $s1, $s2\nsrl $s1, $s1, 2\nadd $s3, $t1, $s1",
                "options": [
                    "Z = X + Y",
                    "Z = X * Y",
                    "Z = X + Y + X/4",
                    "Z = X + Y + X"
                ],
                "correct_index": 2,
                "explanation": "Lệnh 1: $t1 = X + Y. Lệnh 2: dịch phải logic $s1 đi 2 bit tương đương phép chia nguyên cho 2^2 = 4 ($s1 = X / 4). Lệnh 3: $s3 = $t1 + $s1 = (X + Y) + X / 4.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d3_q3",
                "question_num": 3,
                "content": "Sử dụng 9 bit để biểu diễn một số nguyên không dấu, dải biểu diễn sẽ là bao nhiêu?",
                "code": "",
                "options": [
                    "0 tới 255",
                    "từ -256 tới +255",
                    "từ -255 tới +511",
                    "từ 0 tới 511"
                ],
                "correct_index": 3,
                "explanation": "Với n bit không dấu, dải giá trị từ 0 đến 2^n - 1. Với n = 9 bit: từ 0 đến 2^9 - 1 = 0 tới 511.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d3_q4",
                "question_num": 4,
                "content": "Trong chu trình hoạt động cơ bản của máy tính, có giai đoạn nạp lệnh (Fetch). Giai đoạn này CPU sẽ tác động tới 2 thanh ghi hệ thống nào?",
                "code": "",
                "options": [
                    "Thanh ghi lệnh IR & thanh ghi ngắt",
                    "Thanh ghi lệnh IR & thanh ghi bộ đếm chương trình PC",
                    "Thanh ghi bộ đếm chương trình PC & thanh ghi ngắt",
                    "Thanh ghi bộ đếm chương trình PC & Thanh ghi con trỏ lệnh IP"
                ],
                "correct_index": 1,
                "explanation": "Trong giai đoạn nạp lệnh (Instruction Fetch), CPU đọc lệnh từ bộ nhớ tại địa chỉ do thanh ghi PC (Program Counter) chỉ định, lưu lệnh vừa nạp vào thanh ghi IR (Instruction Register), đồng thời tăng PC để trỏ đến lệnh tiếp theo.",
                "category": "Chu trình thực thi lệnh của CPU"
            },
            {
                "id": "d3_q5",
                "question_num": 5,
                "content": "Đơn vị nào bên trong CPU chịu trách nhiệm lưu giữ các thông tin tạm thời phục vụ cho hoạt động của CPU?",
                "code": "",
                "options": [
                    "Cache",
                    "Bộ nhớ chính",
                    "Tập thanh ghi (Register File, RF)",
                    "Biến nhớ"
                ],
                "correct_index": 2,
                "explanation": "Tập thanh ghi (Register File) nằm ngay bên trong nhân CPU có tốc độ nhanh nhất, chuyên lưu trữ các toán hạng và kết quả tạm thời trong quá trình thực thi lệnh.",
                "category": "Cấu trúc CPU & Thanh ghi"
            },
            {
                "id": "d3_q6",
                "question_num": 6,
                "content": "Loại bộ nhớ nào không thuộc về bộ nhớ trong của máy tính?",
                "code": "",
                "options": [
                    "Bộ nhớ ROM",
                    "Bộ nhớ ổ cứng HDD",
                    "Bộ nhớ đệm (Cache)",
                    "Bộ nhớ chính (RAM)"
                ],
                "correct_index": 1,
                "explanation": "Bộ nhớ trong (Internal/Primary memory) gồm RAM, ROM và Cache. Ổ đĩa cứng HDD (hoặc SSD) thuộc về bộ nhớ ngoài (External/Secondary Storage).",
                "category": "Phân cấp bộ nhớ"
            },
            {
                "id": "d3_q7",
                "question_num": 7,
                "content": "Đoạn lệnh hợp ngữ MIPS sau đây truy xuất toán hạng ở bộ nhớ chính bao nhiêu lần?",
                "code": "lui  $t0, 0x2019\naddi $t0, $t0, 0x2104\nsll  $t1, $t0, 3\nsub  $t2, $t1, $t3",
                "options": [
                    "0",
                    "không xác định",
                    "1",
                    "2"
                ],
                "correct_index": 0,
                "explanation": "Đoạn lệnh trên chỉ sử dụng các lệnh tức thì và lệnh thanh ghi (lui, addi, sll, sub). Không có bất kỳ lệnh nào truy xuất bộ nhớ như lw, lb, sw, sb nên số lần truy xuất toán hạng ở bộ nhớ chính là 0.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d3_q8",
                "question_num": 8,
                "content": "Số nguyên -77 được biểu diễn dưới dạng số nhị phân 8 bit bù 2 là số nào?",
                "code": "",
                "options": [
                    "0100 1101",
                    "1011 0011",
                    "1011 1101",
                    "0111 0010"
                ],
                "correct_index": 1,
                "explanation": "+77 ở dạng 8 bit nhị phân là 0100 1101. Lấy bù 1 (đảo tất cả các bit): 1011 0010. Cộng thêm 1 để được dạng bù 2: 1011 0010 + 1 = 1011 0011.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d3_q9",
                "question_num": 9,
                "content": "Cho biết giá trị của thanh ghi $s1 sau khi thực hiện xong đoạn lệnh sau:",
                "code": "addi $t1, $0, -1\naddi $t2, $zero, 5\nor   $s1, $t1, $t2",
                "options": [
                    "5",
                    "0xFFFFFFFF",
                    "-5",
                    "1"
                ],
                "correct_index": 1,
                "explanation": "Lệnh addi $t1, $0, -1 nạp giá trị -1 vào thanh ghi 32-bit $t1, dạng nhị phân là toàn bộ 32 bit 1 (0xFFFFFFFF). Bất kỳ giá trị nào khi OR bit với toàn bit 1 (0xFFFFFFFF) đều cho kết quả là 0xFFFFFFFF.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d3_q10",
                "question_num": 10,
                "content": "Đối với bộ xử lý MIPS, địa chỉ nào sau đây không phải là địa chỉ hợp lệ của một lệnh máy?",
                "code": "",
                "options": [
                    "0x18d88",
                    "0x188A",
                    "0xFB019AC",
                    "0x18B124"
                ],
                "correct_index": 1,
                "explanation": "Trong kiến trúc MIPS, mỗi lệnh máy có độ dài 32 bit = 4 byte và bắt buộc phải được căn lề 4 byte (Alignment Restriction), tức địa chỉ phải chia hết cho 4 (kết thúc bằng 0, 4, 8, C). Địa chỉ 0x188A kết thúc bằng A (10) không chia hết cho 4 nên không hợp lệ.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d3_q11",
                "question_num": 11,
                "content": "Khi lấy thông tin ra khỏi ngăn xếp (Stack Pop), bộ xử lý sẽ thực hiện công việc nào sau đây?",
                "code": "",
                "options": [
                    "Giảm nội dung thanh ghi SP",
                    "Tăng nội dung thanh ghi SP",
                    "Giảm nội dung thanh ghi PC",
                    "Tăng địa chỉ thanh ghi PC"
                ],
                "correct_index": 1,
                "explanation": "Trong hầu hết các kiến trúc vi xử lý (kể cả MIPS), ngăn xếp tăng trưởng về phía địa chỉ thấp (khi đẩy push dữ liệu vào thì giảm SP). Do đó, khi lấy dữ liệu ra khỏi ngăn xếp (pop), nội dung thanh ghi con trỏ ngăn xếp SP phải được tăng lên.",
                "category": "Bộ nhớ & Ngăn xếp"
            },
            {
                "id": "d3_q12",
                "question_num": 12,
                "content": "Số 32-bit 0xC81A56 khi được lưu trữ vào bộ nhớ chính theo thứ tự đầu nhỏ (Little-Endian) thì trình tự các byte như thế nào? (Các phương án ghi theo địa chỉ tăng dần)",
                "code": "",
                "options": [
                    "56, 1A, C8",
                    "56, 1A, C8, 00",
                    "00, C8, 1A, 56",
                    "C8, 1A, 56"
                ],
                "correct_index": 1,
                "explanation": "Số 32-bit (4 byte) là 0x00C81A56. Các byte theo trọng số từ thấp đến cao: byte 0 là 56, byte 1 là 1A, byte 2 là C8, byte 3 là 00. Định dạng Little-Endian lưu byte trọng số thấp nhất ở địa chỉ thấp nhất, do đó theo chiều địa chỉ tăng dần các byte sẽ là: 56, 1A, C8, 00.",
                "category": "Địa chỉ bộ nhớ & Mảng"
            },
            {
                "id": "d3_q13",
                "question_num": 13,
                "content": "Ngăn nhớ (Memory Cell) nằm ở chỗ nào trong hệ thống máy tính?",
                "code": "",
                "options": [
                    "CPU",
                    "Thiết bị ngoại vi",
                    "Module vào ra",
                    "Bộ nhớ chính"
                ],
                "correct_index": 3,
                "explanation": "Ngăn nhớ (Memory Cell / Ô nhớ) là thành phần cấu tạo cơ bản của Bộ nhớ chính (RAM) dùng để lưu trữ các byte dữ liệu.",
                "category": "Cấu trúc CPU & Thanh ghi"
            },
            {
                "id": "d3_q14",
                "question_num": 14,
                "content": "Trong số các mã máy sau, mã máy nào thuộc kiểu lệnh J (Jump)?",
                "code": "",
                "options": [
                    "0x24120002",
                    "0x0810000D",
                    "0x02329820",
                    "0x06200002"
                ],
                "correct_index": 1,
                "explanation": "Lệnh nhảy dạng J (như j, jal) có opcode là 2 (000010) hoặc 3 (000011). Mã máy 0x0810000D có 8 bit đầu là 0x08 = 0000 1000(2), 6 bit đầu là 000010 = 2, chính là lệnh nhảy không điều kiện 'j' thuộc kiểu lệnh J.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d3_q15",
                "question_num": 15,
                "content": "Trong các phương pháp định địa chỉ toán hạng dưới đây, phương pháp nào có tốc độ thực thi lệnh chậm hơn?",
                "code": "",
                "options": [
                    "Định địa chỉ thanh ghi",
                    "Định địa chỉ tức thì",
                    "Định địa chỉ trực tiếp",
                    "Định địa chỉ thanh ghi và tức thì"
                ],
                "correct_index": 2,
                "explanation": "Định địa chỉ trực tiếp (Direct addressing) yêu cầu CPU phải phát địa chỉ ra Bus và truy cập vào bộ nhớ chính (RAM) để nạp toán hạng, chu kỳ truy xuất RAM mất nhiều thời gian hơn rất nhiều so với truy xuất thanh ghi hoặc giá trị tức thì có sẵn trong lệnh.",
                "category": "Phương pháp định địa chỉ"
            },
            {
                "id": "d3_q16",
                "question_num": 16,
                "content": "Một hệ thống máy tính cần sử dụng bộ nhớ lên tới 128 KiB, cổng vào ra 64 KiB, và ổ cứng SSD 256 KiB. Hỏi bus địa chỉ phải có độ rộng tối thiểu bằng bao nhiêu?",
                "code": "",
                "options": [
                    "17",
                    "18",
                    "19",
                    "20"
                ],
                "correct_index": 2,
                "explanation": "Tổng không gian địa chỉ CPU cần định tuyến trực tiếp cho bộ nhớ và thiết bị: 128 KiB + 64 KiB + 256 KiB = 448 KiB. Vì 2^18 = 256 KiB < 448 KiB <= 2^19 = 512 KiB, do đó bus địa chỉ cần độ rộng tối thiểu là 19 bit.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d3_q17",
                "question_num": 17,
                "content": "Cho 4 số nguyên 16 bit không dấu có mã hex tương ứng: 8792, 2763, F652, A876. Số nào là số lớn nhất?",
                "code": "",
                "options": [
                    "8792",
                    "A876",
                    "2763",
                    "F652"
                ],
                "correct_index": 3,
                "explanation": "Vì là số nguyên 16-bit không dấu (unsigned), ta so sánh trực tiếp độ lớn giá trị thập lục phân. Chữ số hex cao nhất: F > A > 8 > 2. Do đó 0xF652 (tương ứng 63058 ở hệ 10) là số có giá trị lớn nhất.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d3_q18",
                "question_num": 18,
                "content": "Trong quá trình giải mã lệnh (Instruction Decode), CPU sẽ tiến hành giải mã lệnh đang nằm trên thanh ghi nào?",
                "code": "",
                "options": [
                    "Thanh ghi lệnh IR",
                    "Thanh ghi con trỏ lệnh PC/IP",
                    "Thanh ghi dữ liệu",
                    "Thanh ghi trạng thái"
                ],
                "correct_index": 0,
                "explanation": "Lệnh máy sau khi nạp từ bộ nhớ về sẽ được lưu trong thanh ghi lệnh IR (Instruction Register). Khối giải mã điều khiển (Control Unit) sẽ giải mã trực tiếp nội dung các bit trong IR để phát các tín hiệu điều khiển.",
                "category": "Chu trình thực thi lệnh của CPU"
            },
            {
                "id": "d3_q19",
                "question_num": 19,
                "content": "Một đoạn phần mềm X có các nhóm lệnh A (CPI=1, số lệnh 4), nhóm B (CPI=2, số lệnh 1), nhóm C (CPI=3, số lệnh 1). Hãy cho biết chỉ số CPI trung bình của phần mềm X bằng bao nhiêu?",
                "code": "Nhóm lệnh | CPI | Số lệnh\nA         | 1   | 4\nB         | 2   | 1\nC         | 3   | 1",
                "options": [
                    "2.5",
                    "3",
                    "1.5",
                    "1"
                ],
                "correct_index": 2,
                "explanation": "Tổng số lệnh = 4 + 1 + 1 = 6 lệnh. Tổng số chu kỳ clock = (4 * 1) + (1 * 2) + (1 * 3) = 4 + 2 + 3 = 9 chu kỳ. CPI trung bình = Tổng chu kỳ / Tổng số lệnh = 9 / 6 = 1.5.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d3_q20",
                "question_num": 20,
                "content": "Sử dụng 6 bit nhị phân để biểu diễn số nguyên có dấu dạng bù 2. Hỏi giá trị lớn nhất có thể biểu diễn là bao nhiêu?",
                "code": "",
                "options": [
                    "15",
                    "31",
                    "16",
                    "32"
                ],
                "correct_index": 1,
                "explanation": "Với n bit có dấu dạng bù 2, dải giá trị biểu diễn được là từ -(2^(n-1)) đến +(2^(n-1) - 1). Với n = 6: giá trị nhỏ nhất là -(2^5) = -32, giá trị lớn nhất là +(2^5 - 1) = +31.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            }
        ]
    },
    {
        "id": 4,
        "title": "Đề số 4: Đề ôn thi Giữa kỳ Kiến trúc máy tính (Bộ đề 4)",
        "description": "Bus điều khiển, thời gian chạy asm, số dấu phẩy động 32-bit IEEE 754, so sánh hiệu năng CPU theo chu kỳ xung nhịp và ngắt hệ thống.",
        "duration_minutes": 35,
        "questions": [
            {
                "id": "d4_q1",
                "question_num": 1,
                "content": "Một CPU có bus dữ liệu và địa chỉ có độ rộng đều bằng 32 bit. Hỏi độ rộng của bus điều khiển bằng bao nhiêu?",
                "code": "",
                "options": [
                    "64",
                    "2 mũ 32",
                    "Không xác định",
                    "32"
                ],
                "correct_index": 2,
                "explanation": "Độ rộng của bus điều khiển phụ thuộc vào số lượng các đường tín hiệu điều khiển cụ thể được thiết kế cho hệ thống vi xử lý đó (Read, Write, Interrupt, Reset, Clock, Bus Grant,...). Nó không có công thức hay quan hệ cố định với độ rộng bus địa chỉ hay bus dữ liệu.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d4_q2",
                "question_num": 2,
                "content": "Một phần mềm viết bằng ngôn ngữ Asm với 30 lệnh, được biên dịch thành 40 lệnh máy. Biết rằng CPI trung bình là 2, và CPU có tốc độ xung nhịp 4 GHz. Hỏi thời gian thực hiện phần mềm là bao lâu?",
                "code": "",
                "options": [
                    "60 ns",
                    "80 ns",
                    "20 ns",
                    "15 ns"
                ],
                "correct_index": 2,
                "explanation": "Thời gian CPU = (Số lệnh máy * CPI) / Tần số xung nhịp = (40 * 2) / (4 * 10^9) = 80 / (4 * 10^9) = 20 * 10^-9 giây = 20 ns.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d4_q3",
                "question_num": 3,
                "content": "Sử dụng 9 bit để biểu diễn một số nguyên có dấu bù 2, dải biểu diễn sẽ là bao nhiêu?",
                "code": "",
                "options": [
                    "từ -255 tới 256",
                    "từ -127 tới 127",
                    "từ -256 tới +255",
                    "từ 0 tới 511"
                ],
                "correct_index": 2,
                "explanation": "Dải biểu diễn số nguyên có dấu bù 2 với n = 9 bit là [-(2^8), +(2^8 - 1)] = [-256, +255].",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d4_q4",
                "question_num": 4,
                "content": "Trong số các mã máy sau, mã máy nào không phải là lệnh ADDI?",
                "code": "",
                "options": [
                    "0x22728020",
                    "0x22518020",
                    "0x22338020",
                    "0x02338020"
                ],
                "correct_index": 3,
                "explanation": "Lệnh ADDI có opcode = 8 = 001000(2). 8 bit đầu tiên của mã máy ADDI luôn có dạng 0010 00xx tương ứng chữ số hex đầu tiên là 2 (0x2...). Mã máy 0x02338020 có 6 bit đầu là 000000, đây là lệnh thuộc định dạng R chứ không phải lệnh ADDI.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d4_q5",
                "question_num": 5,
                "content": "Số dấu phẩy động chuẩn IEEE 754 đơn 32-bit sau có giá trị bằng bao nhiêu?",
                "code": "1100 0000 1000 0000 0000 0000 0000 0000",
                "options": [
                    "-5",
                    "-4",
                    "-2",
                    "5"
                ],
                "correct_index": 1,
                "explanation": "Phân tích theo chuẩn IEEE 754 32-bit:\n- Bit dấu s = 1 (số âm).\n- 8 bit mũ E = 1000 0001(2) = 129(10) => Số mũ thực e = E - 127 = 129 - 127 = 2.\n- 23 bit định trị M = 000 0000 0000... => 1.M = 1.0.\nGiá trị = (-1)^1 * (1.0) * 2^2 = -1 * 1.0 * 4 = -4.",
                "category": "Biểu diễn số thực"
            },
            {
                "id": "d4_q6",
                "question_num": 6,
                "content": "Số âm -127(10) bằng với số nào trong các số sau đây? Biết rằng các số sau ở dạng biểu diễn nhị phân 8 bit bù 2.",
                "code": "",
                "options": [
                    "1000 0000(2)",
                    "1000 0001(2)",
                    "-0111 1111(2)",
                    "0111 1111(2)"
                ],
                "correct_index": 1,
                "explanation": "+127(10) ở dạng nhị phân 8 bit là 0111 1111. Để tìm số bù 2 của -127, đảo bit (bù 1) được 1000 0000, sau đó cộng 1 ta được 1000 0001(2).",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d4_q7",
                "question_num": 7,
                "content": "Số dương 1101011.1011 ở hệ cơ số 2 bằng với số nào trong các số thập phân sau đây?",
                "code": "",
                "options": [
                    "107.125(10)",
                    "107.129(10)",
                    "107.1875(10)",
                    "107.6875(10)"
                ],
                "correct_index": 3,
                "explanation": "- Phần nguyên: 1101011(2) = 64 + 32 + 8 + 2 + 1 = 107.\n- Phần thập phân: .1011(2) = 1*(2^-1) + 0*(2^-2) + 1*(2^-3) + 1*(2^-4) = 0.5 + 0.125 + 0.0625 = 0.6875.\nKết quả là 107.6875(10).",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d4_q8",
                "question_num": 8,
                "content": "Máy tính thực hiện phép toán cộng 2 số 8 bit không dấu ở hệ cơ số 2 sau đây: 1010 1000 + 1111 1010. Kết quả 8 bit lưu trong thanh ghi là bao nhiêu?",
                "code": "",
                "options": [
                    "1010 0010(2)",
                    "1000 0010(2)",
                    "1000 1110(2)",
                    "1000 0100(2)"
                ],
                "correct_index": 0,
                "explanation": "Cộng nhị phân:\n  1010 1000 (168)\n+ 1111 1010 (250)\n= 1 1010 0010 (418). Bỏ bit nhớ tràn ngoài 8 bit (carry out = 1), kết quả 8 bit còn lại là 1010 0010(2).",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d4_q9",
                "question_num": 9,
                "content": "Đối với bộ xử lý MIPS, địa chỉ nào sau đây không phải là địa chỉ hợp lệ của một lệnh máy?",
                "code": "",
                "options": [
                    "0x188A",
                    "0xFB019AC",
                    "0x18d88",
                    "0x198C124"
                ],
                "correct_index": 0,
                "explanation": "Mỗi lệnh MIPS phải nằm tại địa chỉ là bội số của 4 (2 bit thấp nhất là 00, ký tự hex cuối cùng là 0, 4, 8 hoặc C). Địa chỉ 0x188A kết thúc bằng A (10) không chia hết cho 4 nên không hợp lệ.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d4_q10",
                "question_num": 10,
                "content": "Loại bus nào vận chuyển nội dung lệnh máy từ bộ nhớ tới CPU?",
                "code": "",
                "options": [
                    "bus điều khiển",
                    "bus vào ra",
                    "bus dữ liệu",
                    "bus địa chỉ"
                ],
                "correct_index": 2,
                "explanation": "Bus dữ liệu (Data Bus) là kênh truyền nội dung các byte dữ liệu cũng như mã máy của các lệnh đọc từ bộ nhớ về CPU trong pha nạp lệnh.",
                "category": "Bus & Giao tiếp hệ thống"
            },
            {
                "id": "d4_q11",
                "question_num": 11,
                "content": "Một số 32 bit được lưu trữ trong bộ nhớ chính ở các ngăn nhớ liên tiếp: Địa chỉ 612 lưu byte 0E, địa chỉ 613 lưu 48, địa chỉ 614 lưu 21, địa chỉ 615 lưu 0A. Giá trị của số đó ở hệ 16 bằng bao nhiêu?",
                "code": "Địa chỉ | Giá trị byte (Hex)\n612     | 0E\n613     | 48\n614     | 21\n615     | 0A",
                "options": [
                    "E4821A nếu lưu trữ theo thứ tự đầu to",
                    "A4821E nếu lưu trữ theo thứ tự đầu to",
                    "0A4821E nếu lưu trữ theo thứ tự đầu nhỏ",
                    "0E48210A nếu lưu trữ theo thứ tự đầu to"
                ],
                "correct_index": 3,
                "explanation": "Theo quy ước đầu to (Big-Endian), byte có trọng số cao nhất (MSB) được lưu trữ ở địa chỉ nhỏ nhất. Ngăn nhớ 612 (nhỏ nhất) lưu 0E, tiếp theo là 48, 21, và 615 lưu 0A. Ghép từ địa chỉ nhỏ đến lớn ta được số: 0x0E48210A.",
                "category": "Địa chỉ bộ nhớ & Mảng"
            },
            {
                "id": "d4_q12",
                "question_num": 12,
                "content": "Máy tính A có chu kỳ xung nhịp hệ thống 300 ps và CPI = 2.0. Máy tính B có chu kỳ xung nhịp 500 ps và CPI = 1.1. Biết hai máy có cùng kiến trúc tập lệnh ISA. Vậy máy nào thực thi nhanh hơn?",
                "code": "",
                "options": [
                    "Không đủ thông tin",
                    "A nhanh hơn B",
                    "A nhanh bằng B",
                    "B nhanh hơn A"
                ],
                "correct_index": 3,
                "explanation": "Thời gian CPU trung bình cho mỗi lệnh = CPI * Chu kỳ xung nhịp.\n- Máy A: 2.0 * 300 ps = 600 ps/lệnh.\n- Máy B: 1.1 * 500 ps = 550 ps/lệnh.\nVì 550 ps < 600 ps nên máy B tốn ít thời gian hơn máy A trên mỗi lệnh, tức máy B thực thi nhanh hơn máy A.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d4_q13",
                "question_num": 13,
                "content": "Biến X, Y, Z nằm ở các thanh ghi $s1, $s2, $s3 tương ứng. Hỏi đoạn mã sau thực hiện phép toán nào?",
                "code": "addi $t1, $s1, 2\nsll  $s2, $s2, 2\nsub  $s3, $t1, $s2",
                "options": [
                    "Z = 2 - Y * 2",
                    "Z = X + 2 - Y * 4",
                    "Z = X * 2 + Y/2",
                    "Z = X - Y * 4"
                ],
                "correct_index": 1,
                "explanation": "Lệnh 1: $t1 = $s1 + 2 = X + 2. Lệnh 2: sll dịch trái 2 bit tương đương nhân với 2^2 = 4, tức $s2 = Y * 4. Lệnh 3: $s3 = $t1 - $s2 = (X + 2) - Y * 4. Do đó Z = X + 2 - Y * 4.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d4_q14",
                "question_num": 14,
                "content": "Đáp án nào mô tả đúng về cơ chế ngắt (Interrupt)?",
                "code": "",
                "options": [
                    "Tạm dừng chương trình đang thực hiện để chuyển đến thực hiện chương trình con khác",
                    "Kết thúc phần mềm",
                    "Tạm dừng phần mềm đang hoạt động",
                    "Kết thúc lệnh máy đang thực hiện dở"
                ],
                "correct_index": 0,
                "explanation": "Cơ chế ngắt (Interrupt) là cơ chế phần cứng/phần mềm cho phép CPU tạm dừng việc thực hiện chương trình hiện tại, lưu lại ngữ cảnh thực thi, để chuyển sang thực hiện một chương trình con phục vụ ngắt (ISR), sau đó quay trở lại tiếp tục chương trình cũ.",
                "category": "Ngắt & I/O"
            },
            {
                "id": "d4_q15",
                "question_num": 15,
                "content": "Vùng nhớ Stack nằm ở chỗ nào trong hệ thống máy tính?",
                "code": "",
                "options": [
                    "Ổ cứng",
                    "Thanh ghi",
                    "Bộ nhớ cache",
                    "Bộ nhớ RAM"
                ],
                "correct_index": 3,
                "explanation": "Ngăn xếp Stack là một vùng không gian địa chỉ được cấp phát bên trong bộ nhớ chính RAM của máy tính, được quản lý thông qua con trỏ ngăn xếp SP.",
                "category": "Bộ nhớ & Ngăn xếp"
            },
            {
                "id": "d4_q16",
                "question_num": 16,
                "content": "Cho 4 số nguyên 16 bit có dấu có mã hex tương ứng: 8792, 2763, F652, A876. Số nào là số lớn nhất?",
                "code": "",
                "options": [
                    "2763",
                    "A876",
                    "F652",
                    "8792"
                ],
                "correct_index": 0,
                "explanation": "Với số nguyên 16 bit có dấu: Bit dấu là bit cao nhất (bit 15). Chữ số hex đầu tiên: 8 (1000), A (1010), F (1111) đều có bit dấu bằng 1 nên là các số âm. Chữ số hex đầu là 2 (0010) có bit dấu bằng 0 nên là số dương duy nhất. Vậy 2763 là số lớn nhất.",
                "category": "Hệ thống số & Biểu diễn dữ liệu"
            },
            {
                "id": "d4_q17",
                "question_num": 17,
                "content": "Thanh ghi nào được tự động tăng mỗi khi CPU nhận xong một lệnh?",
                "code": "",
                "options": [
                    "Thanh ghi Stack Pointer",
                    "Thanh ghi Program Counter",
                    "Thanh ghi $s4",
                    "Thanh ghi Instruction Register"
                ],
                "correct_index": 1,
                "explanation": "Thanh ghi bộ đếm chương trình Program Counter (PC) luôn tự động cộng thêm 4 (trong MIPS 32-bit) sau khi nạp xong một lệnh để sẵn sàng trỏ đến lệnh kế tiếp.",
                "category": "Chu trình thực thi lệnh của CPU"
            },
            {
                "id": "d4_q18",
                "question_num": 18,
                "content": "Lệnh hợp ngữ MIPS nào sau đây sử dụng toán hạng dịch bit (shamt) thay vì thanh ghi nguồn thứ hai?",
                "code": "",
                "options": [
                    "mul $s4, $s4, $s4",
                    "add $s4, $s4, $s4",
                    "sll $s4, $s4, 1",
                    "sub $s4, $s4, $s4"
                ],
                "correct_index": 2,
                "explanation": "Lệnh sll (Shift Left Logical) là lệnh dịch bit sử dụng trường hằng số shamt (Shift Amount, 5 bit) để quy định số lượng bit cần dịch thay vì dùng thanh ghi rs.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d4_q19",
                "question_num": 19,
                "content": "Trong các phương pháp định địa chỉ toán hạng dưới đây, phương pháp nào có tốc độ thực thi lệnh chậm hơn?",
                "code": "",
                "options": [
                    "Định địa chỉ thanh ghi",
                    "Định địa chỉ trực tiếp",
                    "Định địa chỉ tức thì",
                    "Định địa chỉ thanh ghi và tức thì"
                ],
                "correct_index": 1,
                "explanation": "Định địa chỉ trực tiếp (Direct addressing) yêu cầu nạp toán hạng từ ô nhớ trong RAM, có độ trễ lớn hơn nhiều lần so với định địa chỉ thanh ghi hoặc tức thì.",
                "category": "Phương pháp định địa chỉ"
            },
            {
                "id": "d4_q20",
                "question_num": 20,
                "content": "Biến X thuộc kiểu word 32-bit nằm ở địa chỉ 0xAFB028C4. Đoạn chương trình nào tương đương với lệnh C: X = X + 1?",
                "code": "1. addi $t3, $0, 0xAFB028C4; lw $s3, 0($t3); addi $s3, $s3, 1; sw $s3, 0($t3)\n2. lui $t3, 0xAFB0; ori $t3, $t3, 0x28C4; lw $s3, 0($t3); addi $s3, $s3, 1; sw $s3, 0($t3)\n3. lui $t3, 0xAFB0; ori $t3, $t3, 0x28C4; lw $s3, 0($t3); addi $s3, $s3, 1; lw $s3, 0($t3)\n4. addi $t3, $0, 0xAFB028C4; lw $s3, 0($t3); addi $s3, $s3, 1; sw $s3, 0($t3)",
                "options": [
                    "Đoạn lệnh 1",
                    "Đoạn lệnh 2",
                    "Đoạn lệnh 3",
                    "Đoạn lệnh 4"
                ],
                "correct_index": 1,
                "explanation": "Để nạp địa chỉ 32 bit 0xAFB028C4, MIPS cần dùng lui 0xAFB0 để nạp 16 bit cao và ori 0x28C4 để nạp 16 bit thấp vào $t3. Sau đó đọc giá trị bằng lw, tăng 1 bằng addi và lưu lại bằng sw.",
                "category": "Kiến trúc tập lệnh MIPS"
            }
        ]
    },
    {
        "id": 5,
        "title": "Đề số 5: Đề ôn thi Giữa kỳ Kiến trúc máy tính (Bộ đề 5)",
        "description": "Các thành phần phần cứng máy tính, so sánh IPS giữa các CPU, tính toán dung lượng ảnh 2K, quy trình thủ tục MIPS, mã máy addi & srl.",
        "duration_minutes": 35,
        "questions": [
            {
                "id": "d5_q1",
                "question_num": 1,
                "content": "Các thành phần phần cứng cơ bản của máy tính gồm có những gì?",
                "code": "",
                "options": [
                    "Ngõ nhập, ngõ xuất, hệ điều hành và bộ vi xử lý",
                    "Ngõ nhập, ngõ xuất, bộ nhớ và hệ điều hành",
                    "Ngõ nhập, ngõ xuất, bộ nhớ và bộ vi xử lý",
                    "Ngõ nhập, ngõ xuất, bộ nhớ, bộ vi xử lý và hệ điều hành"
                ],
                "correct_index": 2,
                "explanation": "Theo kiến trúc Von Neumann, phần cứng máy tính gồm 4 khối chức năng cơ bản: Thiết bị nhập (Input), Thiết bị xuất (Output), Bộ nhớ (Memory) và Bộ vi xử lý (Processor). Hệ điều hành là phần mềm hệ thống chứ không phải thành phần phần cứng.",
                "category": "Tổng quan kiến trúc máy tính"
            },
            {
                "id": "d5_q2",
                "question_num": 2,
                "content": "Cho 3 bộ xử lý P1, P2 và P3 cùng chạy một tập lệnh: P1 (Clock 2 GHz, CPI 1.5), P2 (Clock 1.5 GHz, CPI 1.0), P3 (Clock 3 GHz, CPI 2.5). Bộ xử lý nào có hiệu suất cao nhất dựa theo tiêu chí số lệnh thực hiện trong 1 giây (IPS)?",
                "code": "Bộ xử lý | Clock rate | CPI\nP1       | 2.0 GHz    | 1.5\nP2       | 1.5 GHz    | 1.0\nP3       | 3.0 GHz    | 2.5",
                "options": [
                    "P3",
                    "P2",
                    "P1",
                    "Cả 3 bằng nhau"
                ],
                "correct_index": 1,
                "explanation": "Tính IPS = Clock Rate / CPI:\n- P1: 2.0 * 10^9 / 1.5 = 1.33 * 10^9 IPS\n- P2: 1.5 * 10^9 / 1.0 = 1.50 * 10^9 IPS\n- P3: 3.0 * 10^9 / 2.5 = 1.20 * 10^9 IPS\nVậy bộ xử lý P2 đạt hiệu suất cao nhất với 1.5 x 10^9 lệnh/giây.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d5_q3",
                "question_num": 3,
                "content": "Giả sử các bài hát file mp3 có dung lượng 5MB, hỏi một máy nghe nhạc có dung lượng 40GB thì có thể chứa tối đa bao nhiêu bài hát file mp3 như trên?",
                "code": "",
                "options": [
                    "9000",
                    "7192",
                    "7000",
                    "8192"
                ],
                "correct_index": 3,
                "explanation": "Đổi đơn vị nhị phân chuẩn hệ thống máy tính: 40 GB = 40 * 1024 MB = 40.960 MB. Số bài hát chứa được = 40.960 / 5 = 8.192 bài hát.",
                "category": "Biểu diễn dữ liệu & Dung lượng"
            },
            {
                "id": "d5_q4",
                "question_num": 4,
                "content": "Công cụ dùng để biên dịch từ ngôn ngữ Assembly sang mã máy gọi là gì?",
                "code": "",
                "options": [
                    "Compiler",
                    "System Program",
                    "Assembler",
                    "Operating System"
                ],
                "correct_index": 2,
                "explanation": "Assembler (Trình hợp dịch) là chương trình chuyển đổi mã nguồn viết bằng Hợp ngữ (Assembly) thành mã máy nhị phân (Machine code). Compiler dùng để biên dịch ngôn ngữ bậc cao (C, C++, Java,...).",
                "category": "Tổng quan kiến trúc máy tính"
            },
            {
                "id": "d5_q5",
                "question_num": 5,
                "content": "Trong các loại bộ nhớ sau, bộ nhớ nào có tốc độ truy xuất nhanh nhất?",
                "code": "",
                "options": [
                    "RAM",
                    "Cache",
                    "SSD",
                    "Hard disk"
                ],
                "correct_index": 1,
                "explanation": "Trong 4 loại bộ nhớ trên, Cache (bộ nhớ đệm cấu tạo từ SRAM tĩnh) có tốc độ nhanh hơn RAM (DRAM), và nhanh hơn vượt trội so với ổ đĩa SSD và HDD.",
                "category": "Phân cấp bộ nhớ"
            },
            {
                "id": "d5_q6",
                "question_num": 6,
                "content": "Một bức ảnh có độ phân giải 2K kích thước 2240x1920 pixels. Mỗi pixel chứa thông tin 3 màu cơ bản R, G, B, mỗi màu 8 bits. Để lưu trữ bức ảnh đó trên bộ nhớ thì dung lượng tối thiểu là bao nhiêu Mbytes?",
                "code": "",
                "options": [
                    "12.4",
                    "13.8",
                    "10.2",
                    "15"
                ],
                "correct_index": 0,
                "explanation": "Số pixel = 2240 * 1920 = 4.300.800 pixel. Mỗi pixel chiếm 3 byte (24 bit RGB). Tổng dung lượng = 4.300.800 * 3 = 12.902.400 Bytes. Tính theo MBytes nhị phân (MiB): 12.902.400 / (1024 * 1024) ≈ 12.3046 ≈ 12.4 Mbytes.",
                "category": "Biểu diễn dữ liệu đa phương tiện"
            },
            {
                "id": "d5_q7",
                "question_num": 7,
                "content": "Một chương trình máy tính chạy trong 14 giây trên máy tính A có tần số xung clock 1.8 GHz. Một nhà thiết kế mong muốn xây dựng máy tính B chạy chương trình này chỉ trong 9 giây, nhưng máy tính B yêu cầu số chu kỳ clock nhiều hơn máy A 1.5 lần. Hỏi tần số xung clock nhà thiết kế dùng cho máy B là bao nhiêu?",
                "code": "",
                "options": [
                    "2.2 GHz",
                    "3.5 GHz",
                    "3 GHz",
                    "4.2 GHz"
                ],
                "correct_index": 3,
                "explanation": "- Số chu kỳ clock máy A = Thời gian A * Tần số A = 14 * 1.8 * 10^9 = 25.2 * 10^9 chu kỳ.\n- Số chu kỳ clock máy B = 1.5 * 25.2 * 10^9 = 37.8 * 10^9 chu kỳ.\n- Tần số xung clock máy B = Chu kỳ B / Thời gian B = (37.8 * 10^9) / 9 = 4.2 * 10^9 Hz = 4.2 GHz.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d5_q8",
                "question_num": 8,
                "content": "Bước cuối cùng trong quá trình thực thi một thủ tục (Procedure / Function) trong kiến trúc máy tính là gì?",
                "code": "",
                "options": [
                    "Chuyển quyền điều khiển cho thủ tục",
                    "Yêu cầu tài nguyên lưu trữ cần thiết cho thủ tục",
                    "Trả điều khiển về vị trí mà thủ tục được gọi",
                    "Lưu kết quả một nơi mà chương trình có thể truy xuất được"
                ],
                "correct_index": 2,
                "explanation": "Sau khi tính toán và ghi kết quả trả về vào các thanh ghi giá trị ($v0, $v1), bước cuối cùng là trả quyền điều khiển về vị trí ngay sau lệnh gọi thủ tục bằng lệnh nhảy 'jr $ra'.",
                "category": "Quy trình thủ tục MIPS"
            },
            {
                "id": "d5_q9",
                "question_num": 9,
                "content": "Cho $s1 = 0x00002004; $s2 = 0x10010004; ô nhớ tại địa chỉ 0x10010008 có giá trị là 0x00002008. Sau khi thực hiện lệnh \"lw $s1, 4($s2)\", thì giá trị của thanh ghi $s2 là bao nhiêu?",
                "code": "",
                "options": [
                    "0x00002008",
                    "0x00002004",
                    "0x10010004",
                    "0x10010008"
                ],
                "correct_index": 2,
                "explanation": "Lệnh \"lw $s1, 4($s2)\" nạp dữ liệu từ ô nhớ có địa chỉ 4 + $s2 vào thanh ghi đích $s1. Lệnh này hoàn toàn KHÔNG làm thay đổi giá trị của thanh ghi cơ sở $s2. Do đó giá trị $s2 vẫn giữ nguyên là 0x10010004.",
                "category": "Kiến trúc tập lệnh MIPS"
            },
            {
                "id": "d5_q10",
                "question_num": 10,
                "content": "Bảng dưới đây mô tả số lệnh và CPI của 4 lớp lệnh A, B, C, D của một chương trình. Tính thời gian thực thi của chương trình biết máy tính có tần số 2.5 GHz?",
                "code": "Lớp lệnh | CPI | Số lệnh\nA        | 1   | 700\nB        | 5   | 180\nC        | 5   | 420\nD        | 2   | 60",
                "options": [
                    "544 ns",
                    "1528 ns",
                    "1504 ns",
                    "1910 ns"
                ],
                "correct_index": 1,
                "explanation": "Tổng số chu kỳ xung clock:\n= (700 * 1) + (180 * 5) + (420 * 5) + (60 * 2)\n= 700 + 900 + 2100 + 120 = 3820 chu kỳ.\nThời gian thực thi = Tổng chu kỳ / Tần số = 3820 / (2.5 * 10^9) = 1528 * 10^-9 giây = 1528 ns.",
                "category": "Hiệu suất máy tính"
            },
            {
                "id": "d5_q11",
                "question_num": 11,
                "content": "Trong các mã máy biểu diễn dưới dạng thập lục phân bên dưới. Câu lệnh nào dùng để biểu diễn lệnh \"srl $s5, $t8, 27\"?",
                "code": "",
                "options": [
                    "0x006A0034",
                    "0x00D482C2",
                    "0x0018D40C2",
                    "0x0018AEC2"
                ],
                "correct_index": 3,
                "explanation": "Lệnh srl rd, rt, shamt thuộc định dạng R: opcode=0 (6b), rs=0 (5b), rt=$t8=24 (5b: 11000), rd=$s5=21 (5b: 10101), shamt=27 (5b: 11011), funct=2 (6b: 000010). Ghép nhị phân: 000000 00000 11000 10101 11011 000010 = 0000 0000 0001 1000 1010 1110 1100 0010 = 0x0018AEC2.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d5_q12",
                "question_num": 12,
                "content": "Trong các mã máy biểu diễn dưới dạng thập lục phân bên dưới. Câu lệnh nào dùng để biểu diễn lệnh \"addi $t2, $s3, -58\"?",
                "code": "",
                "options": [
                    "0x212DFE20",
                    "0x2128FF05",
                    "0x226AFFC6",
                    "0x210DF820"
                ],
                "correct_index": 2,
                "explanation": "Lệnh addi rt, rs, imm thuộc định dạng I: opcode=8 (001000), rs=$s3=19 (10011), rt=$t2=10 (01010). Số âm -58 dạng bù 2 16-bit: +58 = 0x003A => -58 = 0xFFC6 (1111 1111 1100 0110). Ghép lại: 0010 0010 0110 1010 1111 1111 1100 0110 = 0x226AFFC6.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d5_q13",
                "question_num": 13,
                "content": "Trong các câu lệnh assembly MIPS bên dưới. Câu lệnh nào đúng để biểu diễn mã máy 0x00154825?",
                "code": "",
                "options": [
                    "or $t3, $t4, $s5",
                    "and $t3, $t4, $s5",
                    "or $t1, $zero, $s5",
                    "and $t3, $zero, $s5"
                ],
                "correct_index": 2,
                "explanation": "Mã máy 0x00154825 sang nhị phân: 0000 0000 0001 0101 0100 1000 0010 0101. Tách các trường: opcode=000000 (R-type), rs=00000 ($zero), rt=10101 ($s5 = 21), rd=01001 ($t1 = 9), shamt=00000, funct=100101 (0x25 = or). Cú pháp: or $t1, $zero, $s5.",
                "category": "Mã hóa lệnh MIPS"
            },
            {
                "id": "d5_q14",
                "question_num": 14,
                "content": "Chọn định nghĩa đúng cho thanh ghi Program Counter (PC)?",
                "code": "",
                "options": [
                    "Là thanh ghi chứa địa chỉ của lệnh kế tiếp được thực thi trong chương trình",
                    "Là thanh ghi chứa địa chỉ của lệnh đang được thực thi trong chương trình",
                    "Là thanh ghi chứa địa chỉ của đỉnh stack",
                    "Là thanh ghi chứa địa chỉ của dữ liệu đang được thực thi trong chương trình"
                ],
                "correct_index": 0,
                "explanation": "Thanh ghi con trỏ lệnh Program Counter (PC) là thanh ghi lưu trữ địa chỉ bộ nhớ của lệnh tiếp theo sẽ được CPU nạp và thực thi.",
                "category": "Cấu trúc CPU & Thanh ghi"
            },
            {
                "id": "d5_q15",
                "question_num": 15,
                "content": "Giả sử thanh ghi $s1 có giá trị 0x0049ACD3, thực hiện câu lệnh MIPS: \"srl $t0, $s1, 5\". Xác định giá trị trong thanh ghi $t0?",
                "code": "",
                "options": [
                    "0x00024D66",
                    "0x09359B61",
                    "0x09359A60",
                    "0x00024E66"
                ],
                "correct_index": 0,
                "explanation": "srl $t0, $s1, 5 là phép dịch phải logic 5 bit (thêm 5 bit 0 ở đầu). 0x0049ACD3 sang nhị phân: 0000 0000 0100 1001 1010 1100 1101 0011. Dịch phải 5 bit: 0000 0000 0000 0010 0100 1101 0110 0110 = 0x00024D66.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d5_q16",
                "question_num": 16,
                "content": "Cho đoạn chương trình sau. Sau khi thực thi xong thì giá trị trong thanh ghi $s1 là bao nhiêu?",
                "code": "addi $s0, $zero, 4\naddi $t1, $zero, 9\nloop:\nbeq  $t1, $zero, end\nsll  $s0, $s0, 1\naddi $t1, $t1, -3\nj    loop\nend:\naddi $s1, $s0, 5",
                "options": [
                    "33",
                    "37",
                    "35",
                    "25"
                ],
                "correct_index": 1,
                "explanation": "Ban đầu: $s0 = 4, $t1 = 9.\n- Lần 1: $t1 != 0, $s0 = 4 * 2 = 8, $t1 = 6\n- Lần 2: $t1 != 0, $s0 = 8 * 2 = 16, $t1 = 3\n- Lần 3: $t1 != 0, $s0 = 16 * 2 = 32, $t1 = 0\n- Lần 4: $t1 == 0 -> nhảy tới nhãn end.\nTại nhãn end: $s1 = $s0 + 5 = 32 + 5 = 37.",
                "category": "Mô phỏng chương trình MIPS"
            },
            {
                "id": "d5_q17",
                "question_num": 17,
                "content": "Giả sử thanh ghi $s0 và $s1 lưu giá trị biến g và h, địa chỉ nền của mảng A và B lưu trong thanh ghi $s6, $s7. Tìm dòng lệnh ngôn ngữ C tương ứng với chuỗi lệnh assembly sau:",
                "code": "lw  $t0, 16($s7)\nadd $t0, $t0, $s0\nsub $t0, $t0, $s1\nsw  $t0, 4($s6)",
                "options": [
                    "A[1] = g + B[4] - h",
                    "g = h - B[4] + A[1]",
                    "g = B[A[1]] - h + 4",
                    "B[4] = A[1] + g – h"
                ],
                "correct_index": 0,
                "explanation": "- lw $t0, 16($s7): nạp B[4] vào $t0 (vì 16 byte / 4 = index 4 của mảng B).\n- add $t0, $t0, $s0: $t0 = B[4] + g.\n- sub $t0, $t0, $s1: $t0 = B[4] + g - h.\n- sw $t0, 4($s6): lưu $t0 vào A[1] (vì 4 byte / 4 = index 1 của mảng A).\nVậy câu lệnh C tương đương là: A[1] = g + B[4] - h.",
                "category": "Kiến trúc tập lệnh MIPS"
            }
        ]
    }
]

# Write to questions.json
with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(exams, f, ensure_ascii=False, indent=2)

# Write to quiz_data.js for standalone browser usage
with open('quiz_data.js', 'w', encoding='utf-8') as f:
    f.write('const QUIZ_EXAMS = ' + json.dumps(exams, ensure_ascii=False, indent=2) + ';')

total_q = sum(len(e["questions"]) for e in exams)
print(f"Successfully generated database with {len(exams)} exams and {total_q} total questions!")
