#Name:        Abbel Dawit
#Date:        10/10/2015
#Description: Script to validate that user input is between 0 and 100



def main():

    count = 0

    while (count == 0):

        userInput = int(input("Please enter a valid number (0-100): "))

        if (userInput >= 0) and (userInput <= 100):

            print("Thank you for selecting the number", userInput)

            count = count + 1

        else:

            print("That is invalid, please try again.")

main()
