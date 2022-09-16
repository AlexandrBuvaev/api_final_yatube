**Api_final_yatube - финальный проект Спринта 9.**
API для Yatube позволяет создавать, редактировать, удалять посты пользователей, просматривать и добавлять коменнтарии, получать информацию о сообществах и подвисываться на других пользоваетелей.

**Установка проекта**
- Клонирование репозитория:
```bash
git clone git@github.com:AlexandrBuvaev/api_final_yatube.git
cd api_final_yatube/
```
- Создание виртуального окружения и активация виртуального окружения:
```bash
Linux:
python3 -m venv venv
source venv/bin/activate
Window:
python -m venv venv
source venv\Scripts\activate
```
- Установка нужных зависимостей:
```bash
pip install -r requirements.txt
```
- Выполнение миграций и запуск проекта:
```bash
cd yatube_api/
python3 manage.py migrate
python3 manage.py runserver
```
-Документация к API доступна по адресу:
```bash
http://127.0.0.1:8000/redoc/
```
