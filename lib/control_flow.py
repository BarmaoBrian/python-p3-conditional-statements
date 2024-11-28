def hows_the_weather():
    try:
        temperature = float(input("Enter the temperature: "))
        date = input("Enter the date: ")
        
        if temperature < 40:
            return f"It's brisk out there! ({date})"
        elif 40 <= temperature <= 65:
            return f"It's a little chilly out there! ({date})"
        elif temperature > 85:
            return f"It's too dang hot out there! ({date})"
        else:
            return f"It's perfect out there! ({date})"
    except ValueError:
        return "Please enter a valid number for the temperature."

# Example usage:
print(hows_the_weather())
# %%

def admin_login():
    attempts = 0
    max_attempts = 3
    correct_username = ["admin", "ADMIN"]
    correct_password = "12345"

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in correct_username and password == correct_password:
            return "Access granted"
        else:
            attempts += 1
            print("Access denied. Try again.")

    return "Access denied"

# Example usage:
print(admin_login())

def calculator(operation):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        else:
            print("Invalid operation!")
            return None
    except ValueError:
        print("Please enter valid numbers.")
        return None

# Example usage:
operation = input("Enter the operation (+, -, *, /): ")
result = calculator(operation)
if result is not None:
    print(f"The result is: {result}")

# %%
