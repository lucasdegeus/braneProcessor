#!/usr/bin/env python3
import os
import sys
import yaml
import pandas as pd
import numpy as np
from collections import defaultdict
from typing import List

# Reads one column for a CSV and casts all values in this column to string.
def read_csv_column(filename: str, separator: str, columname: str) -> List[str]:
    return list(pd.read_csv(filename,sep=separator).loc[:,columname].replace(np.nan, 'NA', regex=True).astype('string'))

# Makes a dictionary from two lists of equal size and returns two lists. One for keys and one for values.
def average_over_dict(keys: List[str], values: List[float]) -> (List[str], List[float]):
    assert(len(keys) == len(values))
    # Group
    key_value = defaultdict(list)
    for i in range(len(values)):
        key_value[keys[i]].append(values[i])
    # Aggregate
    result_keys = []
    result_values = []
    results = {}
    for key in keys:
        if (key not in results):
            results[key] = True
            result_keys.append(str(key))
            result_values.append(float(sum(key_value[key]) / len(key_value[key])))
    return (result_keys, result_values)

if __name__ == "__main__":
    command = sys.argv[1]
    if (command == "read_csv_column"):
        argument_file = os.environ["FILENAME"]
        argument_separator = os.environ["SEPARATOR"]
        argument_column = os.environ["COLUMN"]
        output = read_csv_column(argument_file, argument_separator, argument_column)
        print("--> START CAPTURE")
        print(yaml.dump({"output": output}))
        print("--> END CAPTURE")

    else:
        argument_keys = [str(os.environ[f"KEYS_{i}"]) for i in range(int(os.environ["KEYS"]))]
        argument_values = [float(os.environ[f"VALUES_{i}"]) for i in range(int(os.environ["VALUES"]))]
        averages = average_over_dict(argument_keys, argument_values)
        # Use either keys or values depending on what is requested.
        output = averages[0] if command == 'average_over_dict_keys' else averages[1]
        print("--> START CAPTURE")
        print(yaml.dump({"output": output}))
        print("--> END CAPTURE")
