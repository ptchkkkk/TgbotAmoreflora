# Використовуємо офіційний Python-образ
FROM python:3.10-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Скопіюємо requirements.txt і встановимо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопіюємо увесь код
COPY . .

# Запускаємо твій бот
CMD ["python", "bot.py"]
