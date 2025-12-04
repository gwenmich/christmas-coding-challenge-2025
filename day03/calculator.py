import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

calculating = True
print(art.logo)
n1 = None

while calculating:
    if not n1:
        n1 = float(input("What's the first number?: "))
    for key in operations.keys():
        print(key)
    operation = input("Pick an operation: ")
    n2 = float(input("What's the next number?: "))
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    next_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if next_calc == "y":
        n1 = result
    elif next_calc == "n":
        n1 = None
        print("\n" * 20)
        print(art.logo)
