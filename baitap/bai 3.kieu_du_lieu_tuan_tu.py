# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))
# Khởi tạo danh sách A (số lẻ) và B (số chẵn)
A = []
B = []
# Duyệt qua các số nhỏ hơn n để phân loại số lẻ và số chẵn
i = 1
while i < n:
    if i % 2 == 0:
        B.append(i)
    else:
        A.append(i)
    i += 1
# Sắp xếp dãy A theo thứ tự giảm dần
i = 0
while i < len(A):
    j = i + 1
    while j < len(A):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
        j += 1
    i += 1
# Sắp xếp dãy B theo thứ tự giảm dần
i = 0
while i < len(B):
    j = i + 1
    while j < len(B):
        if B[i] < B[j]:
            B[i], B[j] = B[j], B[i]
        j += 1
    i += 1
# In ra các danh sách A và B
print(f"Danh sách A (số lẻ):", A)
print(f"Danh sách B (số chẵn):", B)

