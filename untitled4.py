# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:20:16 2023

@author: User
"""

Columns explanation :

title: title name given to the earthquake
magnitude: The magnitude of the earthquake
date_time: date and time
cdi: The maximum reported intensity for the event range
mmi: The maximum estimated instrumental intensity for the event
tsunami: "1" for events in oceanic regions and "0" otherwise
sig: A number describing how significant the event is. Larger numbers indicate a more significant event. This value is determined on a number of factors, including: magnitude, maximum MMI, felt reports, and estimated impact
net: The ID of a data contributor. Identifies the network considered to be the preferred source of information for this event.
nst: The total number of seismic stations used to determine earthquake location.
dmin: Horizontal distance from the epicenter to the nearest station
gap: The largest azimuthal gap between azimuthally adjacent stations (in degrees). In general, the smaller this number, the more reliable is the calculated horizontal position of the earthquake. Earthquake locations in which the azimuthal gap exceeds 180 degrees typically have large location and depth uncertainties
magType: The method or algorithm used to calculate the preferred magnitude for the event
depth: The depth where the earthquake begins to rupture
latitude / longitude: coordinate system by means of which the position or location of any place on Earth's surface can be determined and described
country: affected country
Open Tableau public in your desktop and load the dataset from the provided CSV file.
Create a Pie chart to answer the following question : How many earthquakes had resulted in a tsunami ?
Illustrate a map chart to showcase the earthquakes' magnitude distribution worldwide.
Select the best visual to display the earthquakes' magnitude fluctuation in Peru and Russia.
Select the best visual to display the relationship between the earthquakes' magnitude and their significance level. Interpret the results.
Select the best visual to display the earthquakes' magnitude distribution in 2022.
Personalize your charts by adding relevant titles and renaming their axes.
Create a Dashboard that englobe all the created charts and save it into your tableau public account.