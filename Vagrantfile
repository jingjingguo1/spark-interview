# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  
  config.vm.network "private_network", ip: "10.0.0.15"
  
  config.vm.synced_folder "", "/home/vagrant/spark-model"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end
  
  config.vm.provision "shell", path: "./bash/vagrant_spark_env.sh"

end