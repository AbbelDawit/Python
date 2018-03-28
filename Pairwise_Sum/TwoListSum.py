#Name:         Abbel Dawit
#Date:         10/10/25
#Descritption: Script to take the sum of two user inputed lists.

def main():

    firstList = []
    secondList = []

    userInput = ""

    while (userInput != "end"):

        userInput = raw_input("""[1] please enter a number (or "end" to stop): """)

        if userInput.isdigit():
            firstList.append(int(userInput))

    userInput = ""

    while (userInput != "end"):

        userInput = raw_input("""[2] please enter a number (or "end" to stop): """)

        if userInput.isdigit():

            if len(secondList) < len(firstList):
                secondList.append(int(userInput) * firstList[len(secondList)])

            else:
                secondList.append(int(userInput))
    print(secondList)

main()
