import re

#func get details with validation
def get_details():
    while True:
        name = input("What is your name? \n")
        if name.isalpha():
            break
        print("name should contain only letter")

    while True:
        email = input("What is your email? \n")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        print("enter valid email address")

    while True:
        try:
            age = float(input("What is your age? \n"))
            break
        except ValueError:
            print("age should be a number")

    return name, email, age

#func print details
def print_details(name, email, age):
    print(f"Name: {name}, Email: {email}, Age: {age}")

#func operations
def operations(num1, num2):
    results = {}
    results['sum'] = num1 + num2
    results['difference'] = num1 - num2
    results['product'] = num1 * num2
    results['division'] = num1 / num2 if num2 != 0 else "undefined"
    results['remainder'] = num1 % num2 if num2 != 0 else "undefined"
    results['power'] = num1 ** num2
    return results

#func print results
def print_results(results, num1, num2):
    print(f"Sum: {results['sum']}")
    print(f"Difference: {results['difference']}")
    print(f"Product: {results['product']}")
    print(f"Division: {results['division']}")
    print(f"Remainder: {results['remainder']}")
    print(f"{num1} ^ {num2} is: {results['power']}")


#get details
name, email, age = get_details()

#print details
print_details(name, email, age)

#gaet num1 and num2
while True:
    try:
        num1 = float(input("Insert number1: "))
        num2 = float(input("Insert number2: "))
        break
    except ValueError:
        print("Enter valid numbers.")

#operations
results = operations(num1, num2)

#print results
print_results(results, num1, num2)

