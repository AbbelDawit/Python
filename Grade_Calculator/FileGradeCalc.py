#Name:        Abbel Dawit
#Date:        10/20/15
#Description: Script to calculate a weighted grade from data in file.



def main():

    name_file = raw_input("Please enter the name of the file: ")

    fileName = open(name_file,"r")

    total = 0
    weightedScore = 0

    for line in fileName:
         fileSplit = line.split()
         grades = fileSplit[1:]
         weight = fileSplit[0]
         avgGrades = 0

         for g in grades:
             avgGrades = avgGrades + int(g)
             avgWeight = float(weight)
             total  = avgWeight * (avgGrades/len(grades))

         weightedScore = weightedScore + total

    print("Your weighted grade is:", weightedScore)

main()

