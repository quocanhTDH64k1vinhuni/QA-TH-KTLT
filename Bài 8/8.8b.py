print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import tkinter as tk
from tkinter import messagebox

# Hàm để tạo giao diện
def create_form():
    # Cửa sổ chính
    root = tk.Tk()
    root.title("Thông Tin Cá Nhân và Radio Button")

    # --- Phần 1: Thông tin cá nhân ---
    # Nhãn và ô nhập cho Họ tên
    label_name = tk.Label(root, text="Họ tên:")
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_name = tk.Entry(root, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Nhãn và ô nhập cho Ngày tháng năm sinh
    label_dob = tk.Label(root, text="Ngày tháng năm sinh:")
    label_dob.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_dob = tk.Entry(root, width=30)
    entry_dob.grid(row=1, column=1, padx=10, pady=5)

    # Nhãn và ô nhập cho MSSV
    label_mssv = tk.Label(root, text="MSSV:")
    label_mssv.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_mssv = tk.Entry(root, width=30)
    entry_mssv.grid(row=2, column=1, padx=10, pady=5)

    # Nhãn và ô nhập cho Ngành học
    label_major = tk.Label(root, text="Ngành học:")
    label_major.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_major = tk.Entry(root, width=30)
    entry_major.grid(row=3, column=1, padx=10, pady=5)

    # Hàm để hiển thị thông tin cá nhân
    def show_info():
        name = entry_name.get()
        dob = entry_dob.get()
        mssv = entry_mssv.get()
        major = entry_major.get()
        info_label.config(text=f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")

    # Nút "Hiển thị thông tin"
    btn_show = tk.Button(root, text="Hiển thị thông tin", command=show_info)
    btn_show.grid(row=4, column=0, columnspan=2, pady=10)

    # Nhãn hiển thị thông tin
    info_label = tk.Label(root, text="", justify="left")
    info_label.grid(row=5, column=0, columnspan=2, pady=10)

    # --- Phần 2: Radio Button ---
    label_radio = tk.Label(root, text="Chọn một số:")
    label_radio.grid(row=6, column=0, padx=10, pady=10)

    # Biến để lưu lựa chọn radio button
    selected_number = tk.IntVar()

    # Các radio button
    radio_1 = tk.Radiobutton(root, text="First", variable=selected_number, value=1)
    radio_1.grid(row=7, column=0, padx=10, pady=5)
    radio_2 = tk.Radiobutton(root, text="Second", variable=selected_number, value=2)
    radio_2.grid(row=8, column=0, padx=10, pady=5)
    radio_3 = tk.Radiobutton(root, text="Third", variable=selected_number, value=3)
    radio_3.grid(row=9, column=0, padx=10, pady=5)

    # Hàm để hiển thị lựa chọn radio button
    def show_radio_choice():
        choice = selected_number.get()
        messagebox.showinfo("Lựa chọn", f"Bạn đã chọn: Số {choice}")

    # Nút "Click Me"
    btn_radio = tk.Button(root, text="Click Me", command=show_radio_choice)
    btn_radio.grid(row=10, column=0, columnspan=2, pady=10)

    # Chạy giao diện
    root.mainloop()

# Gọi hàm để tạo form
create_form()
