print("SINH VIEN : DINH XUAN ANH")
print("MSV : 235752021610055")
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Nghiệm của phương trình là: x = {x}")
else:
 
    delta = b**2 - 4*a*c
    
    if delta > 0:
   
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
     
        x = -b / (2*a)
        print(f"Có nghiệm kép: x = {x}")
    else:
      
        print("Phương trình vô nghiệm thực.")
