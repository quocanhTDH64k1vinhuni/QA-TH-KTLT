print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
def remove_invisible_chars(text):
 return ''.join(char for char in text if char not in (' ', '\t'))
s= input('Nhap chuoi:')
for ch in s:
 ch= remove_invisible_chars(s)
print(ch)
