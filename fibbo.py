def fibonacci(n, step_count=0):
    if n <= 1:
        return (n, step_count)
    else:
        # Calculate the (n-1)th and (n-2)th Fibonacci numbers
        fib1, step_count = fibonacci(n - 1, step_count + 1)
        fib2, step_count = fibonacci(n - 2, step_count + 1)
        # Calculate the nth Fibonacci number
        fib = fib1 + fib2
        return (fib, step_count)

# Input: The position of the Fibonacci number you want to calculate
n = int(input("Enter the position of the Fibonacci number: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result, steps = fibonacci(n)
    print(f"The Fibonacci number at position {n} is {result}")
    print(f"Number of steps taken: {steps}")
