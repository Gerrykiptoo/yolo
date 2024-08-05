Vagrant.configure("2") do |config|
  # Define the frontend VM
  config.vm.define "frontend" do |frontend|
    frontend.vm.box = "ubuntu/bionic64"
    frontend.vm.network "private_network", ip: "192.168.56.11"
    frontend.vm.network "forwarded_port", guest: 3000, host: 3000
    frontend.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io docker-compose
      systemctl start docker
      systemctl enable docker
      usermod -aG docker vagrant
    SHELL
    frontend.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  # Define the backend VM
  config.vm.define "backend" do |backend|
    backend.vm.box = "ubuntu/bionic64"
    backend.vm.network "private_network", ip: "192.168.56.12"
    backend.vm.network "forwarded_port", guest: 5000, host: 5000
    backend.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io docker-compose
      systemctl start docker
      systemctl enable docker
      usermod -aG docker vagrant
    SHELL
    backend.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  # Define the MongoDB VM
  config.vm.define "mongo" do |mongo|
    mongo.vm.box = "ubuntu/bionic64"
    mongo.vm.network "private_network", ip: "192.168.56.13"
    mongo.vm.network "forwarded_port", guest: 27017, host: 27017
    mongo.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io docker-compose
      systemctl start docker
      systemctl enable docker
      usermod -aG docker vagrant
    SHELL
    mongo.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  # Provision with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
  end
end
