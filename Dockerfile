FROM python:3-slim

WORKDIR /opt/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py gunicorn_config.py init.py ./

RUN python init.py

EXPOSE 80

#
CMD ["gunicorn","--config", "gunicorn_config.py", "app:app"]