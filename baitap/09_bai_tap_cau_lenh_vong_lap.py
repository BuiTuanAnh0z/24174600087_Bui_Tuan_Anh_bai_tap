# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# In các số lẻ nhỏ hơn n
print("Các số lẻ nhỏ hơn", n, "là:")
for i in range(n):
    if i % 2 == 1:
        print(i)

# Nhập vào số nguyên dương n cho dãy Fibonacci
n_fib = int(input("Nhập vào số nguyên dương n để in n số Fibonacci: "))

# In n số Fibonacci
print("Các số Fibonacci là:")
a = 0
b = 1
for i in range(n_fib):
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        print(a)
        tong_a_b = a + b
        a = b
        b = tong_a_b
