#attempting  to make a simple calculator

#this is the function to add integer
def addition(x,y):
    return x + y
#function to substract
def substraction(x,y):
    return x - y
#function to multiply
def multiplication(x,y):
    return x * y
#function to divide
def divide(x,y):
    return x / y

print("select your operator")
print("1 for addition")
print("2 for substraction")
print("3 for multiplication")
print("4 for divition")

while True:
    choice = input("choose an operator(1/2/3/4/): ")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("input a number: "))
        num2 = float(input("input another number: "))

        if choice == "1":
            print(num1, "+", num2, "=", addition(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=",substraction(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiplication(num1, num2))
        elif choice == "4":
            print(num1,"/", num2, "=", divide(num1, num2))

        next = input("want to calculate again? ")
        if next == "no":
            break
    else:
        print("invalid input, try again")


