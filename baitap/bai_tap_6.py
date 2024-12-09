def kiem_tra_palindrome(chuoi):
    """
    Hàm kiểm tra chuỗi có phải là chuỗi palindrome hay không.
    Tham số:
        chuoi (str): Chuỗi cần kiểm tra.
    Trả về:
        bool: True nếu là chuỗi palindrome, False nếu không.
    """
    # Loại bỏ khoảng trắng và chuyển tất cả ký tự về chữ thường để kiểm tra
    chuoi = chuoi.replace(" ", "").lower()
    # So sánh chuỗi với chuỗi đảo ngược của nó
    return chuoi == chuoi[::-1]
# Ví dụ 
print(kiem_tra_palindrome("racecar"))     
print(kiem_tra_palindrome("level"))          
print(kiem_tra_palindrome("hello"))       
print(kiem_tra_palindrome("A man who is planning to conquer the whole continent of Europe")) 
