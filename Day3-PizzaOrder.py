print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 12 13 15 "))
people = int(input("How many people to split the bill? "))

if tip==12 :
    b = round(((bill * 1.12) / people),2)
    print("bill per person : " + str(b))
if tip==13 :
    print("Each person should pay: "+str((bill * 1.13) / people))

if tip==15 :
    print("Each person should pay: "+str((bill * 1.15) / people))