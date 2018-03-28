#Name:        Abbel Dawit
#Date:        11/19/15
#Description: Script to use the recursive function that prints a right triangel, 
#             with the "tip" of the triangel pointing down.

def tri(height,symbol):

    if height == 0:
        return

    else:
        print(symbol * height)
        height = height - 1
        tri(height, symbol)



def main():

    inputHeight = int(raw_input("Please enter the height of your triangle: "))

    while inputHeight <= 0:

        print("Your triangle height must be positive (> 0).")
        inputHeight = int(raw_input("Please enter the height of your triangle: "))

    inputSymbol = raw_input("Please enter a character for your triangle: ")
    tri(inputHeight,inputSymbol) 

main()
