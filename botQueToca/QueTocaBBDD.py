# -*- coding: utf-8 -*-
import json
import os
import psycopg2

class Horario:
	"""Clase que gestiona las horas de clase"""

	def __init__(self):
		self.basedatos = os.environ["DATABASE"]
		self.user = os.environ["USER"]
		self.password = os.environ["PASSWD"]
		self.host = os.environ["HOST"]

		try:
			with open('./horario.json') as datos:
				self.horario = json.load(datos)
		except IOError as fallo:
			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)

	def ConexionABaseDatos(self):
		conexion = psycopg2.connect(database=self.basedatos, user=self.user, password=self.password, host=self.host)
		return conexion

	def CrearHorario(curso=None, grupo=None, asignatura=None, hora_inicio=None, hora_fin=None, fecha=None, aula=None, profesor=None):
		curso = 4
		if curso > 5 or curso < 0:
			raise IndexError("Error en el numero de curso.")

		datos = {
			"id": "D5",
			"curso": curso,
			"grupo": "C",
			"asignatura": "Infraestructura Virtual",
			"dia_semana": "Jueves",
			"aula": "-1.2",
			"hora_inicio": "09:30",
			"hora_fin": "10:30",
			"profesor": "JJ"
		}
		try:
			with open('./nuevo_horario.json', 'w') as nuevo:
				json.dump(datos, nuevo)
				return True
		except IOError as fallo:
			print("Error %d escribiendo nuevo_horario.json: %s", fallo.errno, fallo.strerror)

	def LeerHorario(self, identificador=None):
		conn = self.ConexionABaseDatos()
		cur = conn.cursor()
		cur.execute("SELECT * FROM horario WHERE id=\'"+str(identificador)+"\'")
		cur.execute("SELECT profesor FROM horario WHERE asignatura=\'"+str(asignatura)+"\'")
		info = cur.fetchall()
		conn.close()
		cur.close()
		return str(info)

	def ModificarHorario(nuevo_id=None, nuevo_curso=None, nuevo_grupo=None, nueva_asignatura=None,
						 nueva_hora_inicio=None, nueva_hora_fin=None, nuevo_dia_semana=None, nuevo_aula=None, nuevo_profesor=None):
		try:
			with open('./horario.json') as datos:
				horario_modificado = json.load(datos)
		except IOError as fallo:
			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)

		nuevo_id = "D32"
		if nuevo_id != None:
			horario_modificado["hora_inicio"] = nuevo_id

		nuevo_curso = 3
		if nuevo_curso == None or nuevo_curso > 5 or nuevo_curso < 0:
			horario_modificado["curso"] = horario_modificado["curso"]
		else:
			horario_modificado["curso"] = nuevo_curso

		nuevo_grupo = "B"
		if nuevo_grupo != None:
			horario_modificado["grupo"] = nuevo_grupo

		nueva_asignatura = "DDSI"
		if nueva_asignatura != None:
			horario_modificado["asignatura"] = nueva_asignatura

		nueva_hora_inicio = None
		if nueva_hora_inicio != None:
			horario_modificado["hora_inicio"] = nueva_hora_inicio

		if nueva_hora_fin != None:
			horario_modificado["hora_fin"] = nueva_hora_fin

		if nuevo_dia_semana != None:
			horario_modificado["dia_semana"] = nuevo_dia_semana

		if nuevo_aula != None:
			horario_modificado["aula"] = nuevo_aula

		if nuevo_profesor != None:
			horario_modificado["profesor"] = nuevo_profesor

		try:
			with open('./horario.json', 'w') as modificado:
				json.dump(horario_modificado, modificado)
				return True
		except IOError as fallo:
			print("Error %d escribiendo horario.json: %s", fallo.errno, fallo.strerror)

	def BorrarHorario(curso=None, grupo=None, asignatura=None):
		try:
			with open('./horario.json') as datos:
				horario_a_borrar = json.load(datos)
		except IOError as fallo:
			print("Error %d leyendo horario.json: %s", fallo.errno, fallo.strerror)
		# Implementado borrar
		horario_a_borrar["id"] = "null"
		horario_a_borrar["curso"] = "null"
		horario_a_borrar["grupo"] = "null"
		horario_a_borrar["asignatura"] = "null"
		horario_a_borrar["hora_inicio"] = "null"
		horario_a_borrar["hora_fin"] = "null"
		horario_a_borrar["dia_semana"] = "null"
		horario_a_borrar["aula"] = "null"
		horario_a_borrar["profesor"] = "null"

		try:
			with open('./horario.json', 'w') as borrado:
				json.dump(horario_a_borrar, borrado)
				return True
		except IOError as fallo:
			print("Error %d escribiendo horario.json: %s", fallo.errno, fallo.strerror)

	def ProfesorAsignatura(self, asignatura=None):
		conn = self.ConexionABaseDatos()
		cur = conn.cursor()
		cur.execute("SELECT profesor FROM horario WHERE asignatura=\'"+str(asignatura)+"\'")
		info = cur.fetchall()
		conn.close()
		cur.close()
		return str(info)

	def MisAsignaturas(self):
		conn = self.ConexionABaseDatos()
		cur = conn.cursor()
		cur.execute("SELECT asignatura FROM horario")
		info = cur.fetchall()
		conn.close()
		cur.close()
		return str(info)

	def MiDia(self, dia=None):
		conn = self.ConexionABaseDatos()
		cur = conn.cursor()
		cur.execute("SELECT * FROM horario WHERE dia_semana=\'"+str(dia)+"\'")
		info = cur.fetchall()
		conn.close()
		cur.close()
		return str(info)
