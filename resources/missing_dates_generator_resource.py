import json

from flask import request
from flask_restful import Resource
from injector import inject

from application.interfaces.i_missing_dates_application import IMissingDatesApplication
from resources.validators.missing_dates_validator import MissingDatesValidator


class MissingDatesGeneratorResource(Resource):

    @inject
    def __init__(self, missing_dates_application: IMissingDatesApplication):
        self.missing_dates_application = missing_dates_application
        self.fields_validator = MissingDatesValidator('id', 'fechaCreacion', 'fechaFin', 'fechas')

    def post(self):
        data = json.loads(request.data)
        if not self.fields_validator.validate(data):
            return {'ERROR': 'CAMPOS DE ENTRADA INVALIDOS'}, 422

