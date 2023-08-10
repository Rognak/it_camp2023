FROM python:3.11
WORKDIR /app

# Установка зависимостей
COPY ./src/requirements.txt .
COPY ./src/vlp/ ./vlp
RUN pip install -r requirements.txt
#
# Запуск приложения
CMD ["uvicorn", "vlp.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]