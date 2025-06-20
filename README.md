# Тестовое задание — Tetrika (Junior Python Developer)

## 📦 Состав проекта

Репозиторий содержит решение трёх задач:

| Задача | Описание |
|--------|----------|
| `task1` | Декоратор `@strict`, проверяющий соответствие типов аргументов аннотациям |
| `task2` | Скрипт для парсинга Википедии и подсчёта количества животных по алфавиту |
| `task3` | Расчёт общего времени одновременного присутствия ученика и преподавателя на уроке |

---

## 🚀 Как запустить

### 1. Установка окружения

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Запуск тестов

```bash
pytest
```

Тесты лежат в:
- `task1/test_solution.py`
- `task2/test_solution.py`
- `task3/test_solution.py`

---

## 📂 Содержимое

```
tetrika-junior-test/
├── task1/
│   ├── solution.py
│   └── test_solution.py
├── task2/
│   ├── solution.py
│   └── test_solution.py
├── task3/
│   ├── solution.py
│   └── test_solution.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Используемые библиотеки

- `pytest` — для тестирования
- `requests` + `beautifulsoup4` — для парсинга в `task2`

---

## 📎 Автор

Jahongir Mirhalikov  
GitHub: [@JahongirM98](https://github.com/JahongirM98)