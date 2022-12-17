# Yatube project API (v1)

#### Description

API service of the yatube project, allowing users to receive information about posts (including additional information - groups, authors, subscriptions)

#### Installation

Clone repository:

```
git clone git@github.com:kgdpete2022/api_final_yatube.git
```

Go to root directory:

```
cd api_final_yatube
```

Create virtual environment:

```
python3 -m venv env
```

Activate virtual environment:

- Linux/macOS

```
source venv/bin/activate
```

-Windows

```
source venv/scripts/activate
```

Update pip:

```
python3 -m -pip install --upgrade pip
```

Install dependencies from requirements.txt file:

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

Run project:

```
python3 manage.py runserver
```

#### API request examples

Getting a list of all publications:

```
GET /api/v1/posts/
```

Adding a new publication to the collection of publications

```
POST /api/v1/posts/
```

Getting a publication by id:

```
GET /api/v1/posts/{id}/
```