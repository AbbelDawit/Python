#Name:        Abbel Dawit
#Date:        10/20/15
#Description: Script to create text file on user input.


def main():


    name = ""
    stopText = ""

    text_file_name = raw_input("Name of text file: " )

    file = (text_file_name + ".txt")

    name_file = open(file,"w")

    name = raw_input("Please enter your name: ")

    name_file.write("Hello ")
    name_file.write(name)
    name_file.write("!")
    name_file.write("\n")


    while stopText != "DONE":

        input = raw_input("""Text (or "DONE"): """)

        stopText = input.upper()

        if stopText != "DONE":
            name_file.write(input)


        else:
            name_file.write("\nThe End")

    name_file.close()



main()
