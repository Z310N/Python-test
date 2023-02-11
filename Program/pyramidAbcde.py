def sequence(d):
   c, l = 0, 1
   while c < d - 1:
     if l%2:
       yield l
       c += 1
     l += 1

def make_pattern(d):
   t, b, r = f'{"A"*(d-1)}+{"B"*(d-1)}', f'{"C"*(d-1)}+{"D"*(d-1)}', list(sequence(d))
   body = '\n'.join(f'{"A"*((r[-1]-i)//2)}+{"E"*i}+{"B"*((r[-1]-i)//2)}' for i in r[:-1]) + \
     f'\n+{"E"*r[-1]}+\n'+'\n'.join(f'{"C"*((r[-1]-i)//2)}+{"E"*i}+{"D"*((r[-1]-i)//2)}' for i in r[:-1][::-1])
   return f'{t}\n{body}\n{b}'

def diamond(d):
  return {1:lambda _:'+', 2:lambda _:'A+B\n+E+\nC+D'}.get(d, make_pattern)(d)

n = int(input("Input Number : "))
print("")
print(diamond(n))

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