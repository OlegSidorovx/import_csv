# Используем базовый образ Python
FROM python:3.9

# Установка переменной среды для Python в режим отладки
ENV PYTHONUNBUFFERED 1

# Создание директории для кода
RUN mkdir /app

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей файла requirements.txt в контейнер
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего кода приложения в контейнер
COPY . /app/

# Запуск миграций и сбор статических файлов
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Определение порта, на котором будет работать приложение (замените на свой порт)
EXPOSE 8000

# Запуск приложения через Gunicorn (или другой сервер)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi:application"]
