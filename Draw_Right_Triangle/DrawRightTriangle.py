#Name:        Abbel Dawit
#Date:        10/01/2015
#Description: Script to draw a right triangle out of user selected symbol.



def main():

    height = int(raw_input("Please enter the height of your triangle: "))
    symbol = raw_input("Please enter a single character for the symbol: ")

    n = 0

    for n in range (height):

        print(symbol * n)
        n = 1

main()

