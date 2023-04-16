"""
ECE 6397: Fuzzy Logic
Professor: Dr. Steven Provence
Author: Joshua Genova
Computer Assignment #8
Description:
    Thermostat Controller for an Air Conditioner.
Deadline: April 16, 2023 11:59PM
"""

import time
import sys
import numpy as np
from tabulate import tabulate
import ece6397_genova_helper_headerfooter as header_footer

class AirConditioner:
    def __init__(self, t_out, hum, occ, t_des):
        """
        set the variables
        """
        self.t_out = t_out
        self.hum = hum
        self.occ = occ
        self.t_des = t_des

        # constants
        self.d0 = 0.65
        self.d1 = 1.58
        self.n1 = 0.08
        
        print(f"Outside Temperature: {self.t_out} F")
        print(f"Room Humidity: {self.hum} %")
        print(f"Room Occupancy: {self.occ}")
        print(f"Desired Temperature: {self.t_des} F")

    def process(self, y_prev, u_prev):
        """
        create function for process
        """
        return self.d1*y_prev + self.n1*u_prev

    def sensor(self, y_prev):
        """
        create function for sensor
        """
        return (self.d0/self.n1)*y_prev
    

##################################################################################################
if __name__=="__main__":
    """
    Variable inputs:
        i) outside temperature (0 - 100 F)
        ii) room humidity (0 - 100 %)
        iii) room occupancy (empty to fully occupied)
        iv) desired temperature (60 - 72 F)
    The output should be a table, such that each row is a sample with four displayed columns:
    sample k, desired temp, actual temp, control effort u(k).
    Where the k samples only taken every 30.
    The script should stop running once the desired temperature has reached steady state for 2
    minutes . . . the control effort should likewise be at zero.
    """
    CA_NUM = 8
    DESCRIPTION = "Write a script that performs the operations presented in class."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    OUTSIDE_TEMP = int(sys.argv[1])
    HUMIDITY = int(sys.argv[2])
    OCCUPANCY = sys.argv[3]
    DESIRED_TEMP = sys.argv[4]
    AC = AirConditioner(OUTSIDE_TEMP, HUMIDITY, OCCUPANCY, DESIRED_TEMP)
    final_time = time.time() - start_time
    header_footer.footer(final_time)