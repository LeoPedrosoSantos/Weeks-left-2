print("***Weeks left to X years***\n")
Age = int(input("How old are you?\n"))
Years = int(input("Choose the age you want:\n"))

Calculate = Years - Age

OneYear = 52.1786

Calculate2 = Calculate * OneYear

Result = Calculate2

print(f"\nYou have {round(Result ,2)} weeks left to {Years} years")

print(input("\nClick ENTER to close the window"))