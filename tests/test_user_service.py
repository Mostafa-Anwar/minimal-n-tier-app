import unittest
from backend.services.user_service import get_users

class TestUserService(unittest.TestCase):
    def test_get_users(self):
        users = get_users()
        self.assertIsInstance(users, list)

if __name__ == '__main__':
    unittest.main()
