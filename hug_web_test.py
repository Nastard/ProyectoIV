# -*- coding: utf-8 -*-
import hug
import hug_web

def test_estado_OK():
    estado = hug.test.get(hug_web, '/')
    assert estado.status == "200 OK"
    assert estado.data['status']=="OK"
