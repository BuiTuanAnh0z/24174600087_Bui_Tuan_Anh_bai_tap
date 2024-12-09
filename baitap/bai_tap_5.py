import math
def kiem_tra_so_chinh_phuong(so):
    """
    Hàm kiểm tra một số có phải số chính phương hay không.
    Tham số:
        so (int): Số cần kiểm tra.
    Trả về:
        bool: True nếu là số chính phương, False nếu không.
    """
    if so < 0:  # Số chính phương không thể là số âm
        return False

    # Tính căn bậc hai của số và kiểm tra xem nó có phải là số nguyên không
    can_bac_hai = math.isqrt(so)  # Sử dụng math.isqrt để tính căn bậc hai chính xác
    return can_bac_hai * can_bac_hai == so
# Ví dụ 
print(kiem_tra_so_chinh_phuong(16))
print(kiem_tra_so_chinh_phuong(25))
print(kiem_tra_so_chinh_phuong(10)) 
print(kiem_tra_so_chinh_phuong(1)) 
print(kiem_tra_so_chinh_phuong(0)) 
