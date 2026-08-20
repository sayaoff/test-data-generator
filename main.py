"""Консольный запуск генератора тестовых данных."""

import argparse

from exporters import save_to_csv, save_to_json
from generator import generate_users


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Генератор пользовательских данных для тестирования"
    )
    parser.add_argument("-n", "--count", type=int, default=5, help="Количество записей")
    parser.add_argument(
        "--invalid", action="store_true", help="Создать некорректные данные"
    )
    parser.add_argument(
        "-f", "--format", choices=["json", "csv"], default="json", help="Формат файла"
    )
    parser.add_argument("-o", "--output", help="Путь к итоговому файлу")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        users = generate_users(args.count, invalid=args.invalid)
        output = args.output or f"output/users.{args.format}"

        if args.format == "json":
            path = save_to_json(users, output)
        else:
            path = save_to_csv(users, output)

        print(f"Готово: создано записей — {len(users)}")
        print(f"Файл сохранён: {path}")
    except (ValueError, OSError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
