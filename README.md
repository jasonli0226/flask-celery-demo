# flask-celery-demo

Flask -> RabbitMQ -> Celery

&nbsp;

## Setup

```bash
pip install -r requirements.txt

```

## Command

```bash
gunicorn -b localhost:8000 -w 4 app:flask_app
celery -A app.celery worker --loglevel=info

```

