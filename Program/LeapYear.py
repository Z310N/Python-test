year = int(input("Input Year :"))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} -> true".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} -> true".format(year))

else:
    print("{0} -> false".format(year))

print("")
print("MENU".center(80, "—"))
print("0. Exit")
print("1. Menu")

while True:
    choice = int(input("Enter your choice: "))
    print("")
    if choice == 1:
        import Menu
    elif choice == 0:
        exit()
    else:
        print("Invalid choice")
        print("")
