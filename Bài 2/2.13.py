print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import cmath  # Sử dụng cmath để xử lý cả nghiệm thực và nghiệm phức

# Nhập hệ số a, b, c
a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))

# Kiểm tra nếu a = 0 thì không phải phương trình bậc 2
if a == 0:
    print("Đây không phải là phương trình bậc 2.")
else:
    # Tính delta
    delta = b*b - 4*a*c

    # Tính nghiệm
    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print(f"Nghiệm thực phân biệt: x1 = {x1.real}, x2 = {x2.real}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Nghiệm kép: x = {x}")
    else:
        # Nghiệm phức
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print(f"Nghiệm phức: x1 = {x1}, x2 = {x2}")
