correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your PIN: ")
    attempts = attempts + 1

    if entered_pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. Attempts left: {remaining}")
        else:
            print("Incorrect PIN. Card blocked.")