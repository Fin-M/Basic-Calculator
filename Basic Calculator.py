print("\nThis is a Basic Calculator!")

first = float(input("\nWhat is your first number?: "))
second = float(input("What is your second number?: "))
operator = input("What do you want to do with the numbers (multiply, divide, add, subtract or power)?: ")


if operator == "multiply":
    print("\nThe answer is:", first * second)

elif operator == "divide":
    answer = first / second
    print("\nThe answer is:", answer)
    dp = round(answer, 2)
    print("or:", dp, "rounded to 2 decimal places.")

elif operator == "add":
    print("\nThe answer is:", first + second)

elif operator == "subtract":
    print("\nThe answer is:", first - second)

elif operator == "power":
    print("\nThe answer is:", first ** second)

else:
    print("\n[Error]")
    print("The number or operator you entered was incorrect.  Read the instructions carefully and try again!")


print("\n[Coded, edited and updated by Fin McGhie]\n")
