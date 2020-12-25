Тренировки и новости из мира фитнеса и бодибилдинга.(дипломный проект)

Описание:
Регистрация авторизация пользователей.
Написание статей, редактирование, удаление статей, чтение новостей.
Написание программ тренировок, редактирование, удаление, просмотр программ треннировок.
Просмотр фотографий.

РАБОЧИЙ ПОТОК :

Клонирование проекта и установка requirements.txt:

git clone https://github.com/Viachaslau95/fit_work.git

sudo pip install -r requirements.txt

Сделать миграций:

python manage.py makemigrations

python manage.py migrate

Создание Admin User:

python manage.py createsuperuser

Запуск приложение 

python manage.py runserver

