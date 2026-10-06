# hash-service

![CI/CD](https://github.com/arc-10/hash-service/actions/workflows/ci.yml/badge.svg)

REST API на Flask для вычисления и проверки хешей (md5, sha1, sha256, sha512).

СРО № 1 по дисциплине «Прикладные аспекты DevOps», вариант 42.

## API

| Метод | Путь | Тело запроса | Ответ |
|---|---|---|---|
| GET | `/health` | — | `{"status": "ok"}` |
| POST | `/hash` | `{"text": "abc", "algorithm": "sha256"}` | `{"algorithm": "sha256", "hash": "..."}` |
| POST | `/verify` | `{"text": "abc", "hash": "...", "algorithm": "sha256"}` | `{"match": true}` |

`algorithm` можно не указывать, по умолчанию sha256.

## Запуск

```
pip install -e .
flask --app hash_service.app run
```

## Тесты и линтер

```
pip install -r requirements-dev.txt
pytest -v --cov=hash_service
ruff check .
```

## CI/CD

GitHub Actions, файл `.github/workflows/ci.yml`: lint и test → build → deploy в окружение test.
