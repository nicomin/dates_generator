from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from flask_restful_swagger import swagger

from application.dates_application import DatesApplication
from application.interfaces.i_missing_dates_application import IDatesApplication
from gateways.interfaces.i_previred_gateway import IPeriodsGateway
from gateways.periods_gateway import PeriodsGateway
from infra.interfaces.i_previred_api import IPreviredApi
from infra.previred_api import PreviredApi
from resources.missing_dates_generator_resource import MissingDatesGeneratorResource


def app_endpoints(api):
    api.add_resource(MissingDatesGeneratorResource, '/challenge/missing-dates')


def bind_modules(binder):
    binder.bind(IDatesApplication, DatesApplication)
    binder.bind(IPeriodsGateway, PeriodsGateway)
    binder.bind(IPreviredApi, PreviredApi)


def create_app():
    app = Flask(__name__)

    api = swagger.docs(Api(app), apiVersion='0.1')
    app_endpoints(api)

    FlaskInjector(app=app, modules=[bind_modules])

    return app


application = create_app()

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=5002, debug=True)
