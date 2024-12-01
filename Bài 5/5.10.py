print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
# Hàm sắp xếp nổi bọt (Bubble Sort)
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n):
        # Cờ để kiểm tra xem có hoán đổi hay không
        swapped = False
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                # Hoán đổi nếu phần tử trước lớn hơn phần tử sau
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không có hoán đổi, kết thúc sớm
        if not swapped:
            break
    return nlist

# Chương trình nhập dữ liệu và sắp xếp
def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập danh sách các phần tử
    nlist = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i+1}: "))
        nlist.append(value)
    
    # Sử dụng bubbleSort để sắp xếp danh sách
    sorted_list = bubbleSort(nlist)
    
    # In ra danh sách sau khi sắp xếp
    print("Danh sách sau khi sắp xếp:")
    print(sorted_list)

# Gọi hàm main để thực thi
if __name__ == "__main__":
    main()
