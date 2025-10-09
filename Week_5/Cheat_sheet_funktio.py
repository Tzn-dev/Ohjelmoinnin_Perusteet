#print() #funktiokutsu
#print("Hello") # "Hello" on funktion parametri
#len()

#while True:
#    print("I can do thi ferever")

#def greet(name):
#    print(f"Hello {name}")

#print("Here I am")
#name = "Mira"
#greet(name)

#def greet(name):
#    return f"Hello, {name}"

#print(greet("Mira"))

def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18-age} years to fly solo.")

greeting_airport(age=48, person="Mira")
#tai
##greeting_airport("Mira", 48)


def is_prime(n):
    #"""Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        num = int(input("Enter a whole number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

    again = input("Do you want to check another number? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break