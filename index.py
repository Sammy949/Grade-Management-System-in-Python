import os

print('Hello, this is a grading system by SamY in co-operation with Mr Lasisi and some PFA students')
print("It uses the 100% scoring system")

name = input("Enter your name: ")
numsub = int(input("Enter number of subjects: "))

data_dir = os.path.join(os.getcwd(), name)
os.makedirs(data_dir, exist_ok=True)

def details():
    print("---------------------------------------")
    subname = input("Enter name of subject: ")
    return subname

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

    grade = ""
    if subscore == 100:
        grade = "Outstanding"
    elif subscore >= 80:
        grade = "A"
    elif subscore >= 70:
        grade = "B"
    elif subscore >= 60:
        grade = "C"
    elif subscore >= 50:
        grade = "D"
    elif subscore >= 40:
        grade = "P"
    else:
        grade = "F"

    return {"ca1": ca1, "ca2": ca2, "exam": exam, "subscore": subscore, "grade": grade}


data = []

for x in range(numsub):
    subname = details()
    subdata = val()
    subdata["subject"] = subname
    data.append(subdata)
    print(f"{name}, your {subname} grade is {subdata['grade']} with a total score of {subdata['subscore']}")

with open(os.path.join(data_dir, "data.txt"), "w") as f:
    for subdata in data:
        f.write(f"Subject: {subdata['subject']}\n")
        f.write(f"First CAT: {subdata['ca1']}\n")
        f.write(f"Second CAT: {subdata['ca2']}\n")
        f.write(f"Exam score: {subdata['exam']}\n")
        f.write(f"Total score: {subdata['subscore']}\n")
        f.write(f"Grade: {subdata['grade']}\n")
        f.write("------------------------------\n")

print("-------------------------------------------")
print("Thanks for trying it out. ")
print("Done by Samuel Yahaya, Mr Lasisi, and some students in PFA Geek Club")
