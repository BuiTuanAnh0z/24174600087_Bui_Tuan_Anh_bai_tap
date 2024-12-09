def kiem_tra_so_nguyen_to(so):
    """
    Hàm kiểm tra một số có phải số nguyên tố hay không.
    Tham số:
        so (int): Số cần kiểm tra.
    Trả về:
        bool: True nếu là số nguyên tố, False nếu không.
    """
    if so < 2:  # Số nguyên tố phải lớn hơn hoặc bằng 2
        return False
    # Duyệt qua tất cả các số từ 2 đến căn bậc hai của số (tối ưu hóa)
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:  # Nếu chia hết cho bất kỳ số nào, không phải số nguyên tố
            return False
    return True  # Nếu không chia hết cho số nào, là số nguyên tố
# Ví dụ
print(kiem_tra_so_nguyen_to(2))   
print(kiem_tra_so_nguyen_to(17))   
print(kiem_tra_so_nguyen_to(15))  
print(kiem_tra_so_nguyen_to(1))    
print(kiem_tra_so_nguyen_to(0))   
print(kiem_tra_so_nguyen_to(-5))  
