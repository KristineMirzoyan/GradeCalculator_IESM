
import json

#ToDos
#   1.Limit the grades

#   2.Order the list
#   3.Grade should be a number
#   4.

def loadSetupData():

    with open('gc_setup.json') as data_file:
        course = json.load(data_file)
    setup = course["course_setup"]
    return setup


def loadStudentGrades():
    with open("gc_grades.json") as data_file:
        points=json.load(data_file)
    return points


def askForAssignmentMarks(grades, points, student_id):
    #current_grades = {student_id: {}}

    for key in grades:
        try:
            if points[student_id][key] >= -1:
                print "Your Grade from " + key + " is " + str(points[student_id][key])
                #points[student_id][key] = points[student_id][key]
                answer=raw_input("Do you want to update your score y/n")
                if answer=="y":
                    points[student_id][key]=input("your new score")
                    if points>=100 or (points<=0 and points!=-1):
                        points = input ("please insert grade between 0 and 100")
            #else:
                #points[student_id][key] = input(
                #"What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
        except:
            points[student_id][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

    return points

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades, student_id):
    curr_grade = 0
    for key in current_grades[student_id]:
        if current_grades[student_id][key] != -1:
            calc_grade = float(current_grades[student_id][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade
    print (curr_grade)
    return curr_grade

def printLetterGrade(curr_grade,conv_matrix):
    for i in range(len(conv_matrix)):
        if curr_grade>conv_matrix[i]["min"] and curr_grade<=conv_matrix[i]["max"]:
            letter_grade=conv_matrix[i]["mark"]
    print letter_grade
    return letter_grade

def main():
    setup = loadSetupData()
    grades = setup["grade_breakdown"]
    conv_matrix = setup["conv_matrix"]
    student_id = raw_input("please tell me your ID")
    points = loadStudentGrades()
    current_grades = askForAssignmentMarks(grades, points, student_id)
    saveGrades(current_grades)
    curr_grade = printCurrentGrade(grades, current_grades,student_id)
    printLetterGrade(curr_grade,conv_matrix)

main()



# def  main():
#    student_id=raw_input("please tell me your ID")
#    students_grades=loadstudentgrades()
#    current_grades=90
#    students_grades[student_id ]=current_grades
#    savegrades(students _ grades)


