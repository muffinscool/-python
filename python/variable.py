#string 
name = "Isha"
#print (type(name))

#integer
roll_number = 17
# print (type(roll_number))

# floating number 
percentage = 92.7
#print (type(percentage))

# boolean 
is_student = True 
#print (type(is_student))

print(name, roll_number,percentage, is_student)
# we are using addition first and then comma because they are not of same data types, firstly its string and then integer. 

print("My name is "+ name + " and My roll number is ", roll_number )
print("I scored", percentage, "% in my final exams. I am a student is", is_student)

#print(name,roll_number, percentage, is_student)

#print expressions 
print(" My percentage has chanaged to", percentage -2.0)

#prit with separator 
print(name, roll_number, percentage, is_student, sep="-")

x=1
y=2
z=3 
print(x,y,z,sep="->")