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
import ece6397_genova_helper_headerfooter as header_footer

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