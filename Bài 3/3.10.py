print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import math

def Tinh(R):
    if R <= 0:
        print("Bán kính phải là một số dương.")
        return
    
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
