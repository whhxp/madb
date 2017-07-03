# -*- coding: utf-8 -*-

class alloy2elements(object):
    def __init__(self):
        pass

    def readcsv(self):
        print("read csv")

    def stringConv(self):
        print("string Convertion")

    def writeCSV(self):
        print("write csv file")


def main():
    print("This script is used to convert alloy to elements.")

    work1 = alloy2elements()

    work1.readcsv()
    work1.stringConv()
    work1.writeCSV()


if __name__ == '__main__':
    main()
