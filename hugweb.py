import hug
from botQueToca.QueTocaBBDD import Horario

horario=Horario()

@hug.get('/')
def status():
	"""Devuelve estado"""
	return { "status": "OK" }

# @hug.get('/horario')
# def actividades_bd():
# 	info = horario.LeerHorario(1)
# 	return { "Horario": info }
