def kiem_tra_so_nguyen(chuoi):
    """
    Hàm kiểm tra chuỗi có phải số nguyên hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi là số nguyên, False nếu không.
    """
    if not chuoi:  # Kiểm tra chuỗi rỗng
        return False
    # Nếu ký tự đầu tiên là '-', kiểm tra các ký tự còn lại
    if chuoi[0] == '-':
        for ky_tu in chuoi[1:]:
            if not ('0' <= ky_tu <= '9'):
                return False
        return True
    else:
        # Kiểm tra tất cả ký tự trong chuỗi là số
        for ky_tu in chuoi:
            if not ('0' <= ky_tu <= '9'):
                return False
        return True
# Ví dụ 
print(kiem_tra_so_nguyen("123"))   
print(kiem_tra_so_nguyen("-456"))  
print(kiem_tra_so_nguyen("12.3"))  
print(kiem_tra_so_nguyen("abc"))  
print(kiem_tra_so_nguyen(""))     
