def kiem_tra_so_nguyen_duong(chuoi):
    """
    Hàm kiểm tra chuỗi có phải số nguyên dương hay không.

    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.

    Trả về:
        bool: True nếu chuỗi là số nguyên dương, False nếu không.
    """
    if not chuoi:  # Kiểm tra chuỗi rỗng
        return False
    # Duyệt qua từng ký tự trong chuỗi để kiểm tra có phải toàn chữ số không
    for ky_tu in chuoi:
        if not ('0' <= ky_tu <= '9'):
            return False
    # Sau khi đảm bảo tất cả ký tự là số, kiểm tra giá trị lớn hơn 0
    return int(chuoi) > 0
# Ví dụ
print(kiem_tra_so_nguyen_duong("123"))   
print(kiem_tra_so_nguyen_duong("0"))     
print(kiem_tra_so_nguyen_duong("-456")) 
print(kiem_tra_so_nguyen_duong("abc"))  
print(kiem_tra_so_nguyen_duong(""))   
