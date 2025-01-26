import os
path = input("enter the path:")
os.chdir(path)

user_input = input("enter the file to read:")
a = user_input + ".txt"
if os.path.exists(a):
    f = open(a,)
    c = f.read()
    print(c)
    f.close()
else:
    print("file no exist")
    
    


