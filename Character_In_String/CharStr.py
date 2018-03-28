#Name:        Abbel Dawit                                                                                                                      
#Date:        09/16/2015
#Description: Script prints the number of times a character appears in a string.


def main():

    string = raw_input("please enter a string: ").upper()

    character = raw_input("please enter a character: ").upper()

    print("The character",character,"appears",string.count(character), "times in the string:",string)

main()
