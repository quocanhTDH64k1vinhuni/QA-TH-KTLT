print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def benefit(t, n, k):
    # Chuyển đổi lãi suất từ phần trăm sang số thập phân
    lãi_suất = t / 100
    # Tính số tiền sau k tháng
    so_tien_nhan_duoc = n * ((1 + lãi_suất) ** k)
    return so_tien_nhan_duoc

# Nhập dữ liệu từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm (t%/tháng): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))
    
    # Tính và in kết quả
    ket_qua = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng: {ket_qua:.2f}")
except ValueError:
    print("Vui lòng nhập các giá trị hợp lệ.")
