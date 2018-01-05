# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "azure"
	config.vm.box_url = "https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box"
	config.vm.network "public_network"
	config.vm.network "forwarded_port", guest: 80, host: 80

	# use local ssh key to connect to remote vagrant box
	config.ssh.private_key_path = "~/.ssh/id_rsa"
	config.vm.provider :azure do |azure, override|
		azure.tenant_id = ENV["TENANT_ID"]
		azure.client_id = ENV["CLIENT_ID"]
		azure.client_secret = ENV["CLIENT_SECRET"]
		azure.subscription_id = ENV["SUB_ID"]
		azure.vm_image_urn = "canonical:UbuntuServer:16.04-LTS:16.04.201711211"
      azure.vm_size = "Basic_A0"
      azure.location = "westeurope"
      azure.tcp_endpoints = "80"
		azure.vm_name = "maquinaquetoca"
		azure.resource_group_name= "recursosiv"
	end

	# Provisionamiento con ansible
	config.vm.provision :ansible do |ansible|
		ansible.playbook = "./provision/playbook.yml"
	end
end
