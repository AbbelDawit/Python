#Name:        Abbel Dawit
#Date:        09/16/2015
#Description: A sample medical diagnosis software.


def main():


    yes = "y"
    no = "n"

    Fever = raw_input("Do you have a fever? (y/n):")

    if Fever in yes:
        Rash = raw_input("Do you have a rash? (y/n):")
        if Rash in yes:
            print("Your diagnosis: You have the Measles.")
        elif Rash in no:
            earPain = raw_input("Do your ears hurt? (y/n):")
            if earPain in yes:
                print("Your diagnosis: You have an Ear Infection.")
            elif earPain in no:
                print("Your diagnosis: You have the Flu.")

    if Fever in no:
        stuffyNose = raw_input("Do you have a stuffy nose? (y/n):")
        if StuffyNose in yes:
            print("Your diagnosis: You have a Head Cold")
        if stuffyNose in no:
            print("Your diagnosis: You are Hypochondriac")

main()
