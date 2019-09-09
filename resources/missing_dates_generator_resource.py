from flask_restful import Resource, marshal, fields, marshal_with
from flask_restful_swagger import swagger
from injector import inject

from application.dates_application_exception import DatesApplicationException
from application.interfaces.i_missing_dates_application import IDatesApplication
from resources.marshal_utils import DateField
from resources.swagger.missing_dates_generator_docs import MISSING_DATES_GENERATOR_DOC


@swagger.model
class MissingDatesResourceFields:

    resource_fields = {
        'id': fields.Integer,
        'fechaCreacion': fields.String(attribute='begin_date'),
        'fechaFin': fields.String(attribute='end_date'),
        'fechas': fields.List(DateField, attribute='input_dates'),
        'fechasFaltantes': fields.List(DateField, attribute='output_dates')
    }


class MissingDatesGeneratorResource(Resource):
    """Llama a la aplicación GDD y trae todas las fechas para un periodo de tiempo determinado por esta aplicación. """
    """Las fechas que ya han sido obtenidas desde la aplicación no son generadas nuevamente """

    @inject
    def __init__(self, missing_dates_application: IDatesApplication):
        self.missing_dates_application = missing_dates_application

    @swagger.operation(**MISSING_DATES_GENERATOR_DOC)
    @marshal_with(MissingDatesResourceFields.resource_fields)
    def get(self):
        try:
            result = self.missing_dates_application.get_initial_and_missing_dates()
        except DatesApplicationException as e:
            return {'ERROR': 'Error generando las fechas'}, 503
        except Exception as e:
            return {'ERROR': 'Error no controlado'}, 500
        else:
            return result
