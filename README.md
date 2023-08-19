# FediPhish
![made with python](https://raw.githubusercontent.com/1337kid/FediPhish/main/img/made-with-python.svg)
![hardstyle](https://raw.githubusercontent.com/1337kid/FediPhish/main/img/made-with-hardstyle.svg)

## Installation
```bash
git clone https://github.com/1337kid/csv2json.git
cd csv2json
sudo make install
```
## Usage
```
Usage  : csv2json infile outfile [indent]
Example: csv2json test.csv outfile.json
       : csv2json test.csv outfile.json 2
Default indentation is 4
```
### Sample CSV
```
name,age
kewldog,12
kewlcat,23
```
### Generated JSON
```json
{
    "1": {
        "name": "kewldog",
        "age": "12"
    },
    "2": {
        "name": "kewlcat",
        "age": "23"
    }
}
```
![csv2json](https://raw.githubusercontent.com/1337kid/csv2json/main/img/sc.png)