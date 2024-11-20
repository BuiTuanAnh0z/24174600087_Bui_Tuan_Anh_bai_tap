k = 10 
tong_i = 0 
for 1 in range(1,k+1):
    tong_i = tong_i + (tong_i + 1) 

n = int(input("Nhập gía trị nguyên dương")) 
tong_n = 0 
for k in range(1,n+1):
    tong_i = 0 
    for i in range(1,k+1):
        tong_i = tong_i + (i + 1)
    tong_n = tong_n + (tong_i/k)

print(f"ket qua: {tong_n}")
