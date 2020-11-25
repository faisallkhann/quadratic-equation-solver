import math
from colorama import Fore, Back, Style

print(Fore.YELLOW +'''

╔═╗ ┬ ┬┌─┐┌┬┐┬─┐┌─┐┌┬┐┬┌─┐  ╔═╗┌─┐ ┬ ┬┌─┐┌┬┐┬┌─┐┌┐┌  ╔═╗┌─┐┬ ┬  ┬┌─┐┬─┐  
║═╬╗│ │├─┤ ││├┬┘├─┤ │ ││    ║╣ │─┼┐│ │├─┤ │ ││ ││││  ╚═╗│ ││ └┐┌┘├┤ ├┬┘  
╚═╝╚└─┘┴ ┴─┴┘┴└─┴ ┴ ┴ ┴└─┘  ╚═╝└─┘└└─┘┴ ┴ ┴ ┴└─┘┘└┘  ╚═╝└─┘┴─┘└┘ └─┘┴└─  v1.0
                    by - Faisal Khan

''')




while True:
    
    while True:
        a = input(Fore.RESET +"Enter the cofficient of X^2: ")
        try:
            a = float(a)
            break
        except:
            print('Bad Input!')
            continue
    if a == 0:
        print('A Quadratic Equation Cannot Have Cofficient of X^2 = 0 \nPlease try again! or type quit to exit!')
        continue


    while True:
        b = input("Enter the cofficient of x: ")
        try:
            b = float(b)
            break
        except:
            print('Bad Input!')        
            continue


    while True:
        c = input("Enter the Value of Constant: ")
        try:
            c = float(c)
            break
        except:
            print('Bad Input!')        
            continue
    break
      

determinant = b * b - 4 * a * c
sqr = math.sqrt(abs(determinant))

root_x = (-b + sqr) / (2 * a)
root_y = (-b - sqr) / (2 * a)

croot = - b / (2 * a)

print(Fore.GREEN +'''
*************************************************
                   Results
*************************************************''')

print(Fore.YELLOW +"Equation: ",a,"x^2 +",b,"x +","(",c,") = 0")
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