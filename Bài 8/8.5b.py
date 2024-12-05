print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import tkinter as tk
root = tk.Tk()#khởi tạo cửa sổ giao diện 
v = tk.IntVar()
v.set(1) # khởi tạo giá trị lựa chọn là 1, tương ứng với "Python"
languages = [
 ("Python",1),
 ("Perl",2),
 ("Java",3),
 ("C++",4),
 ("C",5)
]# danh sách ngôn ngữ lập trình
def ShowChoice():
 print(v.get())
tk.Radiobutton(root,
 text=languages,
indicatoron = 0,
width = 20,
padx = 20,
variable=v,
command=ShowChoice,
value=eval).pack(anchor=tk.W)
for val, language in enumerate(languages):#Tạo các nút radio (RadioButtons)
 tk.Radiobutton(root,
 text=language,
padx = 20,
variable=v,
command=ShowChoice,
value=val).pack(anchor=tk.W)
root.mainloop()
