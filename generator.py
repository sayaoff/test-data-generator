"""Генерация тестовых пользовательских данных."""

import random
import string

FIRST_NAMES = ["alex", "anna", "ivan", "maria", "nikita", "olga", "pavel", "sofia"]
LAST_NAMES = ["ivanov", "petrova", "smirnov", "volkova", "sokolov", "popova"]
DOMAINS = ["example.com", "test.local", "mail.test"]


def generate_password(length: int = 10) -> str:
    """Создаёт пароль с буквами, цифрами и специальным символом."""
    if length < 4:
        raise ValueError("Длина пароля должна быть не меньше 4 символов")

    required = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%"),
    ]
    remaining = random.choices(string.ascii_letters + string.digits + "!@#$%", k=length - 4)
    password = required + remaining
    random.shuffle(password)
    return "".join(password)


def generate_valid_user() -> dict[str, str]:
    """Создаёт набор корректных тестовых данных."""
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    number = random.randint(10, 9999)

    return {
        "first_name": first_name.title(),
        "last_name": last_name.title(),
        "email": f"{first_name}.{last_name}{number}@{random.choice(DOMAINS)}",
        "phone": f"+79{random.randint(100000000, 999999999)}",
        "username": f"{first_name}_{last_name}_{number}",
        "password": generate_password(),
        "data_type": "valid",
    }


def generate_invalid_user() -> dict[str, str]:
    """Создаёт данные с одной случайной ошибкой для негативных тестов."""
    user = generate_valid_user()
    invalid_variants = [
        ("first_name", ""),
        ("email", "email-without-at-sign"),
        ("phone", "123"),
        ("username", "a"),
        ("password", "123"),
    ]
    field, value = random.choice(invalid_variants)
    user[field] = value
    user["data_type"] = f"invalid_{field}"
    return user


def generate_users(count: int, invalid: bool = False) -> list[dict[str, str]]:
    """Создаёт указанное количество записей."""
    if count < 1:
        raise ValueError("Количество записей должно быть больше нуля")

    generator = generate_invalid_user if invalid else generate_valid_user
    return [generator() for _ in range(count)]
