print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập danh sách các số từ bàn phím
input_numbers = input('Nhập các số : ')

# Tách chuỗi thành danh sách các số và chuyển đổi thành số nguyên
numbers = [int(num.strip()) for num in input_numbers.split()]

# Lọc các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# In ra các số lẻ
print('Các số lẻ:',','.join(map(str, odd_numbers)))
