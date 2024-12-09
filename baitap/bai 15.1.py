#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
# 5. Thoát chương trình
while True :
    print ("MENU:")
    print ("1. xem danh sách sinh viên")
    print ("2. Nhập thông tin sinh viên mới vào danh sách")
    print ("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print ("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print ("5. Thoát chương trình")
    lua_chon = input("Nhap lua chon ban muon su dung: ")
    if lua_chon.isdigit() == False :
        print("Yeu cau nhap lai")
    else:
        if lua_chon == 1 :
            print("chay 1") 
        elif lua_chon == 2 :
            print("chay 2") 
        elif lua_chon == 3 : 
            print("chay_3")
        elif lua_chon == 4 :
            print("chay 4") 
        elif lua_chon == 5 :
            print("thoat chuong trinh ")
        break
else :
    print("Yeu cau nhap lai")