n = int(input("Nhap 50 so nguyen duong can kiem tra : "))
if n <= 1 :
    print("Khong la so nguyen to")
else :
    k=n 
for i in range(n):
    if n % k == 0 and k == n and k ==  1 :
       print ("khong la so nguyen to")
       break
    k = k - 1 
else :
    print("là so nguyen to") 