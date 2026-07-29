from storage.file_manager import load_data, save_data


class User:
    def __init__(self, email, password, role):

        self.email = email
        self.password = password
        self.role = role

    def to_dict(self):

        return {
            "email": self.email,
            "password": self.password,
            "role": self.role,
        }

    def add_user(self):

        users = load_data("data/users.json")
        new_user = self.to_dict()
        users.append(new_user)
        save_data("data/users.json", users)
