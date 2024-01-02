# Given string
S1 = "I Love Python 23."

# Initialize counters
vowel_count = 0
consonant_count = 0
space_count = 0
digit_count = 0

# Iterate through each character in the string
for char in S1:
    # Check if the character is a vowel
    if char.upper() in "AEIOU":
        vowel_count += 1
    # Check if the character is a consonant
    elif char.isalpha():
        consonant_count += 1
    # Check if the character is a space
    elif char.isspace():
        space_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1

# Display the results
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
print("Digits:", digit_count)
