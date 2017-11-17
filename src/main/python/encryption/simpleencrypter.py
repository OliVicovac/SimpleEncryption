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
        SimpleEncrypter.message = "".join(SimpleEncrypter.message)
        return SimpleEncrypter.message

    def run(self):

        counter = self.firstIndex   #  first index (0, 1, 2, 3..)
        end = len(SimpleEncrypter.message)     # ende ist der letze buchstaben der message
        if SimpleEncrypter.decryption == False:
            iterable = list(SimpleEncrypter.message)    # liste
            while counter < end:    # Solange wie der counter nicht das ende vom wort erreicht hat
                c = iterable[counter]
                c = SimpleEncrypter.dictionary[c]   # sucht value in dictionary mit key
                iterable[counter] = c   # buchstabe wieder zurückschreiben
                counter += self.offset  #  [offset] buchstaben weiter gehen

            SimpleEncrypter.message = "".join(iterable)
        else:
            for i in range(len(SimpleEncrypter.message)):       #for Schleife für jeden charakter
                for key in SimpleEncrypter.dictionary:      #
                    if SimpleEncrypter.dictionary[key]==list[i]:
                        list[i] = key










