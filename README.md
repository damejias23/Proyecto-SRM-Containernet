# Proyecto-SRM-Containernet


## Containernet: Mininet fork that allows to use Docker containers as hosts in emulated networks

<img align="left" width="200" height="200" style="margin-right: 30px" src="https://raw.githubusercontent.com/containernet/logo/master/containernet_logo_v1.png">


# Containernet - Node simulation with MQTT with Telegram Bot server

Containernet is a fork of the famous Mininet network emulator and allows Docker containers to be used as hosts in emulated network topologies. This enables interesting functionalities to build network / cloud emulators and benchmarks. To carry out tests with Containernet, a node connection will be created where temperature, luminicity and humidity measurements will be made through an MQTT connection and will be sent to a server node that will send the data to the users by Telegram.

This work will cite and work with the data obtained with the following work:

M. Peuster, H. Karl, and S. v. Rossem: MeDICINE: Rapid Prototyping of Production-Ready Network Services in Multi-PoP Environments. IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN), Palo Alto, CA, USA, pp. 148-153. doi: 10.1109/NFV-SDN.2016.7919490. (2016)

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




