FROM python:3.12-slim

COPY requirements.txt /tmp

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY ./src/streamlit-primer/ .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
