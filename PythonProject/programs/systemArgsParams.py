import sys
print(sys.argv)

if len(sys.argv) ==2:
    print("Enter all the values")
    sys.exit()

full_name = "".join(sys.argv[1:])
print(full_name)

full_name = " ".join(sys.argv[1:])
print(full_name)

email =full_name.replace(" ",".")+"@capg.com"
print(email)