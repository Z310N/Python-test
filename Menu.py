while True:
    print("MAIN MENU".center(80, "—"))
    print("1. FizzBuzz (Easy 1)")
    print("2. Leap Year (Easy 2)")
    print("3. Harf Pyramid Right (Easy 3.1)")
    print("4. Harf Pyramid Left (Easy 3.2)")
    print("5. Triangle Void (Easy 3.3)")
    print("6. Mid Pyramid (Easy 3.4)")
    print("7. Dimond Sharp (Easy 3.5)")
    print("8. Pyramid Abcde (Easy 3.6)")
    print("9. Prime Numbers (Medium 1)")
    print("0. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        print("")
        if choice == 1:
            import Program.FizzBuzz
        elif choice == 2:
            import Program.LeapYear
        elif choice == 3:
            import Program.HarfPyramidRight
        elif choice == 4:
            import Program.HarfPyramidLeft
        elif choice == 5:
            import Program.trianVoid
        elif choice == 6:
            import Program.midrapy
        elif choice == 7:
            import Program.DimondSharp
        elif choice == 8:
            import Program.pyramidAbcde
        elif choice == 9:
            import Program.PrimeNumbers
        elif choice == 0:
            exit()
        else:
            print("Invalid choice please try again")