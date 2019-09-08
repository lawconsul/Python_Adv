import chardet
from chardet.universaldetector import UniversalDetector
str_data = "Тест"

str_data.encode()
bytes_data = b'\xd0'
chardet.detect(bytes_data)
import pickle

class Sample:
    def __init__(self, name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age


# class unasafle:
    