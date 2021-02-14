import paho.mqtt.client as mqtt
import json
import random
import time
import threading

THE_BROKER_SENSOR = "eu.thethings.network"
THE_TOPIC_SENOR = "+/devices/+/up"

THE_BROKER_SERVER = "test.mosquitto.org"
THE_TOPIC_SERVER = "PMtest/rndvalue/Daniel"


CLIENT_ID = ""
humidity = 0
lux = 0
temperature = 0
gtwID_list = 0
gtwRSSI_list = 0
datos = ''

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(THE_TOPIC_SENOR, qos=0)

# The callback for when a message is received from the server.
def on_message(client, userdata, msg):
  global datos
  # Imprimir datos Json
  d = json.loads(msg.payload)
  #print(json.dumps(d, indent=2))
  
  # Datos de temperatura, humedad y luminicida
  payload = d["payload_fields"]
  humidity = payload["humidity"]
  lux = payload["lux"]
  tempeature = payload["temperature"]
  
  # Datos de Tiempo
  metadata = d["metadata"]
  data_time= metadata["time"] 

  #datos = {'temperature' : tempeature, 'time':data_time}
  #datos = {'humidity' : humidity, 'time':data_time} 
  datos = {'lux' : lux, 'time':data_time}


# The callback for when a message is published.
def on_publish(client, userdata, mid):
    print("sipub: msg published (mid={})".format(mid))


client_sensor = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")


client_server = mqtt.Client(client_id=CLIENT_ID, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

# Hilo para Publicar el mensaje
def Publicar_Server():
  client_server.on_connect = on_connect
  client_server.on_publish = on_publish 
  client_server.username_pw_set(None, password=None)
  client_server.connect(THE_BROKER_SERVER, port=1883, keepalive=60)
  client_server.loop_start()
  msg_to_be_sent = datos
  while True:
    time.sleep(0.25)
    if msg_to_be_sent != datos and msg_to_be_sent!='':
      print(json.dumps(msg_to_be_sent))
      client_server.publish(THE_TOPIC_SERVER, 
                    payload=json.dumps(msg_to_be_sent), 
                    qos=0, 
                    retain=False)
    msg_to_be_sent = datos
  client_server.loop_stop()



# Hilo para recibir datos del sensor de medicion
def Recibir_Sensor():
  client_sensor.on_connect = on_connect
  client_sensor.on_message = on_message
  client_sensor.username_pw_set("lopy2ttn", password="ttn-account-v2.TPE7-bT_UDf5Dj4XcGpcCQ0Xkhj8n74iY-rMAyT1bWg")
  client_sensor.connect(THE_BROKER_SENSOR, port=1883, keepalive=60)
  client_sensor.loop_forever()

#Ejecucion de los hilos
hilo1 = threading.Thread(target=Publicar_Server)
hilo2 = threading.Thread(target=Recibir_Sensor)
hilo1.start()
hilo2.start()


