# test_workmate

Проект FastAPI
Описание
Это проект API на основе FastAPI, который запускается в Docker-контейнере. Он использует Alembic для управления миграциями базы данных и включает автоматический запуск парсера при старте контейнера.

Скопируйте проект:
git clone https://github.com/Cryptodirector/test_workmate.git

Перейдите в папку с проектом:
cd test_workmate

В корневой директории вашего проекта создайте файл .env

Скопируйте и вставьте в него следующий шаблон переменных окружения:

POSTGRES_HOST="IP сервера"
POSTGRES_PORT=5432
POSTGRES_USER="Логин"
POSTGRES_PASSWORD="Пароль"
POSTGRES_DB="Название базы"

TEST_POSTGRES_USER="Логин"
TEST_POSTGRES_PASSWORD="Пароль"
TEST_POSTGRES_HOST="IP сервера"
TEST_POSTGRES_PORT=5433
TEST_POSTGRES_DB="Название базы"

Запустите:
docker compose up --build

Готово! 🔥🔥🔥 
