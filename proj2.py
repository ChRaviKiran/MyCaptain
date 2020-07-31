import os
file = input("Enter file name : ")
split = os.path.splitext(file)
print('The extension of the file is :')
if(split[1] == '.txt'):
    print("'Text file'")
elif(split[1] == '.c'):
    print("'C'")
elif(split[1] == '.cpp'):
    print("'C++'")
elif(split[1] == '.java'):
    print("'Java'")
elif(split[1] == '.py'):
    print("'Python'")

