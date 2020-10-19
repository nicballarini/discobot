FROM python:3

RUN mkdir /src
WORKDIR /src
COPY bot.py /src
COPY config.yml /src
COPY requirements.txt /src

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]