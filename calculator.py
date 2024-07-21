def addition():
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        print("The sum of the numbers is:",a+b)


def substraction():
    a=int(input("Enter the first number(which is greater than the second):"))
    b=int(input("Enter the second number:"))
    print("This result is:",a-b)


def multiplication():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("This result is:",a*b)

def division():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if b == 0:
        print("You can't divide by zero")   
    else:
        print("the result is:",a/b)

def expression():
    result=eval(input("Enter the expression: "))
    print("The result is:",result)



def main():
        while True:
            print("Welcome!!!")
            print("Please select an option below")
            print("1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Any other Expression")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice =="1":
                addition()
            elif choice =="2":
                substraction()
            elif choice =="3":
                multiplication()
            elif choice =="4":
                division()
            elif choice =="5":
                expression()
            elif choice =="6":
                break
            else:
                print("Invalid input. Please try again.")

main()