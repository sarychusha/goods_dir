# goods_dir
Домашнее задание на тему "Словари"

Учёт товаров

Вы делаете приложение по учёту товаров на складе.

В организации, для которой вы делаете приложение есть готовые системы. Одна собирает данные по одному отдельному товару. Другая - собирает данные из таблиц для предоставления их в удобном виде на сайте.

Ваша задача — сделать систему, связывающую эти две системы.

Разработчики системы, которая собирает данные по товарам выдали вам формат данных которые они готовы отдавать в виде json-схемы.

В свою очередь, разработчики системы, отображающей данные для сайта предоставили схему таблиц, с которой они готовы работать.

От вас требуется предоставить прототип приложения, которое бы выполняло задачу сохранения данных в таблицу.

Нужно принимать json и записывать строки в таблицы БД.


Требования:
В качестве входных параметров программа получает файл json.
Происходит валидация входных данных.
Приложение должно уметь сохранять в базу в  две таблицы.
Приложение создаёт таблицы если они не созданы.
Приложение только вставляет данные, но не делает удаления.
Если пришли новые данные по предмету уже имеющемуся в базе — обновить.
Использовать либо sqlite3 либо postgre для хранения данных.

Разрешается:
Использовать сторонние библиотеки

Не разрешается:
Списывать у других студентов
Изменять приложенные схемы

Требования к качеству кода:
Формат кода соответствует pep8
Проверка: flake8 --max-line-length=120 .

Формат докстрингов соответствует pep 257
Проверка: pep257 . 

Формат аннотаций соответствует pep 484
Проверка: mypy . --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs --check-untyped-defs  --disallow-untyped-decorators --ignore-missing-imports --pretty

Если в проекте используются сторонние библиотеки — они все указаны в файле requirements.txt вместе с версиями

Отсутствует мертвый код
Проверка:  vulture . --min-confidence 70

В вашем решении должен присутствовать tox.ini запускающий автоматические проверки качества кода

В вашем решении должен присутствовать хотя бы одн тест, написанный с помощью модуля unittest

