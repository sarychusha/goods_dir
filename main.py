"""ДЗ по теме "Словари"."""
import json
import jsonschema
import psycopg2
from psycopg2 import OperationalError

with open("test.json", "r", -1, encoding="utf-8") as f:
    data = json.load(f)

with open("goods.schema.json", "r", -1, encoding="utf-8") as file:
    schema = json.load(file)


def validate_json(data: dict, schema: dict) -> bool:
    """Валидация JSON."""
    try:
        jsonschema.validate(data, schema)
    except Exception:
        print("Ошибка валидации JSON-файла")
        exit()
    return True


validate_json(data, schema)


def create_connection(
    db_name: str, db_user: str, db_password: str, db_host: str, db_port: str
) -> psycopg2.extensions.connection:
    """Привязка к БД."""
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError:
        print("Ошибка подключения к базе данных")
        exit()
    return connection


connection = create_connection(
    "goods_account", "postgres", "123456", "localhost", "5433"
)


def execute_query(connection: psycopg2.extensions.connection, query: str) -> None:
    """Создание таблиц."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except OperationalError:
        print("Ошибка  выполнении запроса")
        exit()


create_table_goods = """CREATE TABLE IF NOT EXISTS goods
     (id SERIAL PRIMARY KEY NOT NULL,
     name TEXT NOT NULL,
     package_height REAL NOT NULL,
     package_width REAL NOT NULL)
     ;"""

create_table_shops = """CREATE TABLE IF NOT EXISTS shops_goods
     (id SERIAL PRIMARY KEY NOT NULL,
     id_good INTEGER REFERENCES goods(id),
     location TEXT NOT NULL,
     amount INT NOT NULL)
     ;"""

execute_query(connection, create_table_goods)
execute_query(connection, create_table_shops)

cursor = connection.cursor()

for key, value in data.items():
    if key == "id":
        id_good = int(value)
    if key == "name":
        name = value
    if key == "package_params":
        for k, v in value.items():
            if k == "width":
                width = v
            if k == "height":
                height = v

insert_query_goods = f"""INSERT INTO goods (id, name, package_height, package_width) VALUES
({id_good},'{name}',{width},{height})
ON CONFLICT (id) DO NOTHING;"""
cursor.execute(insert_query_goods)
connection.commit()

for key, value in data.items():
    if key == "location_and_quantity":
        for lst in value:
            for k, v in lst.items():
                if k == "location":
                    location = v
                if k == "amount":
                    amount = v
            exist_query = f"""SELECT exists (SELECT * FROM shops_goods
            WHERE id_good = {id_good} AND location = '{location}')"""
            cursor.execute(exist_query)
            row = cursor.fetchone()
            if row[0]:
                update_query_shops = f"""UPDATE shops_goods SET amount = {amount}
                                WHERE id_good = {id_good}
                                AND location = '{location}';"""
                cursor.execute(update_query_shops)
            else:
                insert_query_shops = f"""INSERT INTO shops_goods (id_good, location, amount)
                VALUES ({id_good}, '{location}',{amount});"""
                cursor.execute(insert_query_shops)

connection.commit()
