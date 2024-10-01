#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2021 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    main.py
# @author  Yunqing Jia (JMTR)
# @date    2024-10-01

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random

# we need to import python modules from the $SUMO_HOME/tools directory
import scipy.io


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


from xml.dom.minidom import parse
import csv

def xml2csv():
    tree = parse('tripinfo.xml')
    # root=tree.getroot()
    rootNode = tree.documentElement
    customers = rootNode.getElementsByTagName("tripinfo")
    # print(root.attrib)
    #print(customers)

        # name 元素

    i=0;#d1=[];d2=[];d3=[];d4=[];d5=[]
    with open('test1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        for tripinfo in customers:
            #if tripinfo.hasAttribute("departDelay"):
                i+=1
                tt=tripinfo.getAttribute("arrival")
                #print("ID:", tripinfo.getAttribute("id"))
                writer.writerow([i, tt, tripinfo.getAttribute("departDelay")])


def generate_routefile():
    random.seed(42)  # make tests reproducible
    INT = 288
    

    day = 7
    A_tensor= scipy.io.loadmat('avol_7_288_8.mat')['lana2vol']
    
    with open("test.rou.xml", "w") as routes:  #accel="0.8" decel="4.5" sigma="0.5" length="5" maxSpeed="60"
        print("""<routes>
        <vType id="type1" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67"/>
        <route id="R1" edges="ASI RSIII" />
        <route id="R2" edges="ASII RSI" />
        <route id="R3" edges="ASII RSIV" />
        <route id="R4" edges="ASIII RSII" />
        <route id="R5" edges="ASIII RSI" />
        <route id="R6" edges="ASIV RSIII" />
        <route id="R7" edges="ASIV RSII" />
        <route id="R8" edges="ASI RSIV" />
        <route id="R9" edges="ASI RSII" />
        <route id="R10" edges="ASII RSIII" />
        <route id="R11" edges="ASIII RSIV" />
        <route id="R12" edges="ASIV RSI" />""", file=routes)
        
        for i in range(INT):
            print('         <flow id="typeR9_%i" route="R9"  color="1,1,0"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),15+random.randint(-5,5)), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR10_%i" route="R10"  color="1,1,0"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),15+random.randint(-5,5)), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR11_%i" route="R11"  color="1,1,0"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),15+random.randint(-5,5)), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR12_%i" route="R12"  color="1,1,0"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),15+random.randint(-5,5)), file=routes)
            print("     </flow>", file=routes)
            ###############   ↑right-turn
            print('         <flow id="typeR1_%i" route="R1"  color="1,0,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,0]*2), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR2_%i" route="R2"  color="0,1,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,1]), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR3_%i" route="R3"  color="1,0,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,2]), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR4_%i" route="R4"  color="0,1,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,3]), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR5_%i" route="R5"  color="1,0,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,4]*2), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR6_%i" route="R6"  color="0,1,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,5]), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR7_%i" route="R7"  color="1,0,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,6]), file=routes)
            print("     </flow>", file=routes)
            print('         <flow id="typeR8%i" route="R8"  color="0,1,1"  begin="%i" end= "%i" number="%i" type="type1">' % (
                    i, 300*i+1,300*(i+1),A_tensor[day-1,i,7]), file=routes)
            print("     </flow>", file=routes)

        print("</routes>", file=routes)



def run():
    """execute the TraCI control loop"""
    step = 0
    
    bp=[72*300,123*300,192*300,240*300]

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        tt=traci.simulation.getTime()
        if tt <= bp[0]:
             traci.trafficlight.setProgram('CP', 1)

        elif tt>bp[0] and tt<=bp[1]:
             traci.trafficlight.setProgram('CP', 2)
             #print('1111')
        elif tt>bp[1] and tt<=bp[2]:
             traci.trafficlight.setProgram('CP', 3)
        elif tt > bp[2] and tt <= bp[3]:
             traci.trafficlight.setProgram('CP', 4)
        elif tt>bp[3]:
             traci.trafficlight.setProgram('CP', 5)
        step += 1
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "test.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
    xml2csv()