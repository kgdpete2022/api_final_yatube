# API проекта Yatube (v1)

#### Описание

API-сервис проекта yatube, позволяющий пользователям получать информацию о постах (включая дополнительную информацию - группы, авторы, подписки)

#### Установка

Клонировать репозиторий:

```
git clone git@github.com:kgdpete2022/api_final_yatube.git
```

Перейти в корневой каталог:

```
cd kittygram_backend
```

Cоздать виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:

- Linux/macOS

```
source venv/bin/activate
```

- Windows

```
source venv/scripts/activate
```

Обновить pip:

```
python3 -m -pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Примеры запросов к API

Получение списка всех публикаций:

```
GET /api/v1/posts/
```

Добавление новой публикации в коллекцию публикаций

```
POST /api/v1/posts/
```

Получение публикации по id:

```
GET /api/v1/posts/{id}/
```
