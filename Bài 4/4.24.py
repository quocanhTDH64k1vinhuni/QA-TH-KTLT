print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập câu từ bàn phím
s = input('Nhập một câu: ')

# Khởi tạo biến đếm
upper_count = 0# chữ hoa 
lower_count = 0 #chữ thường

# Duyệt qua từng ký tự trong câu
for char in s:
    if char.isupper():  # Kiểm tra chữ hoa
        upper_count += 1
    elif char.islower():  # Kiểm tra chữ thường
        lower_count += 1

# In ra kết quả
print('Chữ hoa:', upper_count)
print('Chữ thường:', lower_count)
