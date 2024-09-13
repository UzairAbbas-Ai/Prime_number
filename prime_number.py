def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_user_input():
    name = input("Enter your name= ")
    num1 = int(input("Enter your first favorite number= "))
    num2 = int(input("Enter your second favorite number= "))
    num3 = int(input("Enter your third favorite number= "))
    return name, num1, num2, num3

def process_numbers(numbers):
    parity = [(num, "even") if num % 2 == 0 else (num, "odd") for num in numbers]
    squares = [(num, num**2) for num in numbers]
    total = sum(numbers)
    is_prime_num = is_prime(total)
    return parity, squares, total, is_prime_num

def print_results(name, parity, squares, total, is_prime_num):
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    print("Number Parity:")
    for num, parity in parity:
        print(f"The number {num} is {parity}.")

    print("\nNumber Squares:")
    for num, square in squares:
        print(f"The number {num} and its square: ({num}, {square})")

    print("\nSum of Your Favorite Numbers:")
    print(f"The sum of your favorite numbers is: {total}")

    print("\nPrime Number Check:")
    if is_prime_num:
        print(f"Wow, {total} is a prime number!")
    else:
        print(f"{total} is not a prime number.")


name, num1, num2, num3 = get_user_input()
numbers = [num1, num2, num3]
parity, squares, total, is_prime_num = process_numbers(numbers)
print_results(name, parity, squares, total, is_prime_num)