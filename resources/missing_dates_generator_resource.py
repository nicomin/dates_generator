from flask_restful import Resource, marshal, fields
from injector import inject

from application.dates_application_exception import DatesApplicationException
from application.interfaces.i_missing_dates_application import IMissingDatesApplication
from resources.marshal_utils import DateField


class MissingDatesGeneratorResource(Resource):
    missing_dates_fields = {
        'id':  fields.Integer,
        'fechaCreacion': fields.String(attribute='begin_date'),
        'fechaFin': fields.String(attribute='end_date'),
        'fechas': fields.List(fields.String, attribute='input_dates'),
        'fechasFaltantes': fields.List(DateField, attribute='output_dates')
    }

    @inject
    def __init__(self, missing_dates_application: IMissingDatesApplication):
        self.missing_dates_application = missing_dates_application

    def get(self):
        try:
            result = self.missing_dates_application.get_initial_and_missing_dates()
        except DatesApplicationException:
            return {'ERROR': 'Error generando las fechas'}, 503
        except Exception:
            return {'ERROR': 'Error no controlado'}, 500
        else:
            return marshal(result, self.missing_dates_fields)
