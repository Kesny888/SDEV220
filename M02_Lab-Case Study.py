# Kesny Raingsey
# SDEV220
# 3/29/2024
# M02_Lab- Case Study.py
#Create a program that determines if the student qualifies for either the Dean's List or the Honor Roll. It allow the student enter lastname, firstname and GPA. If the student entered last name is 'ZZZ', the program will quit. If the student entered GPA 3.5 or greater, the student qualify for the Dean's list. And if the student entered GPA 3.2 or greater, the student qualiify for the Honor Roll.

#StudentLname = "ZZZ"

StudentLname = input("Enter the student's last name: ")
while (StudentLname != "ZZZ"):
    StudentFname = input("Enter the student's first name: ")
    StudentGPA = float(input("Enter the student's GPA: "))

    if (StudentGPA >= 3.5):
        print("the student has made the Dean's List")
    elif(StudentGPA >= 3.2):
        print("the student has made the Honor Roll.")




