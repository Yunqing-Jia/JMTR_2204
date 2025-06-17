from __future__ import print_function
from __future__ import absolute_import
from xml.dom.minidom import parse
import csv

def main():
    tree = parse('tripinfo.xml')
    rootNode = tree.documentElement
    customers = rootNode.getElementsByTagName("tripinfo")
    i=0;d1=[];d2=[];d3=[];d4=[];d5=[]
    with open('test1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SN", "Name", "Contribution"])
        for tripinfo in customers:
                i+=1
                tt=tripinfo.getAttribute("arrival")
                
                writer.writerow([i, tt, tripinfo.getAttribute("departDelay")])


if __name__ == "__main__":
    main()
	
