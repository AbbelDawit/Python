#Name:        Abbel Dawit
#Date:        10/05/2015
#Description: Script to draw a box out of user input width and height.

def main():

    width = int(raw_input("Please enter the width of the box: "))
    height = int(raw_input("Please enter the height of their box: "))
    symbol = raw_input("Please enter the sybol you would like to use: ")

    n=0


    print(symbol*width)

    for n in range (height-2):
        print(symbol + (width-2)*" " + symbol)

    print(symbol*width)

main()
