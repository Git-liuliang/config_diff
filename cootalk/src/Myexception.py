#!/usr/bin/env python
# encoding: utf-8

class NofileException(Exception):

    def __init__(self, parameter):
        err = 'one of your file is not exist in remote machine,detail>> "{0}" '.format(parameter)
        Exception.__init__(self, err)
        self.parameter = parameter
