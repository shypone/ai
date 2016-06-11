
class Word:
    def __init__(self, token):
        self.noun = token.part_of_speech
        self.surface = token.surface


