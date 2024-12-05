
print("Nguyễn Quốc Anh")
print("MSV 235752021610084")

# Import thư viện turtle
import turtle

# Cài đặt cửa sổ
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tạo đối tượng turtle để vẽ
painter = turtle.Turtle()
painter.fillcolor("blue")
painter.pencolor('blue')
painter.pensize(3)

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

# Vẽ các hình vuông xoay theo góc nhỏ
for i in range(1,180):  
    painter.left(18)  # Quay turtle một góc 18 độ sau mỗi lần vẽ
    drawsq(painter, 200)  # Vẽ hình vuông với cạnh dài 200
   

