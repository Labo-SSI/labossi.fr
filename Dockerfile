FROM python:3.13-bookworm

WORKDIR /app

RUN groupadd flask && useradd -r -g flask flask

COPY . /app
RUN chown -R flask:flask /app

RUN pip install --no-cache-dir -r requirements.txt

USER flask

EXPOSE 5000

ENV FLASK_APP=src/app
CMD ["flask", "run", "--host=0.0.0.0"]
