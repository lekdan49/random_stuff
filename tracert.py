#! /usr/bin/env python3
import os


IP = input("Please enter the IP or website you want me to traceroute! ")


class BigBoi:
    ComRun = os.system("tracert {}".format(IP))


def RunCode():
    BigBoi.ComRun()

RunCode()