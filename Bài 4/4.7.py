print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập chuỗi từ bàn phím
s = input('Nhập chuỗi: ')

# Loại bỏ các chữ số
s1 = ''.join(char for char in s if not char.isdigit())

# In ra chuỗi mới
print('Chuỗi sau khi loại bỏ chữ số:', s1)
