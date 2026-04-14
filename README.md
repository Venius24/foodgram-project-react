# Foodgram — Социальная сеть для кулинаров

***14.04.26 РАБОТАЕТ ПО АДРЕСУ***
# https://venius24.ddns.net/

Современный веб-сервис для обмена рецептами с функциями соцсети: подписки, лайки, списки покупок и персональная лента.

![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-FF4757?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-1.19-232F3E?style=for-the-badge&logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 🚀 Быстрый запуск (Docker)

### Предварительные требования
- Docker
- Docker Compose
- Доменное имя (например, `venius24.ddns.net`)
- Открытые порты 80 и 443

### 1. Подготовка окружения
Создайте файл `.env` в корне проекта:

```bash
cp .env.example .env
```

Заполните переменные:
```bash
# .env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=foodgram
DB_USER=foodgram_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432

SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=venius24.ddns.net,localhost,[IP_ADDRESS]

# Настройки Let's Encrypt
EMAIL=your-email@example.com
```

### 2. Запуск
```bash
# Собрать и запустить все сервисы
docker compose up -d --build

# Применить миграции
docker compose exec backend python manage.py migrate

# Создать суперпользователя (если нужно)
docker compose exec backend python manage.py createsuperuser
```

### 3. Получение SSL-сертификата
```bash
# Создать папку для сертификатов
mkdir -p infra/data/certbot/conf

# Запустить Certbot (введите ваш email и согласитесь с условиями)
docker compose run --rm certbot certonly --webroot -w /var/www/certbot \
  -d venius24.ddns.net \
  --email [EMAIL_ADDRESS] \
  --agree-tos \
  --no-eff-email

# Перезапустить Nginx для применения сертификата
docker compose restart nginx
```

## 🛠️ Структура проекта

```
foodgram/
├── backend/              # Django-приложение
│   ├── api/              # REST API
│   ├── recipes/          # Модуль рецептов
│   ├── users/            # Модуль пользователей
│   ├── recipes/          # Модуль рецептов
│   └── ...
├── frontend/             # React-приложение
├── infra/                # Инфраструктура
│   ├── docker-compose.yml  # Конфигурация Docker
│   ├── nginx.conf        # Конфигурация Nginx
│   └── .env.example      # Шаблон переменных окружения
├── .github/workflows/    # GitHub Actions
└── README.md
```

## 📋 Технологии

### Backend
- **Django 4.2** — фреймворк
- **Django REST Framework** — API
- **PostgreSQL 16** — база данных
- **JWT** — аутентификация
- **Celery** — фоновые задачи
- **Redis** — брокер сообщений

### Frontend
- **React 18** — UI-библиотека
- **Redux Toolkit** — управление состоянием
- **React Router** — навигация
- **Axios** — HTTP-клиент

### Инфраструктура
- **Docker** — контейнеризация
- **Docker Compose** — оркестрация
- **Nginx** — reverse proxy
- **Let's Encrypt** — SSL-сертификаты

## 🔐 Безопасность

### Аутентификация
- JWT-токены (access и refresh)
- Хеширование паролей (pbkdf2_sha256)
- Защита от CSRF и XSS

### SSL/TLS
- Автоматическое получение сертификатов Let's Encrypt
- HTTPS на всех эндпоинтах
- HSTS-заголовки

## 🔄 Автоматизация

### CI/CD (GitHub Actions)
Автоматическое развертывание при пуше в ветку `production`:
1. Checkout кода
2. SSH-подключение к серверу
3. Pull изменений
4. Пересборка Docker-контейнеров
5. Применение миграций
6. Очистка старых образов

## 📝 API

### Основные эндпоинты
- `GET /api/` — список рецептов
- `GET /api/recipes/{id}/` — детали рецепта
- `POST /api/recipes/` — создание рецепта
- `GET /api/users/{username}/` — профиль пользователя
- `POST /api/auth/token/` — получение токена
- `POST /api/auth/token/refresh/` — обновление токена

### Документация
- **Swagger UI**: http://venius24.ddns.net/api/docs/
- **ReDoc**: http://venius24.ddns.net/api/docs/redoc/

## 📂 Структура папок

### Backend
```
backend/
├── api/                # API-эндпоинты
├── recipes/            # Модуль рецептов
│   ├── models.py       # Модели (Recipe, Ingredient, RecipeIngredient)
│   ├── serializers.py  # Сериализаторы
│   └── views.py        # Вьюсеты
├── users/              # Модуль пользователей
│   ├── models.py       # Модели (User, Follow)
│   ├── serializers.py  # Сериализаторы
│   └── views.py        # Вьюсеты
├── recipes/            # Модуль рецептов
│   ├── models.py       # Модели (Recipe, Ingredient, RecipeIngredient)
│   ├── serializers.py  # Сериализаторы
│   └── views.py        # Вьюсеты
├── recipes/            # Модуль рецептов
│   ├── models.py       # Модели (Recipe, Ingredient, RecipeIngredient)
│   ├── serializers.py  # Сериализаторы
│   └── views.py        # Вьюсеты
└── ...
```

### Frontend
```
frontend/
├── src/
│   ├── components/     # React-компоненты
│   ├── pages/          # Страницы приложения
│   ├── store/          # Redux-хранилище
│   ├── api/            # API-клиент
│   └── ...
└── ...
```

## 🚀 Развертывание

### Локальное развертывание
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
npm install
npm start
```

### Production
```bash
# Обновить код
git pull origin production

# Пересобрать и запустить
docker compose up -d --build

# Применить миграции
docker compose exec backend
