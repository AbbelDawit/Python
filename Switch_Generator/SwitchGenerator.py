#Name:        Abbel Dawit
#Date:        09/17/2015
#Description: Script used to determine if gernerator is on or off based on swith states.

def main():

    yes = "y"
    no = "n"

    firstSwitch = raw_input("Is the first switch on? (y/n): ")
    secondSwitch = raw_input("Is the second switch on? (y/n): ")

    if firstSwitch == secondSwitch in yes or firstSwitch == secondSwitch in no:
        print("The generator is OFF")
    else:
        print("The generator is ON.")

main()
