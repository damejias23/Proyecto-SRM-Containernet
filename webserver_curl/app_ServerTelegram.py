import argparse
import base64
import json
import logging
import signal
import struct
import sys
import time

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import paho.mqtt.client as mqtt
from datetime import datetime, timezone

THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "PMtest/rndvalue/Daniel"

r_value = "VOID"
t_value = "VOID"
l_value = "VOID"
h_value = "VOID"
time_value = "VOID"

def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(THE_TOPIC, qos=0)

def on_message(client, userdata, msg):
    global r_value, t_value, l_value, h_value, time_value
    print("msg received with topic: {} and payload: {}".format(msg.topic, str(msg.payload)))
    if ("Daniel" in msg.topic):
      d = json.loads(msg.payload)
      r_value = d
      if ("temperature" in d):
        t_value = d["temperature"]
        time_value = d["time"]
        print(t_value)
      
      if ("lux" in d):
        l_value = d["lux"]
        time_value = d["time"]
        print(l_value)

      if ("humidity" in d):
        h_value = d["humidity"]
        time_value = d["time"]
        print(h_value)        
      
      
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/gettime to get measurement time")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/gettemp to get temperature")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/gethumidity to get humidity")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/getlux to get luminicity")
    
def gettime(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(time_value))

def gettemp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(t_value))    
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(time_value))
	

def getlux(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(l_value)) 
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(time_value))

def gethumidity(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(h_value)) 
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(time_value))

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


updater = Updater(token='1537395092:AAGo0e3XKdZnCxzPKQ3-BXk7xsTUVy7uvMc', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

gettime_handler = CommandHandler('gettime', gettime, pass_args=False)
dispatcher.add_handler(gettime_handler)

gettemp_handler = CommandHandler('gettemp', gettemp, pass_args=False)
dispatcher.add_handler(gettemp_handler)

getlux_handler = CommandHandler('getlux', getlux, pass_args=False)
dispatcher.add_handler(getlux_handler)

gethumidity_handler = CommandHandler('gethumidity', gethumidity, pass_args=False)
dispatcher.add_handler(gethumidity_handler)

unknown_handler = MessageHandler(Filters.text & (~Filters.command), unknown)
dispatcher.add_handler(unknown_handler)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(None, password=None)
client.connect(THE_BROKER, port=1883, keepalive=60)
client.loop_start()

updater.start_polling()
updater.idle()

