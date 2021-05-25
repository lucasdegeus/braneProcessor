# dataprocessor
Dataprocessor is a brane package for manipulating data and using various statistical functions on this data.
Think about packages such as Pandas and Numpy for Python. Currently only two functions are identified:
    * A function to read a csv and return one column of this csv
    * A function that computes the average for each key in a dictionary. The keys are represented as a list and the values as well.

## Installation

If on Linux or MacOS first run:

``` chmod +x run.py ```

Otherwise/then:

```console
brane build container.yml
brane push dataprocessor 1.0.0
```

Or install using the brane import function: 
```
brane import lucasdegeus/braneLocation --kind ecu
```


## Usage average
Input parameters are:
    * keys: an array of keys in a dictionary
    * values: an array that should equal the length of keys and should contain the values associated with the keys.
```brane
import dataprocessor;

let keys := ["Canada", "Canada", "United States of America"];
let values := [100.0, 200.0, -50.0];

average_over_dict_values(keys, values);
average_over_dict_keys(keys, values);
```

## Usage csv
Input parameters are:
    * file: filename to read from
    * separator: the seperator between columns. Usually a "," in a csv
    * columname: the column to retrieve from this csv
```brane
read_csv_column(/data/<filename.csv>, ",", "columnname");
```

## Notes
It is currently not possible to return tuples, dictionaries or multiple outputs in Brane. Therefore, the average function is split into two. ``average_over_dict_values`` returns the keys and ``average_over_dict_values`` the values corresponding with those keys.
