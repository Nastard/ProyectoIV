# -*- coding: utf-8 -*-
import hug
import hugweb

def test_estado_OK():
    estado = hug.test.get(hugweb, '/')
    assert estado.status == "200 OK"
    assert estado.data['status']=="OK"
