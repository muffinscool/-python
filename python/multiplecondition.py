eng_marks = int(input("Enter marks in english: "))
maths_marks = int(input("Enter marks in maths: "))

#if both are more than 80, print A grade 
if eng_marks > 80 and maths_marks > 80: 
    print("A grade")

#if either of marks are more than 80, print B grade
elif eng_marks > 80 or maths_marks >80:
    print("B grade")

#if neither of marks are more than 80 
else:
    print("C grade")
    