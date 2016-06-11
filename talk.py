# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
import types
from pprint import pprint
from action.receive import Receive

first_response = input("hello, how do you do > ")

t = Tokenizer()
tokens = t.tokenize(first_response)

w = Receive(tokens)
result = w.chose()

if False == result:
    learn_word = w.learn()
    teach = input("please tell us about " + learn_word.surface)

