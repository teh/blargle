import sys
import mosquitto


SERVER, CLIENT = sys.argv[1:]

client = mosquitto.Mosquitto(CLIENT)
client.connect(SERVER)

while True:
    msg = raw_input('enter msg: ')
    client.publish('blargle', msg, 1)
    client.loop()
