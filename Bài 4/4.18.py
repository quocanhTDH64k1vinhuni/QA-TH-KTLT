print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập số nguyên n từ bàn phím
n = int(input('Nhập số nguyên n: '))

# Khởi tạo danh sách các số Fibonacci
fibonacci_numbers = []

# Các số Fibonacci đầu tiên
a, b = 0, 1

# Tính toán và thêm các số Fibonacci nhỏ hơn n vào danh sách
while a < n:
    fibonacci_numbers.append(a)
    a, b = b, a + b

# In ra danh sách các số Fibonacci
print('Các số Fibonacci nhỏ hơn', n, ':', fibonacci_numbers)
