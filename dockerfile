FROM python:3

RUN mkdir /src
WORKDIR /src
ADD bot.py /
ADD requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]