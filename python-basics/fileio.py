#Name : Bob Afwata
# Date : 24/02/2026
# Program to perfom file operations

# create new file 
new_file = open("student_data.txt","r+")

# write to new file 
new_file.write("{ Student Name : Bob Afwata , ID : 29783789 , email:bob@gmail.com }")



# read from the file 
new_file = open("student_data.txt","r+")

data = new_file.read()

print(data)

new_file.close()

#delete file 
# us os module 
import os 
os.remove("remove.txt")


#delete folder
os.rmdir("folder")