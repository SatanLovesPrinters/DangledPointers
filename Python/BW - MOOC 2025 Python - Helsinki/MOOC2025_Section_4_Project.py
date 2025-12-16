# https:/programming-25.mooc.fi/part-4
# End of chapter project. 

def getInput(): # Get Input & Export As: [[15, 87], [10, 55], [11, 40], [4, 16]] | (examPoints, exerciseQty)
    student_values = []

    while True:
        student_input = input("Exam points and exercises completed: ")
        if student_input == "":
            break
        else:
            student_input = [int(student_input) for student_input in student_input.split()]
            student_values.append(student_input)
    return student_values

def getExercisePoints(student_values): #takes exerciseQty from student_values: returns exercisePoints
    exercisePoints = []

    for examPoints, exerciseQty in student_values:

        if (exerciseQty / 100) == 1:
            exercisePoints.append(10)
        elif (exerciseQty / 100) <= .99 and (exerciseQty / 100) >= .90:
            exercisePoints.append(9)
        elif (exerciseQty / 100) <= .89 and (exerciseQty / 100) >= .80:
            exercisePoints.append(8)
        elif (exerciseQty / 100) <= .79 and (exerciseQty / 100) >= .70:
            exercisePoints.append(7)
        elif (exerciseQty / 100) <= .69 and (exerciseQty / 100) >= .60:
            exercisePoints.append(6)
        elif (exerciseQty / 100) <= .59 and (exerciseQty / 100) >= .50:
            exercisePoints.append(5)
        elif (exerciseQty / 100) <= .49 and (exerciseQty / 100) >= .40:
            exercisePoints.append(4)
        elif (exerciseQty / 100) <= .39 and (exerciseQty / 100) >= .30:
            exercisePoints.append(3)
        elif (exerciseQty / 100) <= .29 and (exerciseQty / 100) >= .20:
            exercisePoints.append(2)
        elif (exerciseQty / 100) <= .19 and (exerciseQty / 100) >= .10:
            exercisePoints.append(1)
        elif (exerciseQty / 100) < .10:
            exercisePoints.append(0)

    return exercisePoints
    

def getGradeVal(student_values, exercisePoints): #take examPoints & add it w/ exercisePoints: returns gradeValList
    
    student_values_source = student_values
    examPoints, exerciseQty = zip(*student_values_source)
  
    i = 0 
    gradeValList = []
    while i < len(exercisePoints):
        if (examPoints[i] + exercisePoints[i] < 10) or examPoints[i] < 10:
            gradeVal = examPoints[i]
            gradeValList.append(gradeVal)
            i+=1
        else:
            gradeVal = examPoints[i] + exercisePoints[i]
            gradeValList.append(gradeVal)
            i+=1
    return gradeValList


def getGradeLetter(gradeValList): #compare results to a table & format for letter completion (returns gradeLetterFinal as a list)

    gradeLetterFinal = []
    for grade in gradeValList:
        
        if grade <= 14:
            gradeLetterFinal.append(0)
        elif 15 <= grade <=17:
            gradeLetterFinal.append(1)
        elif 18 <= grade <=20:
            gradeLetterFinal.append(2)
        elif 21 <= grade <=23:
            gradeLetterFinal.append(3)
        elif 24 <= grade <=27:
            gradeLetterFinal.append(4)
        elif 28 <= grade <=30:
            gradeLetterFinal.append(5)
    
    return gradeLetterFinal


def formatted(gradeValList, gradeLetterFinal, student_values, exercisePoints): #gradeValList = [23, 15, 15, 5], gradeLetterFinal = [3, 1, 1, 0]
   
    student_values_source = student_values
    examPoints, exerciseQty = zip(*student_values_source)

    i = 0
    class_fail = 0
    while i < len(gradeLetterFinal):
        if gradeLetterFinal[i] == 0:
            class_fail += 1
            i+=1
        else:
            i+=1

    gradeValAverage = (sum(examPoints)+sum(exercisePoints))/len(gradeValList)
    gradePassPercentage = ((len(gradeLetterFinal)-class_fail)/len(gradeLetterFinal)) * 100

    print("Statistics: ")
    print(f"Points average: {gradeValAverage:.1f}")
    print(f"Pass percentage: {gradePassPercentage:.1f}")
    print("Grade distribution:")
    print(f"  5:", gradeLetterFinal.count(5)*"*")
    print(f"  4:", gradeLetterFinal.count(4)*"*")
    print(f"  3:", gradeLetterFinal.count(3)*"*")
    print(f"  2:", gradeLetterFinal.count(2)*"*")
    print(f"  1:", gradeLetterFinal.count(1)*"*")
    print(f"  0:", gradeLetterFinal.count(0)*"*")
   


def main():
    inputs = getInput() # @TestString1: [[20, 100], [10, 10], [9, 100], [15, 75], [18,40]] 
    findExercisePoints = getExercisePoints(inputs)
    findGradeVal = getGradeVal(inputs, findExercisePoints)
    findGradeLetterFinal = getGradeLetter(findGradeVal)
    
    formatted(findGradeVal, findGradeLetterFinal, inputs, findExercisePoints)
    
main()


