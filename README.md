# astrosoft_pro_test

## 1. Запуск проекта

```
cp .env.example .env
docker-compose up --build
make dmigr
```

## 2. Создание пользователя

```
make duser
```

## 3. Запуск тестов

```
make dtest
```
