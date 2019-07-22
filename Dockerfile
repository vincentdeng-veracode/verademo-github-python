FROM python:3.6.6

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src verademo/

WORKDIR verademo

RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 80

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]
