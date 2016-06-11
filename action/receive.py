
from entity.word import Word
from pprint import pprint
import requests
import random

class Receive:

    word = property(doc='word property')

    @word.setter
    def word(self, value):
        self._word = value

    @word.getter
    def word(self):
        return self._word

    @word.deleter
    def word(self):
        del self._word

    def __init__(self, tokens):
        self._word = []
        for token in tokens:
            if '名詞' in token.part_of_speech:
                self._word.append(Word(token))

    def chose(self):
        for w in self._word:
            if '天気' in w.surface:
                weather_res = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010")
                weather_json = weather_res.json()
                print(weather_json["description"]["text"])
                return True
        return False

    def learn(self):
        random.shuffle(self._word)
        return self._word[0]


