FROM python:3

ADD bot.py /

RUN pip install yaml, discord, random

CMD [ "python", "./bot.py" ]