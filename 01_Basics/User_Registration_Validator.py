# ------------------ User Registration Validator
# Requirements:
      #--1 Allowed usernames:
      #--2 Ask for a new username.
      #--3 If the username already exists:
# List of existing usernames (commas added between elements)
existing_users = ["kakmal", "ratan", "subrata"]

def register_user():
    while True:
        # Prompt for a new username and trim whitespace
        new_username = input("Enter a new username: ").strip()

        # Check for empty input
        if not new_username:
            print("Username cannot be empty. Please try again.\n")
            continue

        # Check if username already exists (case-insensitive)
        if new_username.lower() in [user.lower() for user in existing_users]:
            print(f"The username '{new_username}' is already taken. Please choose a different one.\n")
        else:
            # Register the new user
            existing_users.append(new_username)
            print(f"Success! Username '{new_username}' registered successfully.")
            break

# Run the registration function
register_user()

