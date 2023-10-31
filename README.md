# JazzPractice
Вэб сервис помогающий заниматься джазовым сольфеджио, после регистрации позволяет переходить на
страницу с теорией, где представленны нотные примеры всех основных джазовых аккордов с возможностью их прослушать. Так же
 есть раздел "практиковаться", где пользователю предлагается слушать и угадывать аккорды, все успехи практики
 сохраняются в личном кабинете.
# Установка
Клонируйте репозиторий на свой компьютер
```commandline
git clone https://github.com/AlbertSabirzianov/JazzPractice.git
```
Перейдите в каталог приложения
```commandline
cd Diplom
```
Установите зависимости
```commandline
pip install -r req.txt
```
Запустите миграции
```commandline
python manage.py migrate
```
Загрузите Аккорды в базу данных
```commandline
python manage.py chords_to_db
```
Запустите тестовый сервер
```commandline
python manage.py runserver
```
Пользуйтесь приложением по адресу [http://127.0.0.1:8000/main/]()
# Деплой на сервер

Клонируйте репозиторий на свой сервер
```commandline
sudo git clone https://github.com/AlbertSabirzianov/JazzPractice.git
```
Добавте файл .env в папку проекта с настройками базы данных 
```.env
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
```
Замените в файле Diplom/settings.py настройки базы данных
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}
```
Смените значение переменной DEBUG на значение False в файле Diplom/settings.py
```python
DEBUG = False
```
Запустите докер контейнеры
```commandline
sudo docker compose up
```
Приложение будет доступно по адресу [http://localhost:8000/main]()

