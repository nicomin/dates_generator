from entities.time_period import TimePeriod

MISSING_DATES_GENERATOR_DOC = {
    'notes': 'Api de prueba. Postulación Previred',
    'responseClass': TimePeriod.__name__,
    'nickname': 'DesafioUno',
    'parameters': [],
    'responseMessages': [
        {
            "code": 200,
            "message": "Exitoso. Se obtienen las fechas mediante la aplicación GDD y se añaden las que faltan para el periodo."
        },
        {
            "code": 506,
            "message": "Error controlado."
        },
        {
            "code": 500,
            "message": "Error no controlado."
        }
    ]
}
