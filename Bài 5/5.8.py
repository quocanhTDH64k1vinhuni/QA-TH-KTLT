print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def sequential_search(data, item):
  """
  Hàm thực hiện tìm kiếm tuyến tính.

  Args:
    data: Danh sách các phần tử.
    item: Phần tử cần tìm.

  Returns:
    Vị trí của phần tử nếu tìm thấy, ngược lại trả về -1.
  """

  for i in range(len(data)):
    if data[i] == item:
      return i
  return -1

# Nhập danh sách từ người dùng
n = int(input("Nhập số lượng phần tử: "))
data = []
for i in range(n):
  element = int(input(f"Nhập phần tử thứ {i+1}: "))
  data.append(element)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm và in kết quả
result = sequential_search(data, item)

if result != -1:
  print(f"Phần tử {item} được tìm thấy tại vị trí {result}")
else:
  print(f"Phần tử {item} không tìm thấy trong danh sách")
