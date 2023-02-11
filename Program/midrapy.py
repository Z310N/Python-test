row = int(input("Input rows : "))

for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if i==1 or j==1 or j==2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
# Lower-Half
for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

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
