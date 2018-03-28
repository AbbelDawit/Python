#Name:        Abbel Dawit
#Date:        09/16/2015
#Description: Script calculates a users course grade.


def main():

    homeworkWeight = input("Please enter the homework weight (Flaot): ")
    homeworkGrade = input("Please enter the homework grade: ")
    examWeight = input("Please enter the exam weight (Float): ")
    examGrade = input("Please enter the exam grade: ")
    discussionWeight = input("Please enter the discussion weight (Float): ")
    discussionGrade = input("Please enter the disscussion grade: ")

    finalGrade = (homeworkWeight*homeworkGrade)+(examWeight*examGrade)+(discussionWeight*discussionGrade)

    print("The final numberical grade is:", finalGrade)

    if finalGrade >= 90:
        print("This earns you an A in the class.")
    elif finalGrade >= 80:
        print("This earns you a B in the class.")
    elif finalGrade >= 70:
        print("This earns you a C in the class.")
    elif finalGrade >= 60:
        print("This earns you a D in the class.")
    else:
        print("This earns you a F in the class.")

main()
