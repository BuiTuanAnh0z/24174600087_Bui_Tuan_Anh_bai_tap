# Khởi tạo hai số đầu tiên trong dãy Fibonacci
a, b = 0, 1

# In ra 50 số đầu tiên trong dãy Fibonacci
print("50 số đầu tiên trong dãy Fibonacci là:")
for i in range(50):
    print(a, end=" ")
    # Cập nhật giá trị của a và b
    a, b = b, a + b
