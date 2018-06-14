'''
Includes supportive methods to return parameters such as current
temperature in Brunswick, current time, solar irradiance, colr of
tanks (depends on temperature) and position of the sun. The state
of the sun is hardcoded in the range (6am to 6pm) and depends on
the current time.
'''

import datetime
import math
import requests
from PyQt5.QtGui import QColor

from Parameter import Parameters as P


# returns the current time as int (like 12:34 -> 1234) in range 6am-6pm
def getTimeInt():
    now = datetime.datetime.now()
    time = (now.hour * 100) + now.minute
    if(time < 600):
        return 600
    elif(time > 1800):
        return 1800
    else:
        return time

    # returns the current time as int (like 12:34 -> 1234) in range 6am-6pm
def getTimeSecInt():
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    s = now.second
    return h * 10000 + m * 100 + s

# returns the current time as string hh:mm
def getTime():
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    if(m < 10):
        return str(h) + ":0" + str(m)
    else:
        return str(h) + ":" + str(m)

def getDate():
    now = datetime.datetime.now()
    y = now.year
    m = now.month
    d = now.day
    if(d < 10):
        return str(y) + "_" + str(m) + "_0" + str(d)
    else:
        return str(y) + "_" + str(m) + "_" + str(d)


# returns x-coordinate of the sun, depends on daytime
def getXSunCoordinate(timeInt):
    return (1200 - timeInt) / 2

# returns x-coordinate of the sun, depends on daytime
def getYSunCoordinate(x):
    return math.sqrt(300 - abs(x)) * 10

# Get current temperature of Brunswick from OpenWeatherMap (https://openweathermap.org)
# APPID is a default ID
# 7c5780015a045be5fd564eafab3a9e35
def getTemperature():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Brunswick&APPID=7c5780015a045be5fd564eafab3a9e35')
    list = r.json()
    P.ambientTemp = list['main']['temp']
    return list['main']['temp']

# Get the percentage (0...1) of solar irradiance
# 12:00 = 100%, <=06:00 = 0%, >=18:00 = 0%
def getSolarIrradiancePercent():
    time = getTimeInt()
    return (600 - abs(1200 - time))/600

# Set the current solar irradiacne depends on actual time
def setSolarIrradiance():
    P.currentSolarIrradiance = getSolarIrradiancePercent() * P.solarIrradiance


# Get solar irradiance and its percentage as String
def getSolarIrradianceString():
    sr = getSolarIrradiancePercent()
    text = str(round(P.currentSolarIrradiance, 2))
    percent = str(round(sr * 100, 2))
    return text + " (" + percent + "%)"


# Get the state of the hot tank: if empty -> False
def getLevelHotTank():
    return P.fluidLevelHot > 6


# Get the state of the cold tank: if empty -> False
def getLevelColdTank():
    return P.fluidLevelCold > 6

# Get the current color of the hot Tank, depends on temperature
def getColorHotTank():
    tempHot = P.hotTankTemp
    if(tempHot >= 335):
        return QColor(150, 0, 0)
    elif(tempHot < 335 and tempHot > 330):
        return QColor(255, 50, 50)
    elif(tempHot <= 330 and tempHot > 320):
        return QColor(255, 150, 150)
    elif(tempHot <= 320):
        return QColor(255, 200, 200)

# Get the current color of the cold Tank, depends on temperature
def getColorColdTank():
    tempCold = P.coldTankTemp
    if(tempCold <= 293):
        return QColor(0, 0, 150)
    elif(tempCold > 293 and tempCold < 300):
        return QColor(0, 100, 200)
    elif(tempCold >= 300):
        return QColor(100, 170, 255)
