"""
Created on 02.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171102

@description: Implementation eines einfachen Encryptors für A bis Z,
              aber auch zusätzlich für alle visible ascii chars in einem erweiterten Schritt
"""
import threading


class SimpleEncrypter(threading.Thread):

    dictionary = {}
    distance = 0
    decryption = False
    message = ""

    def __init__(self, firstIndex, offset):
        threading.Thread.__init__(self)
        self.firstIndex = firstIndex
        self.offset = offset

    @staticmethod
    def setCryptography(dic1, distance=0, decryption=False):
        SimpleEncrypter.dictionary = dic1
        SimpleEncrypter.distance = distance
        SimpleEncrypter.decryption = decryption

    @staticmethod
    def setDecryption(enabled):
        SimpleEncrypter.decryption = enabled

    @staticmethod
    def setMessage(message):
        SimpleEncrypter.message = message

    @staticmethod
    def getMessage():
        return SimpleEncrypter.message

    def run(self):

        pass

