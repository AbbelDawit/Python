#Name:        Abbel Dawit
#Date:        09/17/2015
#Descritpion: Day of the week calculator for month starting on monday


def main():

    daysMonth = int(input("Please enter the day of the month here (1-31): "))

    monday = [1,8,15,22,29]
    tuesday = [2,9,16,23,30]
    wednesday = [3,10,17,24,31]
    thursday = [4,11,18,25]
    friday =  [5,12,19,26]
    saturday =  [6,13,20,27]
    sunday = [7,14,21,28]

    if daysMonth in monday:
        print("Today is Monday")

    if daysMonth in tuesday:
        print("Today is Tuesday")

    if daysMonth in wednesday:
        print("Today is Wednesday")

    if daysMonth in thursday:
        print("Today is Thursday")

    if daysMonth in friday:
        print("Today is Friday")

    if daysMonth in saturday:
        print("Today is Saturday")

    if daysMonth in sunday:
        print("Today is Sunday")

    if daysMonth > 31 or daysMonth < 1:
        print("Invalid Day")

main()
