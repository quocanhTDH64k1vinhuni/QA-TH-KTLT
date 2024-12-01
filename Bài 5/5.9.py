print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def binary_search(list, value):
  """
  Hàm thực hiện tìm kiếm nhị phân.

  Args:
    list: Danh sách các phần tử đã được sắp xếp.
    value: Phần tử cần tìm.

  Returns:
    True nếu tìm thấy, False nếu không tìm thấy.
  """

  left = 0
  right = len(list) - 1
  while left <= right:
    mid = (left + right) // 2
    if list[mid] == value:
      return True
    elif list[mid] < value:
      left = mid + 1
    else:
      right = mid - 1
  return False  

# Nhập danh sách từ người dùng
n = int(input("Nhập số lượng phần tử: "))
data = []
for i in range(n):
  element = int(input(f"Nhập phần tử thứ {i+1}: "))
  data.append(element)

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Sắp xếp danh sách (nếu chưa được sắp xếp)
data.sort()

# Gọi hàm tìm kiếm và in kết quả
result = binary_search(data, value)

if result:
  print(f"Phần tử {value} đã được tìm thấy.")
else:
  print(f"Phần tử {value} không tìm thấy.")
