employee_file = open("employees3.txt", "w") #changed the letter to w

'''additionally, you can create an entire new file by j writing the name of the file
you want to create in open()'''

employee_file.write("Kelly - Customer Service") #this code will change the entire text file

employee_file.close()

#you could also create any file such as a html webpage. ex: index.html as the name.
#then, do write("<p>This is HTML</p>")