import matplotlib.pyplot as plt

def calculate_result(marks_dic):
    total = sum(marks_dic.values())
    percentage = total/len(marks_dic)
    grade = None
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else: 
        grade = "F"
    
    return percentage , total , grade

def mark_analyzer():
    print("Welcome to student Marks analyzer !")
    students = {}
    subjects = ["Physics","Chemistry","Maths"]

    n = int(input("Enter the number of students : "))
    for i in range(n):
        name = input("\nEnter name of the student : ")
        students[name] = {}
        for subject in subjects:
            students[name][subject] = int(input(f"Enter the marks for {subject} : "))

    
    print("\nStudent Report : ")
    topper = None 
    highest_marks = 0
    total = 0
    for student, marks in students.items():
        percentage , total_marks , grade = calculate_result(marks)
        total += total_marks
        if total_marks>highest_marks:
            highest_marks = total_marks
            topper = student

        print(f"\n\nName : {student}")
        print("Marks : ",marks)
        print("Grade : ",grade)
        print("Percentage : ",round(percentage,2))
        print("Total marks :",total_marks)

    print("\nClass Report :")
    print(f"Class avg is {round(total/n,2)}")
    print(f"Class Topper is {topper} with highest marks of {highest_marks}")

    totals = []
    names = students.keys()
    for name in names:
        total = sum(students[name].values())
        totals.append(total)

    plt.bar(names, totals)
    plt.title("Students total marks comparison")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.show()



mark_analyzer()