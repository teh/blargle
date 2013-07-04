#!/usr/bin/python

import random
from time import sleep

import mosquitto

class Worder(object):

    def __init__(self,):
        with open('/usr/share/dict/words') as fh:
            self.dictionary = fh.readlines()

    def prune_dictionary(self, length):
        self.dictionary = [ i for i in self.dictionary if len(i) < length ]

    def get_word(self,):
        return random.choice(self.dictionary)




if __name__ == '__main__':
    w = Worder()

    while True:
        print w.get_word()

        sleep(2)

