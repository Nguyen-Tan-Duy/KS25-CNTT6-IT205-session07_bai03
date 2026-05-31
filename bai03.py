# hệ thống quản lý và chuẩn hóa dữ liệu nhân sự

# (1) Phân tích & Thiết kế giải pháp
#  Input
# Chuỗi thô raw_data chứa thông tin nhân sự, phân tách bằng | giữa các nhân viên, và ; giữa các trường.
# Dữ liệu có thể chứa:
# Khoảng trắng thừa
# ID viết hoa/thường lẫn lộn
# Họ tên chưa chuẩn hóa
# Số điện thoại có dấu - hoặc ký tự không hợp lệ
# Phòng ban viết thường
#  Output
# Menu console với 4 chức năng:
# In dữ liệu gốc
# Chuẩn hóa và in báo cáo dạng bảng
# Tìm kiếm nhân viên theo ID
# Thoát chương trình
#  Giải pháp
# Tách dữ liệu: dùng split("|") để lấy từng nhân viên, sau đó split(";") để lấy từng trường.
# Chuẩn hóa:
# ID: .strip().upper()
# Họ tên: .title() sau khi loại bỏ khoảng trắng thừa
# Phòng ban: .strip().upper()
# Số điện thoại:
# Xóa dấu - bằng .replace("-", "")
# Kiểm tra .isdigit()
# Nếu hợp lệ: che 6 số đầu bằng "******" + phone[6:]
# Nếu không hợp lệ: "Invalid Format"
# Tìm kiếm nhân viên:
# Chuẩn hóa input ID: .strip().upper()
# So sánh với danh sách ID đã chuẩn hóa
# Menu:
# Dùng vòng lặp while True
# Kiểm tra lựa chọn hợp lệ, nếu sai in thông báo và lặp lại
# Pseudocode
# Mã
# while True:
#     in menu
#     choice = input()
#     if choice == "1":
#         print raw_data
#     elif choice == "2":
#         parse raw_data
#         normalize fields
#         print table
#     elif choice == "3":
#         id = input()
#         normalize id
#         search in normalized data
#         print result or "Không tìm thấy"
#     elif choice == "4":
#         print "Thoát chương trình"
#         break
#     else:
#         print "Lựa chọn không hợp lệ"

# dữ liệu gốc:
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    choice = int(input('===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====\n' \
    '1. Hiển thị chuỗi dữ liệu gốc\n' \
    '2. Chuẩn hóa dữ liệu và in báo cáo \n' \
    '3. Tìm kiếm nhân viên theo mã ID\n' \
    '4. Thoát chương trình\n' \
    'Nhập chức năng:_'))

    match choice:
        case 1:
            print('----- Dữ liệu gốc -----\n', raw_data)
            print('-' * 50)
            print()

        case 2:
            records = raw_data.split("|")
            print(f"{'ID':<10}{'Name':<20}{'Phone':<15}{'Dept':<10}")
            print("-" * 55)
            for rec in records:
                fields = rec.split(";")
                if len(fields) != 4:
                    continue
                emp_id = fields[0].strip().upper()
                name = fields[1].strip().title()
                phone = fields[2].strip().replace("-", "")
                dept = fields[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[6:]
                else:
                    phone = "Invalid Format"

                print(f"{emp_id:<10}{name:<20}{phone:<15}{dept:<10}")
            print()

        case 3:
            search_id = input("Nhập mã nhân viên: ").strip().upper()
            found = False
            records = raw_data.split("|")
            for rec in records:
                fields = rec.split(";")
                if len(fields) != 4:
                    continue
                emp_id = fields[0].strip().upper()
                name = fields[1].strip().title()
                phone = fields[2].strip().replace("-", "")
                dept = fields[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[6:]
                else:
                    phone = "Invalid Format"

                if emp_id == search_id:
                    print("Thông tin nhân viên:")
                    print(f"ID: {emp_id}")
                    print(f"Họ tên: {name}")
                    print(f"SĐT: {phone}")
                    print(f"Phòng ban: {dept}")
                    found = True
                    break
            if not found:
                print("Không tìm thấy nhân viên")
            print()

        case 4:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
