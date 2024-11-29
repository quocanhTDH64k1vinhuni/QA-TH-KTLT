print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
#Viết chương trình in ra màn hình dãy số Fibonacci nhỏ hơn 4.000.000, tìm tổng các số chẵn trong dãy đã in
a,b=1,2
total=0
print(a,end="")
while (a<=4000000-1):
    if a%2==0:
        total +=a
    a,b=b,a+b
    print(a,end="")
print("\n sum of prime numbers term in fibonacci series:",total)
