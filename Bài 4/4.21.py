print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def check_divisible_by_5(binary_strings):
    divisible_by_5 = []
    
    for binary in binary_strings.split(','):
        # Chuyển đổi chuỗi nhị phân thành số nguyên
        decimal = int(binary, 2)
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    
    return ','.join(divisible_by_5)

# Nhập vào chuỗi các số nhị phân 4 chữ số
input_string = input("Nhập các số nhị phân 4 chữ số (phân tách bởi dấu phẩy): ")
result = check_divisible_by_5(input_string)

if result:
    print("Các số nhị phân chia hết cho 5:", result)
else:
    print("Không có số nhị phân nào chia hết cho 5.")
