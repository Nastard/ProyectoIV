# ProyectoIV, Bot de Telegram QueToca
[![Build Status](https://travis-ci.org/Anixo/ProyectoIV.svg?branch=master)](https://travis-ci.org/Anixo/ProyectoIV)  
>Proyecto a desarrollar de la asignatura Infraestructura Virtual.  
Se puede consultar en [este enlace](https://anixo.github.io/ProyectoIV/).

# Descripción
Se va a desarrollar un bot de Telegram que al preguntarle nos dira el horario que nos corresponde.  
En un principio solo funcionará para alumnos del **grado de Ingeniería Informática**  
También nos dira el profesor correspondiente a la asignatura.  
Deberemos saber el curso y el grupo del usuario.  
Nos dirá también la asignatura actual en la que se encuentra el alumno.  


# Desarrollo
Hemos usado lenguaje Python y la API de Telegram. Se tendrá en cuenta para el desarrollo de este bot la API de un calendario realizada por un compañero (SCRUM).  
Usaremos un sistemas de test y de integración continua, que se detalla más adelante.   
Como todavía no disponemos de una BBDD, usamos el archivo *horario.json* para realizar los tests.  

# Sistema de test y Integración continua
Hemos usado el sistema de test de Python, `unittest`, y TravisCI para la integración continua, encargado de ejecutar estos test. Cuando se modifique el código del repositorio, se comprueba que el codigo generado sigue funcionando de manera correcta, verificando su integración.  
El archivo `QueToca_test.py`, dentro de la carpeta *botQueToca*, tiene desarrollados los test unitarios de las funciones de la biblioteca del bot.

# Requisitos:
Debemos instalar:  
~~~
sudo apt-get install python  
sudo apt-get install python-pip  
sudo pip install -r requirements.txt
~~~
