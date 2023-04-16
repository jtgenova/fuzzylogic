import numpy as np
import skfuzzy as fuzz

# Define the input variable
x = np.arange(0, 11, 1)

# Define the membership functions
low = fuzz.trimf(x, [0, 0, 5])
medium = fuzz.trimf(x, [0, 5, 10])
high = fuzz.trimf(x, [5, 10, 10])

# Calculate the fuzzy set
fuzzy_set = np.fmax(low, np.fmax(medium, high))
print(low)

# Defuzzify using the centroid method
defuzzified_value = fuzz.defuzz(x, fuzzy_set, 'centroid')

print("Defuzzified value:", defuzzified_value)
