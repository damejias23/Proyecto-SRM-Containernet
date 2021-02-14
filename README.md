# Proyecto-SRM-Containernet


## Containernet: Mininet fork that allows to use Docker containers as hosts in emulated networks

<img align="left" width="200" height="200" style="margin-right: 30px" src="https://raw.githubusercontent.com/containernet/logo/master/containernet_logo_v1.png">


# Containernet - Node simulation with MQTT with Telegram Bot server

Containernet is a fork of the famous Mininet network emulator and allows Docker containers to be used as hosts in emulated network topologies. This enables interesting functionalities to build network / cloud emulators and benchmarks. To carry out tests with Containernet, a node connection will be created where temperature, luminicity and humidity measurements will be made through an MQTT connection and will be sent to a server node that will send the data to the users by Telegram.

This work will cite and work with the data obtained with the following work:

M. Peuster, H. Karl, and S. v. Rossem: [**MeDICINE: Rapid Prototyping of Production-Ready Network Services in Multi-PoP Environments**](http://ieeexplore.ieee.org/document/7919490/). IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN), Palo Alto, CA, USA, pp. 148-153. doi: 10.1109/NFV-SDN.2016.7919490. (2016)

Based on: **Mininet 2.3.0d5**

* Containernet website: https://containernet.github.io/
* Mininet website:  http://mininet.org
* Original Mininet repository: https://github.com/mininet/mininet


## Installation Containernet

Automatic installation is provided through an Ansible playbook.

Requires: **Ubuntu Linux 18.04 LTS** and **Python3**
Experimental: **Ubuntu Linux 20.04 LTS** and **Python3**

```bash
$ sudo apt-get install ansible git aptitude
$ git clone https://github.com/containernet/containernet.git
$ cd containernet/ansible
$ sudo ansible-playbook -i "localhost," -c local install.yml
$ cd ..
```
    
Wait (and have a coffee) ...

You can switch between development (default) and normal installation as follows:

```sh
sudo make develop
# or 
sudo make install
```

## Download the repository files

You must apply the following command to download the files that the project execution contains:

```
git clone https://github.com/damejias23/Proyecto-SRM-Containernet.git
```

## Build Server and Client images

For the execution of the nodes. The images must be created with the information of the nodes to be executed. For that, the following commands must be carried out:

```sh
cd Proyecto-SRM-Containernet
# To Server imagen
docker build --tag=server_telegram -f webserver_curl/Dockerfile.server webserver_curl
# To client imagen
docker build --tag=client_data -f Dockerfile.client .
```
 The images are built with version **python:3.8.2-buster**. 


## Run the simulation

In the execution of this program the file **containernet_node_sensor_telegram.py** is used. In this file the creation of the nodes is declared. Where the **Server, Node1, Node2 and Node3** nodes are created.

**Node1** will be in charge of measuring the temperature and sending it to **Server**.

**Node2** will be in charge of measuring the luminicity and sending it to **Server**.

**Node3** will be in charge of measuring the humidity and sending it to **Server**.


```sh
sudo python3 containernet_node_sensor_telegram.py
```

When executing the command the following result would be shown

```python
*** Adding controller
*** Adding docker containers
1: 
server: kwargs {'ip': '10.0.0.250'}
server: update resources {'cpu_quota': -1}
1: 
client_data; latest; None; sha256:7bb7b9d108774bacce1dc99b36513eca089d599424948ac749cb6862a154a13c
client_data; latest; None; sha256:53939ad671343059088d4a185ccbe16f418733af692e23fd848441ac301daafd
client1: kwargs {'ip': '10.0.0.251'}
client1: update resources {'cpu_quota': -1}
1: 
client_data; latest; None; sha256:7bb7b9d108774bacce1dc99b36513eca089d599424948ac749cb6862a154a13c
client_data; latest; None; sha256:53939ad671343059088d4a185ccbe16f418733af692e23fd848441ac301daafd
client2: kwargs {'ip': '10.0.0.252'}
client2: update resources {'cpu_quota': -1}
1: 
client_data; latest; None; sha256:7bb7b9d108774bacce1dc99b36513eca089d599424948ac749cb6862a154a13c
client_data; latest; None; sha256:53939ad671343059088d4a185ccbe16f418733af692e23fd848441ac301daafd
client3: kwargs {'ip': '10.0.0.253'}
client3: update resources {'cpu_quota': -1}
*** Adding switches
*** Creating links
(1.00Mbit 100ms delay) (1.00Mbit 100ms delay) (1.00Mbit 100ms delay) (1.00Mbit 100ms delay) *** Starting network
*** Configuring hosts
server client1 client2 client3 
*** Starting controller
c0 
*** Starting 2 switches
s1 (1.00Mbit 100ms delay) s2 (1.00Mbit 100ms delay) ...(1.00Mbit 100ms delay) (1.00Mbit 100ms delay) 
*** Running CLI
*** Starting CLI:
```

## Test 

For the test of the use in Telegram you can open the boot in the following link: https://t.me/SRM_Danielbot

