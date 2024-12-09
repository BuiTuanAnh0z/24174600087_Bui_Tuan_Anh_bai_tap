def kiem_tra_so_thuc(chuoi):
    """
    Hàm kiểm tra chuỗi có phải số thực hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi là số thực, False nếu không.
    """
    if not chuoi:  # Kiểm tra chuỗi rỗng
        return False
    co_dau_cham = False  # Biến đánh dấu sự xuất hiện của dấu '.'
    # Nếu chuỗi bắt đầu bằng dấu âm, bỏ qua ký tự đầu tiên
    if chuoi[0] == '-':
        chuoi = chuoi[1:]
    # Duyệt từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if ky_tu == '.':  # Gặp dấu chấm thập phân
            if co_dau_cham:  # Nếu đã gặp dấu '.' trước đó, không phải số thực
                return False
            co_dau_cham = True
        elif not ('0' <= ky_tu <= '9'):  # Ký tự không phải số và không phải '.'
            return False
    # Đảm bảo chuỗi không chỉ là dấu '.' hoặc rỗng
    return co_dau_cham and len(chuoi) > 1
# Ví dụ
print(kiem_tra_so_thuc("123.45"))   
print(kiem_tra_so_thuc("-0.56"))  
print(kiem_tra_so_thuc("789"))      
print(kiem_tra_so_thuc("12.3.4")) 
print(kiem_tra_so_thuc("abc"))    
print(kiem_tra_so_thuc(""))      
