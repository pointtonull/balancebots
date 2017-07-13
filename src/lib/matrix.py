#!/usr/bin/env python

from collections import defaultdict
try:
    from queue import Queue
except ImportError: # for Python2
    from Queue import Queue
import re
import threading

DSL = {
    re.compile(r"bot (?P<botname>\d+) gives low to (?P<low>\w+ \d+) and high to (?P<high>\w+ \d+)"): "order",
    re.compile(r"value (?P<value>\d+) goes to bot (?P<assignee>\d+)"): "assigns",
}


class Bot(threading.Thread):

    def __init__(self, matrix, name):
        super(Bot, self).__init__()
        self.matrix = matrix
        self.name = "bot %s" % name
        self.pocket = list()
        self.setted_up = threading.Event()

    def __repr__(self):
        return self.name

    def run(self):
        while True:
            basket = self.matrix.baskets[self.name]
            new_value = basket.get()
            if new_value == "kill":
                print(self, "is shuting down")
                break
            self.pocket.append(new_value)
            if len(self.pocket) == 2:
                self.setted_up.wait()
                low_basket = self.matrix.baskets[self.low]
                high_basket = self.matrix.baskets[self.high]
                low_value, high_value = sorted(self.pocket)
                low_basket.put(low_value)
                high_basket.put(high_value)
                print("  > %s assigning %s to %s and %s to %s" % (self,
                      low_value, self.low, high_value, self.high))
                if set(self.pocket) == self.matrix.target:
                    print("=== %s is the bot comparing %s" % (self.name,
                          self.pocket))
                    self.matrix.result = self
                    self.matrix.kill()

    def order(self, low, high):
        self.low = low
        self.high = high
        self.setted_up.set()

    def assign(self, value):
        basket = self.matrix.baskets[self.name]
        basket.put(value)


class Matrix:

    def __init__(self, target=None):
        self.baskets = defaultdict(Queue)
        self.done = threading.Event()
        self.flock = {}
        self.result = None
        self.target = target

    def get_bot(self, botname):
        if botname in self.flock:
            bot = self.flock[botname]
        else:
            bot = Bot(self, botname)
            print("  > %s had been created" % bot)
            self.flock[botname] = bot
            bot.start()
        return bot

    def kill(self):
        for basket in self.baskets.values():
            basket.put("kill")
        self.done.set()

    def order(self, botname, low, high):
        bot = self.get_bot(botname)
        bot.order(low, high)

    def assigns(self, value, assignee):
        bot = self.get_bot(assignee)
        bot.assign(value)

    def execute_instruction(self, instruction):
        for regex, handler_name in DSL.items():
            match = regex.match(instruction)
            if match:
                handler = getattr(self, handler_name)
                handler(**match.groupdict())
                break
        else:
            raise NotImplementedError("DSL is incomplete!")
