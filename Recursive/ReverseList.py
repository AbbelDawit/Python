#Name:        Abbel Dawit
#Date:        11/19/15
#Description: Script use a recursive function that takes in a list of integers as a parameter,and prints out the list reversed.

def rev(userList):

    if len(userList) == 0:
        return

    else:
        print(userList[-1])
        userList = userList[:-1]
        rev(userList)


def main():

    userInput = 0
    userList = []
    while userInput != -1:

        userInput = int(raw_input("Enter a number to append to the list, or -1 to stop: "))

        if userInput != -1:
            userList.append(userInput)

    print("The list as you entered it is: ", userList)

    print("The reversed list is: ")

    rev(userList)

main()
