from managers.auth_manager import AuthManager

def login_attempt():
    while True:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = AuthManager().login_validation(email, password)
        if user:
            print("Login successful!")
            print("Welcome!")
            return user
        print("Invalid email or password.")
    