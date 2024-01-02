#pailidrome
# Input a number
num = int(input("Enter a number: "))

# Convert the number to a string for comparison
num_str = str(num)

# Reverse the string
reverse_str = num_str[::-1]

# Check if the original and reversed strings are the same
if num_str == reverse_str:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
