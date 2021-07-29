import unittest
import main
import json

with open("test.json", 'r', -1, encoding="utf-8") as f:
    data = json.load(f)

with open("goods.schema.json", 'r', -1, encoding="utf-8") as file:
    schema = json.load(file)


class MyTests(unittest.TestCase):

    def test_validate_json(self) -> None:
        """Проверка валидации json."""
        self.assertTrue(main.validate_json(data, schema))

    def test_create_connection(self) -> None:
        """Проверка коннекта к БД."""
        self.assertTrue(main.create_connection("goods_account", "postgres",
                                               "123456", "localhost", "5433"))


if __name__ == '__main__':
    unittest.main()
