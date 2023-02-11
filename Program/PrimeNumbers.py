def isprime(n):
     
    # Corner case
    if n <= 1 :
        return False
 
    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
 
    return True
 
# Function to print primes
def printprime(n):
    for i in range(2, n + 1):
        if isprime(i):
            print(i, end = " ")
 
# Driver code
if __name__ == "__main__" :
    n = int(input("Input Number :"))
    # function calling
    printprime(n)

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