#Câu lệnh vòng lặp while
#n = 10 
#while n > 2 :#True
#     print(f"chay vòng lap {n}") 
#Vòng lặp while cùng hỗ trợ : break, continue và else 
n = 10 
#break
#while n > 2 : #True 
   # print(f"Chay vong lap {n}")
   # n = n - 1
   # if n == 0:
    #    break
#continue 
#n = 10 
#while n > 2 : #True 
  #  print(f"Chay vong lap {n}")
   # n = n - 1
  #  if n == 6:
       # continue 
  #  print(f"Chay vong lap {n}")
#else:
   # print("chay cau lenh else")

#n=10
#while n > 2 : #True 
  #  print(f"Chay vong lap {n}")
   # n = n - 1
   #if n == 0 
  #      continue 
#n = 10 
#while n > 2 : #True 
  #  print(f"Chay vong lap {n}")
  #  n = n - 1
  #  if n == 6:
  #      continue 
  #  print(f"Chay vong lap {n}")
#else:
   # print("chay cau lenh else")

#TÌm số nguyên tố lớn nhất nhỏ hơn hoặc bằng 20 
n = 20  
while True:
    for i in range(1,n): 
        if n%i==0 and i!=1 and i!=n:
            n = n - 1
            break 
    else:
        break 

    if n < 1: 
        break 
print(f"so nguyen to la {n}")
