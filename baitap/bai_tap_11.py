def kiem_tra_in_hoa(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi chứa ít nhất một ký tự in hoa hay không.

    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.

    Trả về:
        bool: True nếu chuỗi chứa ít nhất một ký tự in hoa, False nếu không.
    """
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if 'A' <= ky_tu <= 'Z':  # Kiểm tra nếu ký tự là chữ in hoa
            return True
    return False  # Nếu không có ký tự in hoa nào
# Ví dụ 
print(kiem_tra_in_hoa("hello"))          
print(kiem_tra_in_hoa("Hello"))        
print(kiem_tra_in_hoa("heLLo"))         
print(kiem_tra_in_hoa("hello world"))  
print(kiem_tra_in_hoa(""))  
