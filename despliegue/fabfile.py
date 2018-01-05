from fabric.api import run, sudo, env, shell_env
import os

def Instalar():
	run("git clone https://github.com/Anixo/ProyectoIV")
	run("pip3 install -r /home/vagrant/ProyectoIV/requirements.txt")

def Desinstalar():
	run("rm -R -f /home/vagrant/ProyectoIV")

def Iniciar():
	sudo("hug -p 80 -f /home/vagrant/ProyectoIV/botQueToca/hugweb.py")
