def kiem_tra_in_thuong(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa ít nhất một ký tự in thường hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu chuỗi chứa ít nhất một ký tự in thường, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if 'a' <= ky_tu <= 'z':  # Kiểm tra nếu ký tự là chữ in thường
            return True
    return False  # Nếu không có ký tự in thường nào
# Ví dụ
print(kiem_tra_in_thuong("HELLO"))     
print(kiem_tra_in_thuong("Hello"))      
print(kiem_tra_in_thuong("HELLO World"))
print(kiem_tra_in_thuong("12345"))      
print(kiem_tra_in_thuong(""))           