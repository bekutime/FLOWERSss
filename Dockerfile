#Какую версю питона будем  ставить , на чем ?
FROM python:3.10-alpine
#Дальше указываем рабочию директорию, у меня проект называется flowers
WORKDIR /flowers/
#Какие команды в нутри будут, и что мы еще будем в нутри этих контейнеров устонавливать
# для того что бы это сдлеать нам надо requirements.txt -скопировать
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /flowers/
# Внутри контейнера мы просто запускаем наш код -r requirements.txt
RUN pip install -r requirements.txt
# И всё наше содержимое надо скопировать внутрь нашей папки flowers
COPY . /flowers/

#Теперь у меня есть докер файл, согласно этому сценарию у меня будет создоваться image
