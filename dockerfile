FROM python:3

# RUN mkdir /src
# WORKDIR /src
COPY bot.py /
COPY config.yml /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD python bot.py