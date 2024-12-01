print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sắp xếp dữ liệu theo chiều cao tăng dần và lấy chỉ số sắp xếp
sorted_indices = np.lexsort((student_id, student_height))

# In ra chỉ số sắp xếp
print("Chỉ số:")
print(sorted_indices)

# In ra dữ liệu sắp xếp theo thứ tự đã sắp xếp
print("Dữ liệu sắp xếp:")
for idx in sorted_indices:
    print(f"{student_id[idx]} {student_height[idx]}")
