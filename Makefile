#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Centos 7 VM and Environment
install:
	vagrant plugin install vagrant-vbguest && vagrant up
start:
	vagrant up
reload:
	vagrant reload
stop:
	vagrant halt
clean:
	vagrant destroy
ssh:
	vagrant ssh

## Submit spark jobs on VM
assemble:
	spark-submit --master local ./src/data/assemble_data.py

# featurize:
# 	spark-submit --master local ./src/features/featurize_data.py

classifier:
	spark-submit --master local ./src/models/model_data.py