print("Nguyễn Quốc Anh")
print("MSV 235752021610084")

class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Create instances of Nam and Nu
aNam = Nam()
aNu = Nu()

# Print gender information for each
print(aNam.getGender())  # Output: Nam
print(aNu.getGender())   # Output: Nữ
