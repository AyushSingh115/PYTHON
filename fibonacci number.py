N = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initializing the first two terms of the series
a, b = 0, 1

# Displaying the first N Fibonacci numbers
print("First", N, "Fibonacci numbers:")
count = 0
while count < N:
    print(a, end=" ")
    nth = a + b
    # Updating values for the next iteration
    a = b
    b = nth
    count += 1
