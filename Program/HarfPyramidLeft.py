def pypart2(n):
     
    k = 2*n - 2
 
    for i in range(0, n):
     
        for j in range(0, k):
            print(end=" ")
     
        k = k - 2
     
        for j in range(0, i+1):
         
            print("* ", end="")
            
        print("\r")
 
# Driver Code
n = int(input("Input Number :"))
pypart2(n)

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
