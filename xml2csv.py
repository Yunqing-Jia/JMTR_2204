#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2013-2021 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    xml2csv.py
# @author  Jakob Erdmann
# @author  Michael Behrisch
# @author  Laura Bieker
# @date    2013-12-08


from __future__ import print_function
from __future__ import absolute_import
import os
import sys
import socket
import gzip
import io
import collections
from optparse import OptionParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
import csv

def main():
    tree = parse('tripinfo.xml')
    # root=tree.getroot()
    rootNode = tree.documentElement
    customers = rootNode.getElementsByTagName("tripinfo")
    # print(root.attrib)
    #print(customers)

        # name 元素
    bp = str([11 * 1800, 28 * 1800, 36 * 1800, 40 * 1800])
    i=0;d1=[];d2=[];d3=[];d4=[];d5=[]
    with open('test1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        for tripinfo in customers:
            #if tripinfo.hasAttribute("departDelay"):
                i+=1
                tt=tripinfo.getAttribute("arrival")
                #print("ID:", tripinfo.getAttribute("id"))
                writer.writerow([i, tt, tripinfo.getAttribute("departDelay")])

                #print("ID:", tripinfo.getAttribute("id"))
                #writer.writerow([i, tripinfo.getAttribute("id"), "Linux Kernel"])
        #writer.writerow(["SN", "Name", "Contribution"])
        #writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
        #writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
        #writer.writerow([3, "Guido van Rossum", "Python Programming"])


if __name__ == "__main__":
    main()
	
