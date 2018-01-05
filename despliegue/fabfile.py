from fabric.api import run, sudo, env, shell_env
import os

def Instalar():
	sudo("apt-get install -y supervisor")
	run("git clone https://github.com/Anixo/ProyectoIV")
	sudo("cp /home/vagrant/ProyectoIV/supervisor.conf /etc/supervisor/conf.d/")
	run("pip3 install -r /home/vagrant/ProyectoIV/requirements.txt")

def Desinstalar():
	sudo("rm -R -f /home/vagrant/ProyectoIV")

def Iniciar():
	sudo("cd /home/vagrant/ProyectoIV/ && supervisorctl reread && supervisorctl reload && supervisorctl start hugweb", pty = False)
