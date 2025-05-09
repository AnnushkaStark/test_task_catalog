# test_task_catalog

## Необходимо использовать следующие инструменты и технологии:

* Python (3.10+)
* FastAPI
* PostgreSQL или SQLite
    SQLAlchemy


## Необходимо реализовать API для каталога товаров со следующими endpoint-ами:

* GET /catalog/ - постраничный      вывод  списка товаров с поиском/фильтрацией

* GET /catalog/filter/ - вывод параметров для фильтрации

* GET /product/{UID} - информация о товаре

* POST /product/ - добавление товара

* DELETE /product/{UID} - удаление товара

* POST /properties/ - добавление свойства

* DELETE /properties/{UID} - удаление свойства


## Реализация

доступные энпонты

* GET property_types - получение свойст продукта (параметров для фильтрации)

Доступные свойтсва:

- COLOR - str
- MEMORY_SIZE - str
- HIGHT - int

каждый продукт может иметь одно или несколько свойств каждого типа

* POST create_propery - создание свойства (указывается тип свойста котрое создается и value (значение свойства в str))

* GET properties - списка свойств с фильтацией по типу (цвет/объем памяти/высота)

* GET property - получение свойства по uid

* DELETE propery - удаление свойства по uid

* POST - создание продукта

* GET products - получение списка продуктов с возможностью поиска по названию и фильтрацией по свойству и пагинацией

* GET product - получение продукта по uid

* DELETE product - удаление продукта по uid

Так же для проверки работы доступны эндпонйты для генерации тестовых данных

* GET test_data properties - создание набора свойств
* GET test_data products - создание набора продуктов

## Запуск проекта

1. Создать в корневой директории файл .env

2. Скрпировать в .env натройки для базы данных из файла .env.template

3. Из корневой директории запустить проект командой

```
docker-compose up --build
```
