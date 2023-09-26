import unittest
from user import User, UserRepository


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Alex', '12345')

    def test_authenticate_success(self):
        self.assertTrue(self.user.authenticate('Alex', '12345'))

    def test_authentic_fail_name(self):
        self.assertFalse(self.user.authenticate('Mike', '12345'))
        self.assertFalse(self.user.authenticate('', '12345'))

    def test_authentic_fail_password(self):
        self.assertFalse(self.user.authenticate('Alex', '56788'))
        self.assertFalse(self.user.authenticate('Alex', ''))

    def test_authentic_fail_all(self):
        self.assertFalse(self.user.authenticate('Mike', '98765'))
        self.assertFalse(self.user.authenticate('', ''))


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.authentic_user = User('Alex', '12345')
        self.authentic_user.authenticate('Alex', '12345')

        self.non_authentic_user = User('Mike', '98765')

        users = [User(f'User{i}', f'password{i}', is_admin=True) for i in range(2)]
        for user in users:
            user.authenticate(user.name, user.password)

        self.repository = UserRepository(users)

    def test_authentic_user_add(self):
        self.repository.add_user(self.authentic_user)
        self.assertTrue(self.authentic_user in self.repository.users)

    def test_non_authentic_user_add(self):
        self.repository.add_user(self.non_authentic_user)
        self.assertFalse(self.non_authentic_user in self.repository.users)

    def test_logout_except_admins(self):
        self.repository.logout_except_admins()
        self.assertTrue(all(user.is_admin for user in self.repository.users))
