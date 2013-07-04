import sys
import mosquitto


def on_message(mosq, obj, msg):
    print "msg", msg
    typed_word_queue.append(msg)


def mainloop():
    command = pick_word()
    print "please shout {}".format(command)

    while True:
        client.loop(50) # check every 50 ms
        try:
            word = typed_word_queue.pop()
            break
        except IndexError:
            pass
    if word == command:
        print "success"
        

def main():
    SERVER, CLIENT = sys.argv[1:]

    client = mosquitto.Mosquitto(CLIENT)
    client.connect(SERVER)

    client.subscribe('command', 0)
    client.on_message = on_message


    while True:
        msg = raw_input('enter msg: ')
        client.publish('blargle', msg, 1)
        client.loop()


main()