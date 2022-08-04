# flask-celery-demo

Flask -> RabbitMQ -> Celery

## Setup

```bash
pip install -r requirements.txt

```

&nbsp;

## Command

```bash
gunicorn -b localhost:8000 -w 4 app:flask_app
celery -A app.celery worker --loglevel=info

```

&nbsp;