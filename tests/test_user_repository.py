import unittest
from data.user_repository import fetch_all_users

class TestUserRepository(unittest.TestCase):
    def test_fetch(self):
        users = fetch_all_users()
        self.assertIsInstance(users, list)

if __name__ == '__main__':
    unittest.main()
