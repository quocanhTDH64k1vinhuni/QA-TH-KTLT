print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def print_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(' '.join(map(str, row)))

# Nhập n từ người dùng
n = int(input("Nhập số dòng của tam giác Pascal: "))
print_pascals_triangle(n)
