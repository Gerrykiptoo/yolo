Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", type: "dhcp"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io docker-compose
    systemctl start docker
    systemctl enable docker
    usermod -aG docker vagrant
  SHELL

  config.vm.define "frontend" do |frontend|
    frontend.vm.network "forwarded_port", guest: 3000, host: 3000
    frontend.vm.network "forwarded_port", guest: 22, host: 2222
    frontend.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.extra_vars = {
        vars_file: "/vagrant/vars/vars.yml"
      }
    end
  end

  config.vm.define "backend" do |backend|
    backend.vm.network "forwarded_port", guest: 5000, host: 5000
    backend.vm.network "forwarded_port", guest: 22, host: 2200
    backend.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.extra_vars = {
        vars_file: "/vagrant/vars/vars.yml"
      }
    end
  end

  config.vm.define "mongo" do |mongo|
    mongo.vm.network "forwarded_port", guest: 27017, host: 27017
    mongo.vm.network "forwarded_port", guest: 22, host: 2201
    mongo.vm.boot_timeout = 600  # Increase boot timeout to 10 minutes
    mongo.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook.yml"
      ansible.extra_vars = {
        vars_file: "/vagrant/vars/vars.yml"
      }
    end
  end
end
