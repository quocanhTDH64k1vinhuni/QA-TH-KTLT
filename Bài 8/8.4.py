print("Nguyễn Quốc Anh")
print("MSV 235752021610084")

from tkinter import *

# Tạo cửa sổ chính
windown = Tk()
windown.title('Welcome to LikeGeeks app')
windown.geometry('350x200')

# Tạo nhãn (Label) và đặt vị trí bằng phương thức grid
lbl = Label(windown, text='Hello')
lbl.grid(column=0, row=0)  

# Hàm khi nhấn nút
def clicked():
    lbl.configure(text='Button was clicked !!')

# Tạo nút (Button) và gán hành động khi nhấn nút
# Tạo nút (Button) và gán hành động khi nhấn nút
btn = Button(windown, text='Click Me', command=clicked, bg='blue', fg='white')
# Đặt màu nền và màu chữ
btn.grid(column=1, row=0)


# Giữ cửa sổ mở
windown.mainloop()
