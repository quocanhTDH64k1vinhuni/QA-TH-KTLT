print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Khởi tạo số dư tài khoản
balance = 0

# Nhập nhật ký giao dịch từ người dùng
while True:
    transaction = input('Nhập giao dịch (hoặc gõ "kết thúc" để dừng): ')
    
    # Kiểm tra điều kiện dừng
    if transaction.lower() == 'kết thúc':
        break
    
    # Tách loại giao dịch và số tiền
    parts = transaction.split()
    
    if len(parts) != 2:
        print('Vui lòng nhập định dạng hợp lệ (D <số tiền> hoặc W <số tiền>).')
        continue
    
    action = parts[0]
    
    try:
        amount = float(parts[1])
        
        if action.upper() == 'D':  # Tiền gửi
            balance += amount
        elif action.upper() == 'W':  # Tiền rút
            balance -= amount
        else:
            print('Hành động không hợp lệ. Vui lòng nhập D hoặc W.')
    except ValueError:
        print('Vui lòng nhập một số hợp lệ.')

# In ra số tiền thực của tài khoản
print('Số tiền thực của tài khoản là:', balance)

