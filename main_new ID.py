import json


def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]
    return grades

def loadStudentGrades():
    with open('gc_grades.json') as data_file:
        user_grades=json.load(data_file)

    return user_grades

def studentInput(user_grades):
    student_ID = raw_input("Please insert your ID")
    while True:
        if student_ID in user_grades:
            return student_ID
        student_ID=raw_input("Your inputted ID did not match any in the database. Please enter another one: ")



def askForAssignmentMarks(grades, user_grades, student_ID):
    current_grades = {student_ID: {}}

    for key in grades:
        print(key)
        change=input("Would you like to change the grade? Type 0 for no and 1 for yes")

        if change!=0 and change!=1:
            change=input("Please put in either 0 for no or 1 for yes.")
        if change==0:
            if ((user_grades[student_ID][key]>=0) and (user_grades[student_ID][key]<=100)) or (user_grades[student_ID][key]==-1):
                current_grades[student_ID][key] = user_grades[student_ID][key]
            else:
                change=1
        if change==1:
            update= input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
            while True:
                if ((update>=0) and (update<=100)) or (update==-1):
                    current_grades[student_ID][key]= update
                    break
                else:
                    update=input("Please enter a number between 0 and 100. Please insert -1 if you don't have a grade yet")
    return current_grades

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades, student_ID):
    curr_grade = 0.0
    for key in current_grades[student_ID]:
        if current_grades[student_ID][key] != -1:
            calc_grade = float(current_grades[student_ID][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print (curr_grade)
    return curr_grade

def printLetterGrade(curr_grade, matrix):
    for i in range(len(matrix)):
        if curr_grade>= matrix[i]["min"] and curr_grade<=matrix[i]["max"]:
            print matrix[i]["mark"]

def main():
    g = loadSetupData()
    grades= g["grade_breakdown"]
    students_grades = loadStudentGrades()
    student_ID = studentInput(students_grades)
    current_student_grades = {student_ID: students_grades[student_ID]}
    current_grades = askForAssignmentMarks(grades, current_student_grades, student_ID)
    students_grades[student_ID] = current_grades[student_ID]
    saveGrades(students_grades)
    curr_grade= printCurrentGrade(grades, current_grades, student_ID)
    conv_matrix= g["conv_matrix"]
    printLetterGrade(curr_grade, conv_matrix)

main()
