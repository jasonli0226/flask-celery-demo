import time
from flask import Flask, jsonify, make_response
from celery import Celery


def make_celery(app):
  celery = Celery(
      app.import_name,
      broker=app.config['CELERY_BROKER_URL']
  )
  celery.conf.update(app.config)

  class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
      with app.app_context():
        return self.run(*args, **kwargs)

  celery.Task = ContextTask
  return celery


flask_app = Flask(__name__)
flask_app.config.update(
    JSON_AS_ASCII=False,
    CELERY_BROKER_URL="amqp://guest@localhost//",
)
celery = make_celery(flask_app)

API_VERSION = "/api"


@flask_app.route(f"{API_VERSION}/greeting", methods=["GET"])
def greeting():
  add_together.delay(10, 15)
  return jsonify(status="OK")


@flask_app.errorhandler(404)
def method_not_allowed(e):
  return make_response(jsonify(message="404 Not Found"), 404)


@flask_app.errorhandler(405)
def method_not_allowed(e):
  return make_response(jsonify(message="Method Not Allowed"), 405)


@flask_app.errorhandler(Exception)
def internal_error(error):
  print(error)
  return make_response(jsonify(message="Internal Server Error"), 500)


if __name__ == "__main__":
  flask_app.run(debug=True, host="0.0.0.0")


@celery.task()
def add_together(a, b):
  # sleep 5 second
  time.sleep(5)
  print(a + b)
