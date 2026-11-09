
import random
import string

print("===== PASSWORD GENERATOR =====")

# Get password length from user
length = int(input("Enter password length: "))

# Characters for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nYour Generated Password is:", password)
