print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))

def find_even_digit_numbers(start, end):
    even_digit_numbers = [str(num)
                          for num in range(start, end + 1) if all_even_digits(num)]
    return ','.join(even_digit_numbers)

# Tìm các số trong đoạn 1000 đến 3000
result = find_even_digit_numbers(1000, 3000)
print(result)
