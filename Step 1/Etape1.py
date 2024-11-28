# 3rd party imports
import numpy as np

# private imports
import Plate_examples   # script with plates examples


# Plate index
plate_example_index = 1

# print(plate_example_index)
# print(Plate_examples.plate{plate_example_index}.score_calculated)

print("Plate n°" + str(plate_example_index))
print("Score calculated : " + str(Plate_examples.plate1.score_calculated))
print("Score given : " + str(Plate_examples.plate1.score_given))
