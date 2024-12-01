print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Import module
import mymaxmin

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập giá trị các phần tử
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(value)

# Sắp xếp danh sách
sorted_lst = mymaxmin.sort_list(lst)

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = mymaxmin.find_max(lst)
min_value = mymaxmin.find_min(lst)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
