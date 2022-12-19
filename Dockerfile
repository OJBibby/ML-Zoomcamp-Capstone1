FROM python:3.9.13

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["train.py", "service.py", "Data.csv", "./"]

RUN python "train.py"

EXPOSE 9696

ENTRYPOINT ["bentoml", "serve", "service.py:svc"]