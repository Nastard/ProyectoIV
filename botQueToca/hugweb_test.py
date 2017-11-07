import hug
import hugweb

def test_estado_OK():
    datos = hug.test.get(hugweb, '/')
    assert datos.status == "200 OK"
    assert datos.data['status']=="OK"

def test_ruta_correcta():
    datos = hug.test.get(hugweb, '/horario')
    assert datos.status == "200 OK"
    assert datos.data['Horario'] == "[(4, 'A', 'Infraestructura virtual', datetime.date(2016, 11, 6), -1.2, datetime.time(9, 30), datetime.time(11, 30), 'JJ')]"
