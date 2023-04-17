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
#pylint: disable=import-error
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from astropy.table import Table
# pylint: enable=import-error
import ece6397_genova_helper_headerfooter as header_footer

class AirConditioner:
    """
    class for AC
    """
    def __init__(self, t_out, hum, occ, t_des):
        """
        set the variables
        """
        self.t_out = int(t_out)
        self.hum = int(hum)
        self.occ = int(occ)
        self.t_des = int(t_des)

        # constants
        self.d_0 = 0.065
        self.d_1 = 0.158
        self.n_1 = 0.08

        self.outside_temperature = ctrl.Antecedent(np.arange(0, 100, 1), 'outside temperature')
        self.humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')
        self.occupancy = ctrl.Antecedent(np.arange(0, 100, 1), 'room occupancy')
        self.temperature = ctrl.Antecedent(np.arange(60, 72, 1), 'desired temperature')
        self.control = ctrl.Consequent(np.arange(-1975, 1250, 1), 'control effort')
    def fuzzification(self):
        """
        fuzzy the input variables
        """
        self.outside_temperature['too-low'] = fuzz.trimf(self.outside_temperature.universe,
                                                         [0, 0, 60])
        self.outside_temperature['range-low'] = fuzz.trimf(self.outside_temperature.universe,
                                                           [60, 63, 66])
        self.outside_temperature['range-mid'] = fuzz.trimf(self.outside_temperature.universe,
                                                           [63, 66, 69])
        self.outside_temperature['range-high'] = fuzz.trimf(self.outside_temperature.universe,
                                                            [66, 69, 72])
        self.outside_temperature['too-high'] = fuzz.trimf(self.outside_temperature.universe,
                                                          [72, 100, 100])

        self.humidity['dry'] = fuzz.trimf(self.humidity.universe,
                                          [0, 0, 50])
        self.humidity['normal'] = fuzz.trimf(self.humidity.universe,
                                             [30, 50, 80])
        self.humidity['wet'] = fuzz.trimf(self.humidity.universe,
                                          [50, 80, 100])

        self.occupancy['empty'] = fuzz.trimf(self.occupancy.universe,
                                             [0, 0, 50])
        self.occupancy['medium'] = fuzz.trimf(self.occupancy.universe,
                                              [30, 50, 70])
        self.occupancy['full'] = fuzz.trimf(self.occupancy.universe,
                                            [50, 80, 100])

        self.temperature['range-low'] = fuzz.trimf(self.temperature.universe,
                                                   [60, 63, 66])
        self.temperature['range-mid'] = fuzz.trimf(self.temperature.universe,
                                                   [63, 66, 69])
        self.temperature['range-high'] = fuzz.trimf(self.temperature.universe,
                                                    [66, 69, 72])

        self.control['low-max'] = fuzz.trimf(self.control.universe,
                                             [-1975, -1975, 0])
        self.control['lower'] = fuzz.trimf(self.control.universe,
                                           [-987.5, -362.5, 0])
        self.control['medium'] = fuzz.trimf(self.control.universe,
                                            [-362.5, 0, 262.5])
        self.control['higher'] = fuzz.trimf(self.control.universe,
                                            [0, 262.5, 625])
        self.control['high-max'] = fuzz.trimf(self.control.universe,
                                              [262.5, 1250, 1250])

    def create_rules(self):
        """
        create the rules from fuzzification
        """
        self.fuzzification()
        rule1 = ctrl.Rule(self.outside_temperature['too-low'], self.control['high-max'])
        rule2 = ctrl.Rule(self.outside_temperature['too-high'], self.control['low-max'])
        rule3a_a = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['dry']
                              & self.occupancy['empty']
                              & self.temperature['range-low'], self.control['higher'])
        rule3a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['high-max'])
        rule3a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['high-max'])
        rule4a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['higher'])
        rule4a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['higher'])
        rule4a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['high-max'])
        rule5a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['medium'])
        rule5a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['higher'])
        rule5a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['higher'])
        rule6a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['higher'])
        rule6a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['higher'])
        rule6a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule7a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['medium'])
        rule7a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['higher'])
        rule7a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['higher'])
        rule8a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['lower'])
        rule8a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['medium'])
        rule8a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['higher'])
        rule9a_a = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['medium'])
        rule9a_b = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['higher'])
        rule9a_c = ctrl.Rule(self.outside_temperature['range-low']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule10a_a = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-low'], self.control['lower'])
        rule10a_b = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-mid'], self.control['medium'])
        rule10a_c = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-high'], self.control['higher'])
        rule11a_a = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-low'], self.control['lower'])
        rule11a_b = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-mid'], self.control['lower'])
        rule11a_c = ctrl.Rule(self.outside_temperature['range-low']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-high'], self.control['medium'])
        rule3b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['higher'])
        rule3b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['higher'])
        rule3b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule4b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['medium'])
        rule4b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry'] & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['higher'])
        rule4b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['higher'])
        rule5b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['lower'])
        rule5b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['medium'])
        rule5b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['higher'])
        rule6b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['medium'])
        rule6b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['higher'])
        rule6b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule7b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['lower'])
        rule7b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['medium'])
        rule7b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['higher'])
        rule8b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['lower'])
        rule8b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal'] & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['lower'])
        rule8b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['medium'])
        rule9b_a = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['lower'])
        rule9b_b = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['medium'])
        rule9b_c = ctrl.Rule(self.outside_temperature['range-mid']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule10b_a = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-low'], self.control['lower'])
        rule10b_b = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-mid'], self.control['lower'])
        rule10b_c = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-high'], self.control['medium'])
        rule11b_a = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-low'], self.control['lower'])
        rule11b_b = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-mid'], self.control['lower'])
        rule11b_c = ctrl.Rule(self.outside_temperature['range-mid']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-high'], self.control['lower'])
        rule3c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['medium'])
        rule3c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['higher'])
        rule3c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule4c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['lower'])
        rule4c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['medium'])
        rule4c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['higher'])
        rule5c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['lower'])
        rule5c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['lower'])
        rule5c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['dry']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['medium'])
        rule6c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['lower'])
        rule6c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['medium'])
        rule6c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['higher'])
        rule7c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-low'], self.control['lower'])
        rule7c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-mid'], self.control['lower'])
        rule7c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['medium']
                             & self.temperature['range-high'], self.control['medium'])
        rule8c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-low'], self.control['lower'])
        rule8c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-mid'], self.control['lower'])
        rule8c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['normal']
                             & self.occupancy['full']
                             & self.temperature['range-high'], self.control['lower'])
        rule9c_a = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-low'], self.control['lower'])
        rule9c_b = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-mid'], self.control['lower'])
        rule9c_c = ctrl.Rule(self.outside_temperature['range-high']
                             & self.humidity['wet']
                             & self.occupancy['empty']
                             & self.temperature['range-high'], self.control['medium'])
        rule10c_a = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-low'], self.control['lower'])
        rule10c_b = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-mid'], self.control['lower'])
        rule10c_c = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['medium']
                              & self.temperature['range-high'], self.control['lower'])
        rule11c_a = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-low'], self.control['low-max'])
        rule11c_b = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-mid'], self.control['lower'])
        rule11c_c = ctrl.Rule(self.outside_temperature['range-high']
                              & self.humidity['wet']
                              & self.occupancy['full']
                              & self.temperature['range-high'], self.control['lower'])

        return [rule1, rule2,
                rule3a_a, rule3a_b, rule3a_c,
                rule4a_a, rule4a_b, rule4a_c,
                rule5a_a, rule5a_b, rule5a_c,
                rule6a_a, rule6a_b, rule6a_c,
                rule7a_a, rule7a_b, rule7a_c,
                rule8a_a, rule8a_b, rule8a_c,
                rule9a_a, rule9a_b, rule9a_c,
                rule10a_a, rule10a_b, rule10a_c,
                rule11a_a, rule11a_b, rule11a_c,
                rule3b_a, rule3b_b, rule3b_c,
                rule4b_a, rule4b_b, rule4b_c,
                rule5b_a, rule5b_b, rule5b_c,
                rule6b_a, rule6b_b, rule6b_c,
                rule7b_a, rule7b_b, rule7b_c,
                rule8b_a, rule8b_b, rule8b_c,
                rule9b_a, rule9b_b, rule9b_c,
                rule10b_a, rule10b_b, rule10b_c,
                rule11b_a, rule11b_b, rule11b_c,
                rule3c_a, rule3c_b, rule3c_c,
                rule4c_a, rule4c_b, rule4c_c,
                rule5c_a, rule5c_b, rule5c_c,
                rule6c_a, rule6c_b, rule6c_c,
                rule7c_a, rule7c_b, rule7c_c,
                rule8c_a, rule8c_b, rule8c_c,
                rule9c_a, rule9c_b, rule9c_c,
                rule10c_a, rule10c_b, rule10c_c,
                rule11c_a, rule11c_b, rule11c_c,
                ]
    def get_control(self):
        """
        compute control effort
        """
        ac_ctrl = ctrl.ControlSystem(self.create_rules())
        control_effort = ctrl.ControlSystemSimulation(ac_ctrl)

        control_effort.input['outside temperature'] = int(self.t_out)
        control_effort.input['humidity'] = int(self.hum)
        control_effort.input['room occupancy'] = int(self.occ)
        control_effort.input['desired temperature'] = int(self.t_des)
        control_effort.compute()
        print(f"control effort: {control_effort.output['control effort']}")
        return control_effort.output['control effort']

    def process(self, y_prev, u_prev):
        """
        create function for process
        """
        return self.d_1*y_prev + self.n_1*u_prev

    def sensor(self, y_prev):
        """
        create function for sensor
        """
        return (self.d_0/self.n_1)*y_prev
    def update(self):
        """
        update the actual temp
        """
        samples = []
        actual_temp = []
        ctrl_eff = []
        y_prev = self.t_out
        u_prev = self.get_control()/1000
        error_prev = 0
        output_table = Table(names=('Samples', 'Desired Temp', 'Actual Temp', 'Control Effort'))
        for k in range(1000):
            samples.append(k+1)
            y_k = self.process(y_prev, u_prev)
            actual_temp.append(y_k)
            y_prev = y_k
            y_m = self.sensor(y_prev)
            error = abs(self.t_des - y_m)
            if error > 30:
                u_prev = u_prev* 1.0
            if (error <= 30) & (error > 20):
                u_prev = u_prev * 0.8
            if (error <= 20) & (error > 10):
                u_prev = u_prev * 0.6
            if (error <= 10) & (error > 5):
                u_prev = u_prev * 0.4
            if (error <= 5) & (error > 1):
                u_prev = u_prev * 0.2
            if error < 1:
                u_prev = u_prev*0
            delta_error = error - error_prev
            error_prev = error
            if (k > 1) & (delta_error > 0):
                u_prev = -u_prev
            ctrl_eff.append(u_prev)
            # print(f"yk: {y_k}, uk: {u_prev}, ym: {y_m}, error: {error}")
            if (k+1) % 30 == 0:
                output_table.add_row((k+1, self.t_des, y_k, u_prev))
            if ((delta_error < 1e-2) & (delta_error > -1e-2)) | (error < 1):
                if len(output_table) == 0:
                    output_table.add_row((k+1, self.t_des, y_k, u_prev))
                break
        print("\n")
        print(output_table)
        print("\n")
##################################################################################################
if __name__=="__main__":
    CA_NUM = 8
    DESCRIPTION = "Thermostat Controller for an Air Conditioner."
    header_footer.header(CA_NUM, DESCRIPTION)
    start_time = time.time()
    OUTSIDE_TEMP = int(sys.argv[1])
    HUMIDITY = int(sys.argv[2])
    OCCUPANCY = sys.argv[3]
    DESIRED_TEMP = sys.argv[4]
    print(f"Outside Temperature: {OUTSIDE_TEMP} F")
    print(f"Room Humidity: {HUMIDITY} %")
    print(f"Room Occupancy: {OCCUPANCY}")
    print(f"Desired Temperature: {DESIRED_TEMP} F")
    AC = AirConditioner(OUTSIDE_TEMP, HUMIDITY, OCCUPANCY, DESIRED_TEMP)
    AC.update()
    final_time = time.time() - start_time
    header_footer.footer(final_time)
