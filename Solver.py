import math
from colorama import Fore, Back, Style
from colorama import init


init()

print(Fore.YELLOW +'''

╔═╗ ┬ ┬┌─┐┌┬┐┬─┐┌─┐┌┬┐┬┌─┐  ╔═╗┌─┐ ┬ ┬┌─┐┌┬┐┬┌─┐┌┐┌  ╔═╗┌─┐┬ ┬  ┬┌─┐┬─┐  
║═╬╗│ │├─┤ ││├┬┘├─┤ │ ││    ║╣ │─┼┐│ │├─┤ │ ││ ││││  ╚═╗│ ││ └┐┌┘├┤ ├┬┘  
╚═╝╚└─┘┴ ┴─┴┘┴└─┴ ┴ ┴ ┴└─┘  ╚═╝└─┘└└─┘┴ ┴ ┴ ┴└─┘┘└┘  ╚═╝└─┘┴─┘└┘ └─┘┴└─  v1.0
                    by - Faisal Khan

                   Type 'quit' to exit!

''')




while True:
    init()
    
    while True:
        init()

        a = input("Enter the cofficient of X^2: ")
        try:
            a = float(a)
            break
        except:
            if a == "quit":
                print("\nExiting!")
                quit()
            else:
                print('Bad Input!')
            

            continue
    if a == 0:
        print('A Quadratic Equation Cannot Have Cofficient of X^2 = 0 \nPlease try again! or type quit to exit!')
        continue
    


    while True:
        init()
        b = input("Enter the cofficient of x: ")
        try:
            b = float(b)
            break
        except:
            if b == "quit":
                print("\nExiting!")
                quit()
            else:
                print('Bad Input!')

    while True:
        init()
        c = input("Enter the Value of Constant: ")
        try:
            c = float(c)
            break
        except:
            if c == "quit":
                print("\nExiting!")
                quit()
            else:
                print('Bad Input!')

    break
      
init()

determinant = b * b - 4 * a * c
sqr = math.sqrt(abs(determinant))

root_x = (-b + sqr) / (2 * a)
root_y = (-b - sqr) / (2 * a)

croot = - b / (2 * a)

print(Fore.GREEN +'''
*************************************************
                   Results
*************************************************''')


print(Fore.YELLOW +"Equation: ","(",a,")","x^2 +","(",b,")","x +","(",c,")","= 0")
print('''-------------------------------------------------''')




if determinant == 0: #real and same
    print(Fore.YELLOW + "\nNote: The Roots are Real & Same.")
    print('''-------------------------------------------------''')
    print(Fore.WHITE +"\nRoots:")
    print(Fore.YELLOW + "\n(1)", root_x, "\n(2)", root_y)

elif determinant > 0: #real and different
    print(Fore.YELLOW +"\nNote: The Roots are Real & Different.")
    print('''-------------------------------------------------''')
    print(Fore.WHITE +"\nRoots:")
    print(Fore.YELLOW + "\n(1)", root_x, "\n(2)", root_y)
else:
    print(Fore.RED +"\nNote: This equation has Complex Roots.")
    print('''-------------------------------------------------''')
    print(Fore.WHITE +"\nRoots:")
    print(Fore.RED + "\n(1)", croot,"+i",sqr, "\n(2)", croot,"+i",sqr)

print(Fore.GREEN +'''
*************************************************''')
print(Fore.RESET +" ")
