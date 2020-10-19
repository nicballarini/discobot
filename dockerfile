FROM python:3.8

EXPOSE 5942

RUN apt-get update && \
    apt-get install -y --no-install-recommends libc-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd appuser && chown -R appuser /app
USER appuser

CMD [ "python", "/app/bot.py" ]
