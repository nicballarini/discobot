FROM python:3

RUN mkdir /src
WORKDIR /src
ADD bot.py /src
ADD requirements.txt /src

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]