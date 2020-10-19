FROM python:3

ADD bot.py /

RUN pip install pyyaml, discord, random

CMD [ "python", "./bot.py" ]