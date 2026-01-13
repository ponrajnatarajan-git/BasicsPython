import sys
print(sys.argv)


full_name = sys.argv[1]
# last_name = sys.argv[2]

if len(sys.argv)==2:
    print("Usage: python email_generator.py 'Enter both firstname and lastname'")
    sys.exit()


#format the name
email =full_name.replace(" ",".")+"@capg.com"


#generate the output
print("---Your Profile----")
print("Full Name is :",full_name)
print("Email Generated is :",email)