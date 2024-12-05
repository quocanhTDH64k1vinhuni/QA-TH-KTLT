print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import tkinter as tk

# Hàm để tạo giao diện
def create_form():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Thông Tin Cá Nhân")

    # Tạo nhãn cho Họ Tên
    label_name = tk.Label(root, text="Họ tên:")
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    
    # Tạo ô nhập cho Họ Tên
    entry_name = tk.Entry(root, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    # Tạo nhãn cho Ngày tháng năm sinh
    label_dob = tk.Label(root, text="Ngày tháng năm sinh:")
    label_dob.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    
    # Tạo ô nhập cho Ngày tháng năm sinh
    entry_dob = tk.Entry(root, width=30)
    entry_dob.grid(row=1, column=1, padx=10, pady=5)

    # Tạo nhãn cho MSSV
    label_mssv = tk.Label(root, text="MSSV:")
    label_mssv.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    
    # Tạo ô nhập cho MSSV
    entry_mssv = tk.Entry(root, width=30)
    entry_mssv.grid(row=2, column=1, padx=10, pady=5)

    # Tạo nhãn cho Ngành học
    label_major = tk.Label(root, text="Ngành học:")
    label_major.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    
    # Tạo ô nhập cho Ngành học
    entry_major = tk.Entry(root, width=30)
    entry_major.grid(row=3, column=1, padx=10, pady=5)

    # Tạo nút để hiển thị thông tin
    def show_info():
        name = entry_name.get()
        dob = entry_dob.get()
        mssv = entry_mssv.get()
        major = entry_major.get()
        # Hiển thị thông tin khi nhấn nút
        info_label.config(text=f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")

    # Tạo nút "Hiển thị thông tin"
    btn_show = tk.Button(root, text="Hiển thị thông tin", command=show_info)
    btn_show.grid(row=4, column=0, columnspan=2, pady=10)

    # Nhãn để hiển thị thông tin sau khi nhấn nút
    info_label = tk.Label(root, text="", justify="left")
    info_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Chạy giao diện
    root.mainloop()

# Gọi hàm để tạo form
create_form()
