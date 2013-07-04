typed_word_queue = []

def pick_word():
    return 'hello'

def on_message(mosq, obj, msg):
    print "msg", msg
    typed_word_queue.append(msg)

client.subscribe('command', 0)
client.on_message = on_message

def main():
    command = pick_word()
    while True:
        client.loop(50) # check every 50 ms
        try:
            typed_word_queue.pop(0, None)
        except IndexError:
            pass
