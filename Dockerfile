FROM python:3.10-slim-bullseye

RUN mkdir /app

COPY ./app /app

COPY ./requirements.txt /app/.

WORKDIR /app

RUN pip install -r requirements.txt

RUN python3 manage.py makemigrations api
RUN python3 manage.py migrate

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]