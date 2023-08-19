# CONVCSV2JSON
Convert a CSV file into JSON format based on CSV headers
```bash
pip install convcsv2json
```
## Usage
```python
from convcsv2json import csv2json

data=csv2json(
    'sample.csv',        # CSV filename
    intend=4,            # JSON intendation
    numbered=True        # Set JSON data in numbered format or not
    )
print(data.conv()) # Print in JSON format
data.export('export.json') # Export the data into a JSON file
```
```"intend" and "numbered" parameters are optional. By default, "intend" is set as None and "numbered" is set as False```
```python
from convcsv2json import csv2json
print(csv2json('sample.csv',4).conv())
```
### Sample CSV
```
name,age
kewldog,12
kewlcat,23
```
### Generated JSON
```json
[
    {
        "name": "kewldog",
        "age": "12"
    },
    {
        "name": "kewlcat",
        "age": "23"
    }
]
```
