FROM python:3.10-slim

WORKDIR /opt/simulation-service

COPY . /opt/simulation-service

RUN pip install --no-cache-dir -r runtime_dependencies.txt

EXPOSE 5000

CMD ["python", "app_service.py"]

