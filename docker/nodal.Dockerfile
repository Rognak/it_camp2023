FROM python:3.11
WORKDIR /app

# Установка зависимостей
COPY ./src/requirements.txt .
COPY ./src/nodal_analysis/ ./nodal_analysis
RUN pip install -r requirements.txt
#
# Запуск приложения
CMD ["uvicorn", "nodal_analysis.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8003"]