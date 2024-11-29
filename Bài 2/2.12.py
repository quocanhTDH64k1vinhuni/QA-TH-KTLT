print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
import re
# Initialize the list to store valid passwords
value = []
# Get the list of passwords from user input
items = [x for x in input("Nhập mật khẩu: ").split(',')]
# Loop through each password to validate it
for p in items:
    # Check if the password length is between 6 and 12 characters
    if len(p) < 6 or len(p) > 12:
        continue
    # Check for at least one lowercase letter
    if not re.search("[a-z]", p):
        continue
    # Check for at least one digit
    elif not re.search("[0-9]", p):
        continue
    # Check for at least one uppercase letter
    elif not re.search("[A-Z]", p):
        continue
    # Check for at least one special character ($, #, or @)
    elif not re.search("[$#@]", p):
        continue
    # Check if the password contains any spaces
    elif re.search("\s", p):
        continue
    # If all conditions are met, add the password to the list
    value.append(p)
# Print out the valid passwords, separated by commas
print(",".join(value))
