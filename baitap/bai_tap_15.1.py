def kiem_tra_email(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là địa chỉ email hợp lệ không, sử dụng try-except.

    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.

    Trả về:
        bool: True nếu chuỗi là một địa chỉ email hợp lệ, False nếu không.
    """
    try:
        # Kiểm tra nếu chuỗi không chứa '@'
        if '@' not in chuoi:
            raise ValueError("Địa chỉ email phải chứa ký tự '@'")
        
        # Tách phần trước và sau '@'
        phan_truoc, phan_sau = chuoi.split('@')

        # Kiểm tra phần trước không rỗng và chỉ chứa ký tự hợp lệ
        for ky_tu in phan_truoc:
            if not (ky_tu.isalnum() or ky_tu in '._'):
                raise ValueError("Phần trước '@' chứa ký tự không hợp lệ")

        # Kiểm tra phần sau không rỗng và chỉ chứa ký tự hợp lệ
        for ky_tu in phan_sau:
            if not (ky_tu.isalnum() or ky_tu in '.'):
                raise ValueError("Phần sau '@' chứa ký tự không hợp lệ")

        return True  # Chuỗi hợp lệ

    except ValueError:
        return False  # Chuỗi không hợp lệ

# Ví dụ sử dụng
print(kiem_tra_email("example@example.com"))  # Kết quả: True
print(kiem_tra_email("example@@example.com"))  # Kết quả: False
print(kiem_tra_email("example@ex@ample.com"))  # Kết quả: False
print(kiem_tra_email("example.com"))           # Kết quả: False
print(kiem_tra_email("example@example_com"))   # Kết quả: False
