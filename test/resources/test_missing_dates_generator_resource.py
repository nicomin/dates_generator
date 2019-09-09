import json
from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from flask import Flask
from flask_injector import FlaskInjector
from flask_restful import Api
from injector import Binder

from application.dates_application_exception import DatesApplicationException
from application.interfaces.i_missing_dates_application import IDatesApplication
from resources.missing_dates_generator_resource import MissingDatesGeneratorResource
from test.factories.time_period_dummy_factory import TimePeriodDummyFactory


class TestMissingDatesGeneratorResource(TestCase):

    def setUp(self):
        app = Flask(__name__)
        api = Api(app)
        api.default_mediatype = 'application/json'
        api.add_resource(MissingDatesGeneratorResource, '/challenge/missing-dates')
        self.app = MagicMock(IDatesApplication)

        def injector_modules(binder: Binder):
            binder.bind(IDatesApplication, self.app)

        FlaskInjector(app=app, modules=[injector_modules])
        app.testing = True
        self.client = app.test_client()

        self.endpoint = '/challenge/missing-dates'
        self.dates_generator = TimePeriodDummyFactory().create()
        self.dates_generator.output_dates = [datetime(2015, 8, 6), datetime(2016, 7, 9)]

    def test_get_when_application_exception_then_return_application_error_response(self):
        self.app.get_initial_and_missing_dates.side_effect = DatesApplicationException

        response = self.client.get(self.endpoint)
        json_response = json.loads(response.get_data(as_text=True))

        self.assertEqual(503, response.status_code)

    def test_get_when_unhandled_exception_then_return_generic_response_about_an_error(self):
        self.app.get_initial_and_missing_dates.side_effect = NameError

        response = self.client.get(self.endpoint)
        json_response = json.loads(response.get_data(as_text=True))

        self.assertEqual(500, response.status_code)

    def test_get_when_application_response_is_ok_then_return_it_as_json(self):
        self.app.get_initial_and_missing_dates.return_value = self.dates_generator

        response = self.client.get(self.endpoint)
        json_response = json.loads(response.get_data(as_text=True))

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, json_response['id'])
        self.assertEqual('1969-03-01', json_response['fechaCreacion'])
        self.assertEqual('1970-01-01', json_response['fechaFin'])
        self.assertEqual(['1969-03-01', '1969-05-01', '1969-09-01', '1970-01-01'], json_response['fechas'])
        self.assertEqual(['2015-08-06', '2016-07-09'], json_response['fechasFaltantes'])