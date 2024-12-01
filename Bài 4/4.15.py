print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập chuỗi từ bàn phím
s = input('Nhập các từ tiếng Anh (tách nhau bởi dấu cách): ')

# Tách chuỗi thành danh sách các từ
s1 = s.split()

# Sắp xếp các từ theo thứ tự từ điển
s2 = sorted(s1)

# In ra các từ đã sắp xếp
print('Các từ theo thứ tự từ điển:')
for word in s2:
    print(s2)
