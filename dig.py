import os
import sys

DiscClaimer = input("Dig is not natively installed on windows!!! press enter to exit or anything else to continue! ")


def runncode():
    if not DiscClaimer:
        sys.exit()
    else:
        print("Hi")
        AssignIp.IP
        ClassNew.DigBoi


runncode()


class AssignIp:
    IP = input("Please enter the IP address you want me to dig! ")


class ClassNew:
    DigBoi = os.system("ping {}".format(AssignIp.IP))


