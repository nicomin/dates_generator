from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api

from resources.missing_dates_generator_resource import MissingDatesGeneratorResource


def app_endpoints(api):
    api.add_resource(MissingDatesGeneratorResource, '/challenge/missing-dates')


bindings_modules = []


def create_app(config: object = None):
    app = Flask(__name__)

    api = Api(app)
    app_endpoints(api)

    FlaskInjector(app=app, modules=bindings_modules)

    return app
