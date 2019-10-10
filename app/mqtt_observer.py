#!/usr/bin/env python
import paho.mqtt.client as mqtt
import os


def on_message(client, obj, msg):
    payload = str(msg.payload.decode('utf-8'))
    print("Payload: " + payload)
    print("Topic: " + msg.topic)
    print("Obj: " + str(obj))
    client.publish("hello/debug1")

if __name__ == '__main__':
    # f = open("/usr/src/mqtt_client_observer/file.txt", "w+")
    # f.write("Hello 1\n")
    #
    mqtt_host = os.environ.get('MQTT_BROKER_HOST')
    mqtt_port = int(os.environ.get('MQTT_BROKER_PORT'))

    mqtt_username = os.environ.get('MQTT_USERNAME')
    mqtt_password = os.environ.get('MQTT_PASSWORD')
    mqtt_client_id = os.environ.get('MQTT_CLIENT_ID')

    mqttc = mqtt.Client(client_id=mqtt_client_id)
    mqttc.username_pw_set(username=mqtt_username, password=mqtt_password)
    mqttc.on_message = on_message
    mqttc.connect(host=mqtt_host, port=mqtt_port)
    mqttc.subscribe("say/hello")
    mqttc.loop_forever()

    #mqttc.on_connect = on_connect
    #mqttc.on_publish = on_publish
    # mqttc.on_subscribe = on_subscribe
