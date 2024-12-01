print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Nhập dãy các từ từ bàn phím
words = input('Nhập dãy các từ :').split()

# Tìm độ dài lớn nhất
max_length = max(len(word) for word in words)

# Tìm tất cả các từ có độ dài bằng độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]

# In ra các từ dài nhất
print('Các từ dài nhất (độ dài:', max_length, '):')
for word in longest_words:
    print(word)
