print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập tên người
full_name = input('Nhập họ và tên: ')

# Tách họ và tên riêng
parts = full_name.split()

# Giả định rằng họ là phần đầu tiên và tên là phần cuối
if len(parts) >= 2:
    last_name = parts[0]  # Họ
    first_name = parts[-1]  # Tên 
else:
    last_name = full_name
    first_name = ""

# In ra họ và tên 
print('Họ:', last_name)
print('Tên:', first_name)
