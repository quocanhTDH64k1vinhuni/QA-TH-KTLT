print("Nguyễn Quốc Anh")
print("MSV 235752021610084")

import turtle, random

# Danh sách các màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Khởi tạo đối tượng turtle
painter = turtle.Turtle()
painter.pensize(3)

# Vẽ các vòng tròn với màu sắc ngẫu nhiên
for i in range(10):
    color = random.choice(colors)  # Chọn màu ngẫu nhiên từ danh sách colors
    painter.pencolor(color)  # Đặt màu cho bút vẽ
    painter.circle(100)  # Vẽ một vòng tròn có bán kính 100
    painter.right(30)  # Quay bút vẽ sang phải 30 độ
    painter.left(60)  # Quay bút vẽ sang trái 60 độ
    painter.setposition(0, 0)  # Đưa bút vẽ về vị trí (0, 0) sau mỗi vòng tròn


