# Prime_number
A Python program that explores favorite numbers, providing information on their parity, squares, sum, and prime status.
## Python Code to Explore Favorite Numbers

**Explanation of the Code:**

1. **`is_prime(num)` Function:**
   - Checks if a given number `num` is prime.
   - Returns `False` if `num` is less than or equal to 1.
   - Returns `True` if `num` is less than or equal to 3.
   - Checks if `num` is divisible by 2 or 3. If so, returns `False`.
   - Iterates through numbers from 5 to the square root of `num` with a step of 6:
      - If `num` is divisible by `i` or `i + 2`, returns `False`.
   - If the loop completes without finding a divisor, returns `True` indicating `num` is prime.

2. **`get_user_input()` Function:**
   - Prompts the user to enter their name and three favorite numbers.
   - Returns the entered name and numbers as a tuple.

3. **`process_numbers(numbers)` Function:**
   - Takes a list of numbers as input.
   - Creates a list `parity` to store tuples of each number and its parity ("even" or "odd").
   - Creates a list `squares` to store tuples of each number and its square.
   - Calculates the sum of the numbers.
   - Checks if the sum is prime using the `is_prime` function.
   - Returns a tuple containing the `parity`, `squares`, `total`, and `is_prime_num` values.

4. **`print_results(name, parity, squares, total, is_prime_num)` Function:**
   - Prints a greeting message with the user's name.
   - Prints the parity information for each number.
   - Prints the number and its square for each number.
   - Prints the sum of the numbers.
   - Prints a message indicating whether the sum is a prime number.

5. **Main Execution:**
   - Calls the `get_user_input` function to get the user's name and favorite numbers.
   - Processes the numbers using the `process_numbers` function.
   - Prints the results using the `print_results` function.

**How the Code Works:**

1. The user enters their name and three favorite numbers.
2. The `process_numbers` function calculates the parity, squares, sum, and prime status of the numbers.
3. The `print_results` function displays the results in a formatted manner.
4. The program outputs the parity, squares, sum, and prime status of the user's favorite numbers.
