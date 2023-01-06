# https://samy01.netlify.app
# This is a python project done by Samuel Yahaya, 
# Mr Lasisi; and 
# some other students of the Peakfield Academy Geek Club

print('Hello, this is a grading system by SamY in co-operation with Mr Lasisi and some PFA students')
print("It uses the 100% scoring system")

name = input("Enter your name: ") # This asks for input of user name

numsub = int(input("Enter number of subjects: ")) 
# This asks for input of number of subjects that will be inputed
# This will be a counter for the number of times the loop will run

def details():
    print("---------------------------------------")
    subname = input("Enter name of subject: ")

def val():
    ca1 = int(input("Enter your First CAT: "))

    while ca1 > 20:
        print("First CAT can't be more than 20")
        ca1 = int(input("Enter your First CAT: "))

    while ca1 < 0:
        print("First CAT can't be less than 0")
        ca1 = int(input("Enter your First CAT: "))

    ca2 = int(input("Enter your Second CAT: "))

    while ca2 > 20:
        print("Second CAT can't be more than 20")
        ca2 = int(input("Enter your Second CAT: "))

    while ca2 < 0:
        print("Second CAT can't be less than 0")
        ca2 = int(input("Enter your Second CAT: "))

    exam = int(input("Enter your Exam score: "))

    while exam > 60:
        print("Exam score can't be more than 60")
        exam = int(input("Enter your Exam Score: "))

    while exam < 0:
        print("Exam score can't be less than 0")
        exam = int(input("Enter your Exam score: "))

    subscore = ca1+ca2+exam
    while subscore > 100:
        print("This score is invalid")

    if subscore == 100:
        print(name + ", Congratulations! This is an outstanding performance. " + "Your total is", subscore)
    elif subscore >= 80:
        print(name + ", You got an A. " + "Your total is", subscore)
    elif subscore >= 70:
        print(name + ", You got a B. " + "Your total is", subscore)
    elif subscore >= 60:
        print(name + ", You got a C. " + "Your total is", subscore)
    elif subscore >= 50:
        print(name + ", You got a D. " + "Your total is", subscore)
    elif subscore >= 40:
        print(name + ", You got a P. " + "Your total is", subscore)
    else:
        print(name + ", You have failed. " + "Your total is", subscore)


for x in range(numsub):
    details()
    val()
    x = x - 1
# This for loop runs through the details function, the val function 
# When it is done, it minuses one from x

print("-------------------------------------------")
print("Thanks for trying it out. ")
print("Done by Samuel Yahaya, Mr Lasisi, and some students in PFA Geek Club")
print("Check out SamY's Website (https://samy01.netlify.app). Thanks")
