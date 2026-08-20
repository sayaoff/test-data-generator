import unittest

from generator import generate_password, generate_users, generate_valid_user


class GeneratorTests(unittest.TestCase):
    def test_valid_user_contains_required_fields(self):
        user = generate_valid_user()

        self.assertEqual(
            set(user),
            {
                "first_name",
                "last_name",
                "email",
                "phone",
                "username",
                "password",
                "data_type",
            },
        )
        self.assertIn("@", user["email"])
        self.assertTrue(user["phone"].startswith("+79"))
        self.assertEqual(user["data_type"], "valid")

    def test_password_contains_different_character_types(self):
        password = generate_password(12)

        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in "!@#$%" for char in password))

    def test_requested_user_count(self):
        self.assertEqual(len(generate_users(7)), 7)

    def test_invalid_user_has_invalid_label(self):
        user = generate_users(1, invalid=True)[0]
        self.assertTrue(user["data_type"].startswith("invalid_"))

    def test_zero_count_raises_error(self):
        with self.assertRaises(ValueError):
            generate_users(0)

    def test_too_short_password_raises_error(self):
        with self.assertRaises(ValueError):
            generate_password(3)


if __name__ == "__main__":
    unittest.main()
