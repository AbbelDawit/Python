#Name:        Abbel Dawit
#Date:        10/25/15
#Description: Script that takes in list of integers from a user and then find statistics of the given list of integers.


def getList():
        integers = ""
        userList = []
        print("Enter a list of integers or q to end the list")
        while integers != "q":
                integers = raw_input("Enter an integer: ")
                if integers != "q":
                        userList.append(int(integers))
        return userList

def getMean(userList):
    average = 0
    total = 0
    for n in userList:
        total += n
        average = total/len(userList)
    return average


def getMedian(userList):
    finalList = userList.sort()
    if len(userList) % 2 == 0:
        middle = len(userList)//2
        print(middle)
    else:
       first =  (len(userList)-1) // 2
       second = (len(userList)+1) // 2
       return((first + second) / 2)

def getMin(userList):
        mini = userList[0]
        for x in userList:
                if x <= mini:
                        mini = x
        return(mini)


def getMax(userList):
        maxi = userList[0]
        for x in userList:
                if x >= maxi:
                        maxi = x
        return(maxi)

def emptyList(userList):
        userList = []
        getList()


def printMenu():

        userList = getList()
        number = "1"
        while number != "0":
                print("please choose the statistics you would like to calculate!")
                print("""1. Min\n2. Max\n3. Mean\n4. Median\n5. Clear List""")


                number = raw_input("Please enter your choice, or 0 to exit: ")
                if number == "1":
                        minimumValue = getMin(userList)
                        print("The minimum value is: ",minimumValue)
                elif number == "2":
                        maximumValue = getMax(userList)
                        print("The maximum value is: ",maximumValue)
                elif number == "3":
                        meanValue = getMean(userList)
                        print("The mean value is: ",meanValue)
                elif number == "4":
                        medianValue = getMedian(userList)
                        print("The median value is: ",medianValue)
                elif number == "5":
                        clearList = emptyList(userList)
                        print("List has been cleared", clearList)


        if number == "0":
                print("Thank you for using my calculator!")

        return

def main():

        print("Welcome to the List Statistics Calculator")

        printMenu()


main()
