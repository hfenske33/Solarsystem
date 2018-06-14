import os
import xml.etree.ElementTree as ET
import datetime

import AdditionalOperations as AO
from Parameter import Parameters as P


def save():
    xmlPath = str("temp/" + AO.getDate() + ".xml")
    if (os.path.exists(xmlPath)):
        appendData()
    else:
        root = ET.Element("root")
        subroot = ET.SubElement(root, "time" )
        subroot.text = str(AO.getTimeSecInt())
        ET.SubElement(subroot, "hotTankTemp").text = str(P.hotTankTemp)
        ET.SubElement(subroot, "coldTankTemp").text = str(P.coldTankTemp)
        ET.SubElement(subroot, "hotTankFluid").text = str(P.fluidLevelHot)
        ET.SubElement(subroot, "coldTankFluid").text = str(P.fluidLevelCold)
        ET.SubElement(subroot, "solarIrradiance").text = str(P.solarIrradiance)
        ET.SubElement(subroot, "lastTime").text = str(AO.getTimeInt())
        ET.SubElement(subroot, "collectorIsOn").text = str(P.collectorIsOn)
        ET.SubElement(subroot, "collectorTemp").text = str(P.collectorTemp)

        tree = ET.ElementTree(root)
        tree.write("temp/" + AO.getDate() + ".xml")

def appendData():
    tree = ET.parse("temp/" + AO.getDate() + ".xml")
    root = tree.getroot()
    subroot = ET.Element("time")
    subroot.text = str(AO.getTimeSecInt())
    ET.SubElement(subroot, "hotTankTemp").text = str(P.hotTankTemp)
    ET.SubElement(subroot, "coldTankTemp").text = str(P.coldTankTemp)
    ET.SubElement(subroot, "hotTankFluid").text = str(P.fluidLevelHot)
    ET.SubElement(subroot, "coldTankFluid").text = str(P.fluidLevelCold)
    ET.SubElement(subroot, "solarIrradiance").text = str(P.solarIrradiance)
    ET.SubElement(subroot, "lastTime").text = str(AO.getTimeInt())
    ET.SubElement(subroot, "collectorIsOn").text = str(P.collectorIsOn)
    ET.SubElement(subroot, "collectorTemp").text = str(P.collectorTemp)

    root.append(subroot)
    tree = ET.ElementTree(root)
    tree.write("temp/" + AO.getDate() + ".xml")

def loadLastData():
    tree = ET.parse("temp/" + AO.getDate() + ".xml")
    root = tree.getroot()

    P.hotTankTemp = float(root[len(root) - 1][0].text)
    P.coldTankTemp = float(root[len(root) - 1][1].text)
    P.fluidLevelHot = float(root[len(root) - 1][2].text)
    P.fluidLevelCold = float(root[len(root) - 1][3].text)

    P.collectorTemp = float(root[len(root) - 1][7].text)


def getStatisticValuesTemp():
    xmlPath = str("temp/" + AO.getDate() + ".xml")
    if (os.path.exists(xmlPath)):
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        x = []
        yhot = []
        ycold = []
        ycolector = []
        together = []
        for i in range(len(root)):
            x.append(getDateTime(int(root[i].text)))
            yhot.append(float(root[i][0].text))
            ycold.append(float(root[i][1].text))
            ycolector.append(float(root[i][7].text))
        together.append(x)
        together.append(yhot)
        together.append(ycold)
        together.append(ycolector)
        return together


def getStatisticsValuesLevel():
    xmlPath = str("temp/" + AO.getDate() + ".xml")
    if (os.path.exists(xmlPath)):
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        x = []
        yh = []
        yc = []
        together = []
        for i in range(len(root)):
            x.append(getDateTime(int(root[i].text)))
            yh.append(float(root[i][2].text))
            yc.append(float(root[i][3].text))
        together.append(x)
        together.append(yh)
        together.append(yc)
        return together


def getDateTime(dateInt):
    h = int(dateInt/10000)
    m = int((dateInt%10000)/100)
    s = int((dateInt%10000)%100)
    st = str(h) + ":" + str(m) + ":" + str(s)
    d = datetime.datetime.strptime(st, "%H:%M:%S")
    return d


def clearStatistics():
    xmlPath = str("temp/" + AO.getDate() + ".xml")
    if (os.path.exists(xmlPath)):
        os.remove(xmlPath)
