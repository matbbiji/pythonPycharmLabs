
employee_file = open("employees2.txt", "a") #appending info into the file

#employee_file.write("Toby - Human Resources") #we're appending info into the file
employee_file.write("\nKelly - Customer Service") #make sure to \n in order to insert on a new line

employee_file.close()
#notice that nothing gets printed. its changing within the file

'''
appending you need to really careful bc if you 
actually go under file again or you append something on something wrong to the file.
it's permanently going to get saved inside the file.

be careful everytime you run a program!
'''