from fabric.api import run, sudo, env, shell_env
import os

def Instalar():
	sudo("apt-get install -y supervisor")
	run("git clone https://github.com/Anixo/ProyectoIV")
	sudo("cp /home/vagrant/ProyectoIV/hugwebconfig.conf /etc/supervisor/conf.d/")
	sudo("pip3 install -r /home/vagrant/ProyectoIV/requirements.txt")

def Desinstalar():
	sudo("rm -R -f /home/vagrant/ProyectoIV")

def Iniciar():
	run("cd /home/vagrant/ProyectoIV/ && sudo supervisorctl reread && sudo supervisorctl reload && sudo supervisorctl start hugweb", pty = False)
