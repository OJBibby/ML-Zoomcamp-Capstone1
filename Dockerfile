FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["train.py", "service.py", "Data.csv", "./"]

RUN python "train.py"

EXPOSE 8080

ENTRYPOINT ["bentoml", "serve", "service.py:svc"]