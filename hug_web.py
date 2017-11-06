import hug

@hug.get('/')
def status():
	"""Devuelve estado"""
	return { "status": "OK" }
