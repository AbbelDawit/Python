#Name:        Abbel Dawit
#Date:        10/20/15
#Description: Script to calculate the total number of words in the file.


def main():

    fileName = raw_input("Please enter the file name: ")

    if fileName[-4:] == ".dat" or fileName[-4:] == ".txt":
        line = open(fileName, "r")
        wordRead = line.read()
        words = wordRead.split()

        wordCount = 0
        average = 0

        for x in words:
            lengthWord = len(words)
            average = average + len(x)
            wordCount = average / lengthWord

        print("The file", fileName, "has", lengthWord, "words in it.")
        print("On average, each word is", wordCount, "characters long.")

    else:
        print("The file must end in .txt or .dat to be valid.")

main()

