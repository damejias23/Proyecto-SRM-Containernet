#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
server = net.addDocker('server', ip='10.0.0.250',		
			dcmd="python app_ServerTelegram.py",
                       dimage="server_telegram:latest")
client1 = net.addDocker('client1', ip='10.0.0.251', 
			dcmd="python Nodo1_temp.py",
			dimage="client_data:latest")
client2 = net.addDocker('client2', ip='10.0.0.252', 
			dcmd="python Nodo2_lux.py",			
			dimage="client_data:latest")
client3 = net.addDocker('client3', ip='10.0.0.253', 
			dcmd="python Nodo3_humidity.py",
			dimage="client_data:latest")
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(server, s1)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s2, client1)
net.addLink(s2, client2)
net.addLink(s2, client3)
info('*** Starting network\n')
net.start()

info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()
