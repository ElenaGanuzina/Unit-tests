from typing import List


class User:
    def __init__(self, name: str, password: str, is_admin: bool = False):
        self._name = name
        self._password = password
        self._is_admin = is_admin
        self._is_authenticated = False

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def is_authenticated(self):
        return self._is_authenticated

    def authenticate(self, name: str, password: str) -> bool:
        if self._name == name and self._password == password:
            self._is_authenticated = True
        else:
            self._is_authenticated = False
        return self._is_authenticated


class UserRepository:
    def __init__(self, users: List[User] = None):
        if users is None:
            self._users = []
        self._users = users

    @property
    def users(self):
        return self._users

    def add_user(self, user: User) -> None:
        if user.is_authenticated:
            self._users.append(user)

    def logout_except_admins(self) -> None:
        for user in self._users:
            if not user.is_admin:
                user.is_authenticated = False
                self._users.remove(user)
