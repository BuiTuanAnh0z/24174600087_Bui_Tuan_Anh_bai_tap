print("Hello world")

a = "Hello world"
b = 'Hello world' 

c = 'Bạn A nói: "Abcd"'
d = "bạn A nói: 'Abcd'"

#Kiểu dữ liệu tuân tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó 
#Truy cập sử dụng index (danh mục) 

print (a[4])

#[start:stop:step]
#start: vị trí bắt đầu 
#stop: vị trí kết thúc 
#step: khoảng cách giữa các bước 
print (a[1:7]) #Lấy các giá trị từ start đến stop-1 
print (a[:7])
print (a[1:])
print (a[:])

#mặc định của step luôn bằng 1 
print (a[1:7:2])
print (a[:7:2]) 
print (a[::2])
print (a[1::2])
print (a[::])
print (a[::-1])

#range(range(5)) #0,1,2,3,4
#range cũng sử dụng start, stop, step 
#range(1,5)
#range(1,5,2)

for item in a:
    print(item)

#hàm đo độ dài kiểu dữ liệu tuần tự : len 
print(len(a))
range(len(a)) #thu được chỉ mục chạy từ 0 đến len(a)-1 = 10 

for i in range(len(a)) :
    print(a[i])

#tính chất của kiểu dữ liệu chuỗi ký tự :
#- có thể truy cập 
#- không thể chỉnh sửa 
#- không thể sắp xếp 

#b = "Hello" + "world" 
#print(b)

#n = int(input ("Nhập vào số nguyên dương: "))
#if n > 0 :
    #print("Da nhap dung so nguyen duong")
#c = "" 
#for i in range (len(a)):
   # if a [1] == "a":
   #     c = c + i 

#for i in a: 
  #  print(i)

#các phương thức trong xử lý trong chuỗi ký tự 
a = "Helloworld123." 
#các phương thức kiểm tra ( trả về cho mình True hoặc False )
#các phương thức này sẽ thằng bắt đầu bằng chữ "is" 

# - kiểm tra chuỗi có phải aLphanumeric(chỉ có kí tự số và chữ hay không)
print(a.isalnum())