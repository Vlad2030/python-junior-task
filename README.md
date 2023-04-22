# Тестовое задание
Необходимо разработать REST API для ведения учета питомцев (собак и кошек).

Требуется использовать:
Python3.Х, FastAPI, SQLite (можно использовать свою fakedb на базе словаря или
класса) и Docker.

##### *P.S. Решил вместо SQlite использовать PostgreSQL + SQLALchemy, вместо обычного Docker, Docker-compose. Также в планах сделать автотесты (pytest) и миграции (alembic)*

Результат задания нужно залить на публичный git.

## API
Необходимо реализовать следующие endpoint’ы:

#### POST /pets
Создать питомца 

##### *request body*
```json
{
  // нужно спроектировать (спроектировано)
  "name": "boy",
  "age": 7,
  "type": "dog"
}
```

##### *response body*
```json
{
  "id": 1,
  "name": "boy",
  "age": 7,
  "type": "dog",
  "created_at": "2021-05-18T19:10:17"
}
```

#### GET /pets
Получить список питомцев 

##### query parameters :
  `limit: integer (optional, default=20)`

##### *response body*
```json
{
  "count": 2,
  "items": [
    {
      "id": 1,
      "name": "boy",
      "age": 7,
      "type": "dog",
      "created_at": "2021-05-18T19:10:17"
    },
    {
      "id": 2,
      "name": "girl",
      "age": 3,
      "type": "cat",
      "created_at": "2021-04-11T22:39:58"
    }
  ]
}
```


#### DELETE /pets
Удалить питомцев

##### *request body*
```json
{
  "ids": [
    1,
    2,
    3
  ]
}
```

##### *response body*
```json
{
  "deleted": 2,
  "errors": [
    {
      "id": 1,
      "error": "Pet with the matching ID was not found."
    }
  ]
}
```

## Автоматизация развертывания
Необходимо контейнеризировать полученное приложение.

Написать `Dockerfile`, который:
- скачивает базовый образ с DockerHub
- копирует приложение внутрь образа
- устанавливает необходимые пакеты и зависимости (БД, requirements.txt, и т.д.)
- производит настройку всех необходимых компонентов для работы приложения
- запускает приложение на 3000 порту

## Итог
На ПК с установленным Docker должна быть возможность склонировать
репозиторий с исходными кодами приложения.

После выполнения команд `docker build` и `docker run` приложение должно отвечать на
вызовы api по адресу `127.0.0.1:3000`
