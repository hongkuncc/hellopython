#encoding:utf-8
import types
class Person(object):
    def __init__(self,name):
        self.name=name


    def run(self):
        print('%s在奔跑')