# Запуск проекта TronWalletInfo

## Создайте .env файл в корневой директории проекта со следующими переменными

| Название | Описание |
-----------|------------------------------------|
| DB_DSN | Строка подключения к БД            |
| TRON_API_KEY | Ключ для взаимодействия с TRON API |

## Запустите контейнеры

```
docker compose up -d
```

## Накатите миграции

```
docker exec -it <container_name> alembic upgrade head
```


## Дополнительно запустить тесты можно командой

```
docker exec -it <container_name> python -m pytest tests/test_api.py
docker exec -it <container_name> python -m pytest tests/test_db.py
```
