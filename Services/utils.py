import json
import random
import cv2
import numpy as py


class ProjectUtils:

    @staticmethod
    def loadJson():

        with open('ML' + '.json', 'r') as f:
            obj = json.load(f)

        return obj


    @staticmethod
    def writeToJson(data):

        with open('FM.json', 'w') as outfile:
            json.dump(data, outfile)


    @staticmethod
    def createRandomMail():

        randEmail = ''.join(random.choice('0123456789ABCDEF') for i in range(16)) + '@mycheck.co.il'

        return randEmail

    @staticmethod
    def createRandomSmsCode():

        randSms = ''.join(random.choice('0123456789') for i in range(6))

        return randSms

    @staticmethod
    def createRandomScreenShotNumber():

        screenShotNumber = ''.join(random.choice('0123456789') for i in range(3))

        return screenShotNumber

    @staticmethod
    def imagesComparator(image1, image2):

        image1 = cv2.imread(image1)
        image2 = cv2.imread(image2)

        diff = cv2.subtract(image1, image2)

        result = not py.any(diff)

        if result is True:
            print("no diff")
        else:
            cv2.imwrite('result.png', diff)




