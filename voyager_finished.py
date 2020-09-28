"""
Mr. Callaghan
voyager_finished.py
Unit 1 Challenge Program
Calculates the distance and time for the Voyager probe
"""

#INPUTS
# Distance from Sun to Voyager in miles & kilometers
sunDistMiles = 16637000000
sunDistKm = sunDistMiles * 1.609344
# Velocity of Voyager in MPH & KPH
velocityMph = 38241
velocityKph = velocityMph * 1.609344
# Velocity in miles per day
velocityMpd = velocityMph * 24
# Radio waves in meters & km per second
radioMetersSec = 299792458
radioKmSec = radioMetersSec / 1000
# Radio waves in MPH (3600 secs in 1 hour)
radioKmHour = radioKmSec * 3600
radioMph = (radioKmHour * (.609344))

days = int(input("How many days since 25 September 2009 are you looking for"))

#CALCULATIONS
# Voyager distance in miles
totalDistMiles = sunDistMiles + (velocityMpd * days)
# Voyager distance in km
totalDistKm = totalDistMiles * 1.609344
# Voyager distance in AU
totalDistAu = totalDistMiles / 92955887.6
# Time for radio communication from Sun (using miles)
totalTimeRadio = (totalDistMiles / radioMph) * 2
# Time for radio communication from Sun (using km)
totalTimeRadioKm = (totalDistKm / radioKmHour) *2

#OUTPUT
print("Voyager's total distance in miles is:", totalDistMiles)
print("Voyager's total distance in Kilometers is:", totalDistKm)
print("Voyager's total distance in Astronomical Units is:", totalDistAu)
print("The time it would take to send and receive a radio transmission in hours is:", totalTimeRadio)

input("\n\n Press Enter to Exit")
