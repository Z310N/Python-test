rows = int(input("Enter the number of rows: "))  
  
k = 2 * rows - 2  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  
  
k = rows - 2  
for i in range(rows, -1, -1):  
    for j in range(k, 0, -1):  
        print(end=" ")  
    k = k + 1  
    for j in range(0, i + 1):  
        print("* ", end="")  
    print("")  

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