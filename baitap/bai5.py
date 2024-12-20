# Nhập một ký tự 
ky_tu = input("Nhập một ký tự: ")

# Kiểm tra xem ký tự có phải là chữ cái trong bảng chữ cái tiếng Anh không
if ky_tu.isalpha() and len(ky_tu) == 1:
    # Chuyển ký tự thành chữ thường để dễ so sánh
    ky_tu = ky_tu.lower()
    
    # Kiểm tra nguyên âm
    if ky_tu in ['u', 'e', 'o', 'a', 'i']:
        print("Ký tự là nguyên âm.")
    else:
        print("Ký tự là phụ âm.")
else:
    print("Đây không phải là một ký tự hợp lệ trong bảng chữ cái.")
