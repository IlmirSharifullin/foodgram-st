# Foodgram - Портал рецептов блюд от разных пользователей 😋

## Запуск проекта

### Требования
- Docker Compose

### 1. Клон репозитория
```bash
git clone https://github.com/IlmirSharifullin/foodgram-st.git
cd foodgram-st
```

### 2. Настройка окружения
```bash
# .env
POSTGRES_USER=postgres
POSTGRES_DB=foodgram
POSTGRES_PASSWORD=12345
DB_PORT=5432
DB_HOST=db
```

### 3. Запуск контейнеров
```bash
docker-compose up --build
```

### 4. Заполнение базы данных
```bash
docker exec -it foodgram-backend python manage.py loaddata data/fill_db.json
```
