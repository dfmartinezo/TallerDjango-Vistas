import variables.logic.variables_logic
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mes_pk):
    measurement = Measurement.objects.get(pk=mes_pk)
    return measurement

def update_measurement(mes_pk, new_mes):
    measurement = get_measurement(mes_pk)
    measurement.variable = variables.logic.variables_logic.get_variable(new_mes["variable"])
    measurement.value = new_mes["value"]
    measurement.unit = new_mes["unit"]
    measurement.place = new_mes["place"]
    measurement.save()
    return measurement

def create_measurement(mes):
    measurement = Measurement(variable=variables.logic.variables_logic.get_variable(mes["variable"]), value=mes["value"], unit=mes["unit"], place=mes["place"], dateTime=mes["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(mes_pk):
    measurement = Measurement.objects.get(pk=mes_pk)
    measurement.delete()
    return measurement