FROM python:3.10-slim

LABEL maintainer="Avanish Tiwari"
LABEL service="batch-simulation-engine"
LABEL environment="ci-cd"

WORKDIR /opt/simulation-engine

COPY workload/ /opt/simulation-engine/

RUN pip install --no-cache-dir -r runtime_dependencies.txt

ENTRYPOINT ["python"]
CMD ["batch-simulation-engine.py"]

