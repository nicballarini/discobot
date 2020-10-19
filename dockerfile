FROM python:3

ADD bot.py /

RUN pip install PyYAML, discord, random

CMD [ "python", "./bot.py" ]