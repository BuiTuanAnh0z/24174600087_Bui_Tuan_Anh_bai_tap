# Hiển thị menu lựa chọn thể loại phim
print("Chào mừng bạn đến với rạp chiếu phim ABC!")
print("Vui lòng chọn thể loại phim bạn muốn xem:")
print("1. Titanic")
print("2. The Walking Dead")
print("3. Tom and Jerry")
print("4. Avatar")

# Nhập lựa chọn của người dùng
lua_chon = input("Nhập số tương ứng với thể loại phim bạn muốn xem (1-4): ")

# Kiểm tra lựa chọn
if lua_chon == '1':
    print("Bạn đã chọn thể loại phim tình cảm.")
elif lua_chon == '2':
    print("Bạn đã chọn thể loại phim kinh dị.")
elif lua_chon == '3':
    print("Bạn đã chọn thể loại phim hoạt hình.")
elif lua_chon == '4':
    print("Bạn đã chọn thể loại phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")
