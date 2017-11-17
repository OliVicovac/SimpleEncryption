"""
Created on 02.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171102

@description: Implementation eines einfachen Encryptors für A bis Z,
              aber auch zusätzlich für alle visible ascii chars in einem erweiterten Schritt
"""
from encryption.simpleencrypter import SimpleEncrypter


class Cryptography():

    def __init__(self, message, dictionary, threads, distance=0):
        if isinstance(message, (dict, set)):
            raise TypeError()
        self.__message = message
        self.__secretDictionary = dictionary
        self.__threadcount = threads
        self.__distance = distance


    def setDictionary(self,dictionary):
        self.__secretDictionary = dictionary

    def setMessage(self,message):
        if isinstance(message, (dict, set)):
            raise TypeError()
        self.__message = message

    def setThreadCount(self,threads):
        self.__threadcount = threads

    def getEncryptedMessage(self):
        threads = []
        SimpleEncrypter.setCryptography(self.__secretDictionary)
        SimpleEncrypter.setMessage(self.__message)
        for i in range(self.__threadcount):
            t = SimpleEncrypter(i, self.__threadcount)
            threads.append(t)
            t.start()

        for j in range(self.__threadcount):
            threads[j].join()
            encryptedM = SimpleEncrypter.getMessage()
            return encryptedM

    def getDecryptedMessage(self):
        pass

def main():
    dict = {' ': ' ', 'A': 'V', 'B': 'J', 'C': 'Z', 'D': 'B', 'E': 'G', 'F': 'N', 'G': 'F', 'H': 'E',
                         'I': 'P', 'J': 'L', 'K': 'I', 'L': 'T', 'M': 'M', 'N': 'X', 'O': 'D', 'P': 'W', 'Q': 'K',
                         'R': 'Q', 'S': 'U', 'T': 'C', 'U': 'R', 'V': 'Y', 'W': 'A', 'X': 'H', 'Y': 'S', 'Z': 'O'}

    bmessage = input("Nachricht eingeben")
    threads = int(input("Threadanzahl eingeben"))


    crypt = Cryptography(bmessage, dict, threads)
    encryptedMessage = crypt.getEncryptedMessage()
    decryptedMessage = crypt.getDecryptedMessage()

    print('Your decrypted message: %s' % encryptedMessage)





if  __name__ == '__main__':
    main()