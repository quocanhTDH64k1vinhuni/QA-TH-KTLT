print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # Khởi tạo mảng is_prime với các giá trị True (mặc định cho rằng tất cả là số nguyên tố)
    p = 2  # Bắt đầu với số 2 (số nguyên tố nhỏ nhất)
    while (p * p <= n):  # Lặp qua các số p từ 2 đến sqrt(n)
        if (is_prime[p] == True):  # Nếu p là số nguyên tố
            for i in range(p * p, n + 1, p):  # Đánh dấu các bội số của p
                is_prime[i] = False  # Các bội số của p không phải là số nguyên tố
        p += 1  # Tiến sang số tiếp theo
    return [p for p in range(2, n) if is_prime[p]]  # Trả về các số nguyên tố trong khoảng từ 2 đến n
primes = tuple(sieve_of_eratosthenes(1000))
print(primes)

