#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memitem.py
#
# Part of MARK II project. For informations about license, please
# see file /LICENSE .
#
# author: Vladislav Mlejnecký
# email: v.mlejnecky@seznam.cz


class memitem(object):

    def __init__(self, baseAddress, size, name):
        self.__name__ = name

        self.startAddress = baseAddress
        self.endAddress = baseAddress + (2**size) - 1
        self.size = size
        self.mem = [0] * (2**size)


    def read(self, address):
        if address >= self.startAddress and address <= self.endAddress:
            return self.mem[address - self.startAddress]
        else:
            return None

    def write(self, address, value):
        if address >= self.startAddress and address <= self.endAddress:
            self.mem[address - self.startAddress] = value

    def reset(self):
        self.mem = [0] * (2**self.size)

