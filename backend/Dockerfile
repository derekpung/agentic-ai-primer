FROM python:3.12-slim

COPY requirements.txt /tmp

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY ./src/agent-backend .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

