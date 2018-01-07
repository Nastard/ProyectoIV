# ProyectoIV, Bot de Telegram QueToca
[![Build Status](https://travis-ci.org/Anixo/ProyectoIV.svg?branch=master)](https://travis-ci.org/Anixo/ProyectoIV) [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Anixo/ProyectoIV)
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

# Sistema de test e Integración continua
Hemos usado el sistema de test de Python, `unittest`, y TravisCI para la integración continua, encargado de ejecutar estos test. Cuando se modifique el código del repositorio, se comprueba que el codigo generado sigue funcionando de manera correcta, verificando su integración.  
El archivo `QueToca_test.py`, dentro de la carpeta *botQueToca*, tiene desarrollados los test unitarios de las funciones de la biblioteca del bot.

# Requisitos:
Debemos instalar:  
~~~
$ sudo apt-get install python  
$ sudo apt-get install python-pip  
$ pip install -r requirements.txt
~~~

# Desarrollo del PaaS
Hemos desplegado el PaaS en Heroku por tener bastantes servicios básicos y de manera gratuita, además de ofrecer una gran cantidad de herramientas.  

Para poder desplegar la aplicación debemos instalar Heroku y ejecutar el siguiente comando para estar logueados:  
~~~
$ heroku login
~~~

Una vez logueados, ejecutamos el siguiente comando para crear la aplicación en Heroku:  
~~~
$ heroku create
~~~

Nuestra aplicacion de Heroku consta de dos dynos, una para el bot y otra para un servicio web, así que debemos configurar de forma correcta el archivo `Procfile` para que tenga en cuenta estas dos aplicaciones.  

En Heroku hemos añadido la base de datos PostgreSQL, para que el bot tenga una funcionalidad mínima que devolver. Esto se puede hacer desde el dashboard de Heroku en el navegador.  

Se han definido también variables de entorno para el TOKEN del Bot y para las datos de conectividad de la base de datos creada.

Ahora lanzamos los dos dynos especificados en `Procfile` con el comando:  
~~~
$ heroku ps:scale worker=1 web=1
~~~

Se ha configurado Heroku para que cada vez que se realice un push en el repositorio, Heroku lo tiene en cuenta y se despliega automáticamente despúes de pasar los test de integración continua:
![imagen](https://github.com/Anixo/EjerciciosIV/blob/master/Imagenes/heroku.png)  

Podemos probar que el servicio web funciona ejecutando  
~~~
$ heroku open
~~~
y viendo que devuelve `status: OK`  
También se puede visitar las rutas siguientes:
* https://iv-anixo.herokuapp.com/horario

La funcionalidad del bot se puede hacer diciéndole el comando `/horario`. El bot se llama @QueTocaBot.

Despliegue https://iv-anixo.herokuapp.com/

# Desarrollo en Docker
Instalamos Docker usando su [guía oficial](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository).  
Si ejecutamos el siguiente comando crearemos la imagen de la aplicación:
~~~
$ sudo docker pull anixo/proyectoiv
~~~
Y si ejecutamos el siguiente comando entraremos dentro del contenedor:
~~~
$ sudo docker run -it anixo/proyectoiv /bin/bash
~~~
Para ver que devuelve un `status: OK` basta con ejecutar:
~~~
$ hug -p 80 -f ./botQueToca/hugweb.py &
$ curl localhost:80/status
~~~

# Docker Hub
Hemos creado una cuenta en Docker Hub y la hemos linkeado con GitHub para que coja el repositorio del Proyecto. Esta actualizado de forma automática con el repositorio:  
![imagen](https://github.com/Anixo/EjerciciosIV/blob/master/Imagenes/dockerhub.png)  
URL de Docker Hub: https://hub.docker.com/r/anixo/proyectoiv/

# Desarrollo en Zeit
Contenedor: https://proyectoiv-frymrirpfw.now.sh/  

Debemos instalar **npm** y luego ejecutar el siguiente comando para instalar now:  
~~~
$ npm install -g now
~~~
Tras ello, si ejecutamos el siguiente comando se despliega automáticamente y nos genera un enlace como el de arriba (Puede que la primera vez nos pida un login, en el cual solo hay que darse de alta):  
~~~
$ now --public
~~~

# Desarrollo en Azure
Para el despliegue de la aplicacion en Azure, debemos instalar los siguientes paquetes básicos:  
~~~
$ sudo apt-get update && sudo apt-get install -y python libssl-dev libffi-dev python-dev build-essential
~~~
Instalamos el CLI de Azure:  
~~~
$ curl -L https://aka.ms/InstallAzureCli | bash
~~~
Y reiniciamos la terminal:  
~~~
$ exec -l $SHELL
~~~

Nos logueamos con:  
~~~
$ az login
~~~
Y obtenemos el ID de cliente, el secreto del cliente y el Tenant ID con el comando:  
~~~
$ az ad sp create-for-rbac
~~~
Y la subscripcion con:  
~~~
$ az account list --query "[?isDefault].id" -o tsv
~~~
Estos 4 datos serán necesarios exportarlos como variables de entorno para el archivo Vagrantfile.  
Instalamos el plugin de Azure para Vagrant:  
~~~
$ vagrant plugin install vagrant-azure
$ npm install azure-cli -g
~~~
Y añadimos el box a Vagrant:  
~~~
$ vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
~~~
Ya podemos crear el archivo Vagrantfile, tal y como está en el repositorio.  
~~~
$ vagrant init azure
~~~

Ahora crearemos el archivo de aprovisionamiento, donde indicaremos todos lo necesario para nuestra app, tal y como se muestra [aqui](https://github.com/Anixo/ProyectoIV/blob/master/provision/playbook.yml).  
Tambíen añadimos un archivo de configuracion, tal y como se muestra [aqui](https://github.com/Anixo/ProyectoIV/blob/master/ansible.cfg).  

Ya podemos iniciar nuestra maquina virtual:  
~~~
$ vagrant up --provider=azure
~~~

Para instalar la aplicacion usaremos un archivo Fabric, como este de [aqui](https://github.com/Anixo/ProyectoIV/blob/master/despliegue/fabfile.py).  
Con este archivo se puede ejecutar tres acciones:
* **Instalar:** se instala supervisor, necesario para mantener el proceso en segundo plano, se clona el repositorio, se copia el archivo de configuracion que usa supervisor, como este de [aqui](https://github.com/Anixo/ProyectoIV/blob/master/hugwebconfig.conf), y se instalan los requirements.  
* **Desinstalar:** borra todo el repositorio.
* **Iniciar:** lanza supervisor y ejecuta la aplicacion en segundo plano.
* **Parar:** detiene supervisor.

Para ejecutar la instalacion de nuestra aplicacion con fabric, utilizamos el comando:  
~~~
$ fab -H <usuario>@<direccion_despliegue> <accion>
~~~

Despliegue final: maquinaquetoca.westeurope.cloudapp.azure.com
