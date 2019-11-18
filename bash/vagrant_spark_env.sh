#!/bin/bash
# Java
sudo yum install java -y
# Scala
sudo yum install wget -y
wget https://downloads.lightbend.com/scala/2.13.1/scala-2.13.1.tgz
tar xvf scala-2.13.1.tgz
sudo mv scala-2.13.1 /usr/lib
sudo ln -s /usr/lib/scala-2.13.1 /usr/lib/scala
export PATH=$PATH:/usr/lib/scala/bin
# Spark
wget http://apache-mirror.8birdsvideo.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
tar xvf spark-2.4.4-bin-hadoop2.7.tgz
# set environment
export SPARK_HOME=$HOME/spark-2.4.4-bin-hadoop2.7
export PATH=$PATH:$SPARK_HOME/bin
# set .bash_profile environment
echo 'export PATH=$PATH:/usr/lib/scala/bin' >> .bash_profile
echo 'export SPARK_HOME=$HOME/spark-2.4.4-bin-hadoop2.7' >> .bash_profile
echo 'export PATH=$PATH:$SPARK_HOME/bin' >> .bash_profile
# pip, numpy
sudo yum install epel-release -y
sudo yum install python-pip -y
sudo pip install --upgrade pip
sudo pip install numpy