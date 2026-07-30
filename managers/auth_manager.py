from storage.file_manager import load_data


class AuthManager:
    def __init__(self):
        pass

    def login_validation(self, email, password):
        users = load_data("data/users.json")
        for user in users:
            if user.get("email") == email and user.get("password") == password:
                return user
        return None
