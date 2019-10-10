#!/bin/sh

echo "MQTT Client Observer: Waiting for MQTT Broker"
while ! nc -z $MQTT_BROKER_HOST $MQTT_BROKER_PORT; do
  sleep 0.1
done
echo "MQTT Client Observer: MQTT Broker is Up"

exec "$@"
