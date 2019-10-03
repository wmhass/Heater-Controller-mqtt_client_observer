#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time




def on_message(client, obj, msg):
    payload = str(msg.payload.decode('utf-8'))
    print("Payload: " + payload)
    print("Topic: " + msg.topic)
    print("Obj: " + str(obj))
    client.publish("hello/debug")


if __name__ == '__main__':
    # f= open("/usr/src/files/file.txt","a+")
    # f.write("Hello 1\n")
    mqttc = mqtt.Client(client_id="sdasdjij")
    mqttc.username_pw_set(username="username", password="password")
    mqttc.on_message = on_message
    #mqttc.on_connect = on_connect
    #mqttc.on_publish = on_publish
    # mqttc.on_subscribe = on_subscribe
    # try:
    mqttc.connect("127.0.0.1")
    mqttc.subscribe("plug/#")
    #mqtt loop
    mqttc.loop_forever()
