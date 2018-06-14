Solarsystem-Shower
##################################################################################
The program Solarsystem-Shower is a real-time simulation. The user has the
possibility to switch on a shower. Two tanks, one cold and one warm, are
available, both with a capacity of 300kg. A graphic indicates a reduction
in the water level and when the tanks are refilled, a drop of the temperature
in the hot tank. To continue to supply the shower with warm water, the user
can turn on a collector, which raises the temperature of the hot tank (340K max).
The efficiency of the collector depends on the position of the sun (illustrated
in the graphic). Since the program has been tried to run in real time as far as
possible, the user can close the program after starting the collector: the last
values ​​(water temperatures, solar irradiance, water level) are saved in an XML file
inside the temp-folder and processed when restarting the program. The current ambient
temperature is the ambient temperature of Braunschweig (Real-time). For this, the
program sends a request to https://openweathermap.org.
In addition, the user can retrieve statistics, the daily water consumption, the
temperatures and the time needed to heat the hot water tank to 340K when the
collector will be turned on.

Requirements
##################################################################################
Packages: PyQt5, Numpy, Matplotlib, xml.etree.ElementTree
Python: Python3

Usage
##################################################################################
Main-Class (Starter): MainWindow.py

Possible extensions
###################################################################################
It would be nice if the state of the sun is not hardcoded (only time-dependent),
but also read via https://openweathermap.org (like the current temperature) and
the clouding could also affect the percentage of solar irradiance.
Another extension would be that the user can change the flow rate of the shower (current
flowrate = 1kg/s).
By storing any changes to the values in the xml-file per day (what the program already
supports), more comprehensive statistics can be collected, such as daily water usage,
average shower temperature per day, average collector usage, etc.