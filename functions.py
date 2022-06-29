#####################################################
# Functions used in scripts for the VORTEX SE project
#####################################################

import numpy as np
import datetime as dt
import matplotlib as mpl
import matplotlib.pyplot as plt
#import probe_info
import subprocess as sp
import os

def get_winddir_string(ws):
    if ws >= 0.0 and ws < 22.5:
        return 'N'
    elif ws >= 22.5 and ws < 67.5:
        return 'NE'
    elif ws >= 67.5 and ws < 112.5:
        return 'E'
    elif ws >= 112.5 and ws < 157.5:
        return 'SE'
    elif ws >= 157.5 and ws < 202.5:
        return 'S'
    elif ws >= 202.5 and ws < 247.5:
        return 'SW'
    elif ws >= 247.5 and ws < 292.5:
        return 'W'
    elif ws >= 292.5 and ws < 337.5:
        return 'NW'
    else:
        return 'N'


def calc_thetae(T,Td,P):
	""" Calculate equivalent potential temperature from Bolton (1980)
	Inputs: Temperature (T, celcius), Dewpoint (Td, celcius) and Station Pressure (P, hPa)
	Output: Equivalent Potential Temperature (theta_e, Kelvin) """
	e = 6.11*(10**((7.5*Td)/(237.3+Td)))                              # vapor pressure, uses degrees C
	w = 0.622 * e/(P-e)		                                          # mixing ratio, uses hPa for pressure variables
	T_K,Td_K = T + 273.15,Td + 273.15                                 # convert T and Td to Kelvin
	Tl = 1.0/(1.0/(Td_K-56.0) + np.log(T_K/Td_K)/800.0) + 56.0  	  # approximated temperature at LCL (Kelvin)
	theta_l = T_K * ((1000.0/(P-e))**0.2854) * (T_K/Tl)**(0.28*w)     # dry potential temperature at LCL (Kelvin)
	theta_e = theta_l * np.exp(((3036.0/Tl)-1.78)*w*(1.0+0.448*w))    # equivalent potential temp (Kelvin)
	return theta_e

def calc_thetav(T,Td,P):
	""" Calculate theta v from Bolton (1980)
	theta_v = theta (1+0.61w)
	Inputs: Temperature (T, celcius), Dewpoint (Td, celcius), Station Pressure (P, hPa)"""
	e = 6.11*(10**((7.5*Td)/(237.3+Td)))
	w = 0.622 * e/(P-e)
	kappa = 2/7.
	theta = (T+273.15)*((1000/P)**kappa)
	theta_v = theta*(1+0.61*w)
	return theta_v

def convert_wind(ws,dir):
    """ convert wind speed to u and v components (in knots) for plotting wind barbs """
    new_dir = 270-dir
    u = (ws*1.94384)*np.cos(new_dir * np.pi/180)
    v = (ws*1.94384)*np.sin(new_dir * np.pi/180)
    return u,v

# calc station pressure from MSLP, T, H
def calc_station_pressure(p_slp,t,h):
	""" p_slp in mb, t in K, h in meters """
	return p_slp * np.exp(-h/(t+29.263))

def alt_to_mb(mm):
	return mm*33.8637526

def calc_dewpoint(T,RH):
    #RH = np.ma.masked_values(RH,-999.9)
    num = np.log(RH/100) + (17.625*T)/(243.04+T)
    denom = 17.625 - np.log(RH/100) - (17.625*T)/(243.04+T)
    return 243.04*num/denom

def calc_windchill(T,V):
    """ Temperature in fahrenheit and wind speed V in miles per hour"""
    return 35.74 + 0.6215*T - 32.75*(V**0.16) + 0.4275*T*(V**0.16)

def calc_heatindex(T,RH):
    """ Temperature in fahrenheit and relative humidity in percent """
    line1 = -42.379 + (2.04901523*T) + (10.14333127*RH)
    line2 = (0.22475541 * T * RH) + (6.83783 * 10**-3 * T**2)
    line3 = (5.481717*10**-1 * RH**2) - (1.22874 * 10**-3 * T**2 * RH)
    line4 = (8.5282*10**-4 * T * RH**2) - (1.99*10**-6 * T**2 * RH**2)
    return line1-line2-line3+line4

def calc_mslp(T,P,h):
    return P*(1-(0.0065*h)/(T+0.0065*h+273.15))**(-5.257)

def C_to_F(temp):
    return np.round(temp*1.8 + 32,decimals=1)
