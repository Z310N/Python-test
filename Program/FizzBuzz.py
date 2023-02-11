for fizzbuzz in range(1,100):
 
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")                                        
        continue
 
    elif fizzbuzz % 3 == 0:    
        print("Fizz")                                        
        continue
 
    elif fizzbuzz % 5 == 0:        
        print("Buzz")                                    
        continue
 
    print(fizzbuzz)

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
