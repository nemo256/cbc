# Count Blood Cells
Count red, white blood cells to detect various diseases such as blood cancer (leukemia), lower red blood cells count (anemia)...

![Sample](sample.png)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Project Structure](#project-structure)
* [Install](#install)
* [Usage](#usage)
* [Develop](#develop)
* [License](#license)

## Project Structure
```
cbc/
|-- data/
|   |-- plt/...
|   |-- rbc/...
|   |-- wbc/...
|
|-- docs/...
|
|-- models/...
|
|-- output/
|   |-- plt/...
|   |-- rbc/...
|   |-- wbc/...
|
|-- AUTHORS
|-- cbc
|-- LICENSE
|-- README.md
|-- TODO.md
|-- requirements.txt 
|-- setup.py
```

## Install
- Install straight from PyPI using pip:
```
$ pip install cbc
```
## Usage
> Please read `cbc --help` before using it
> -o flag is optional (defaults to out/ directory)
- Count blood cells (-r for red and -w for white):
```
$ cbc -r <blood-cell-image>
```
- Predict red blood cells (use Circle Hough Tranform and Connected Component Labeling with otsu's thresholding):
```
$ cbc -r -CHT -CCL -t <blood-cell-image>
```
- Predict white blood cells (with custom output directory):
```
$ cbc -w <blood-cell-image> -o outdir/
```

## Develop
- Download the project:
```
$ git clone https://github.com/nemo256/cbc
$ cd cbc 
```
- Activate virtual environment:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
- Now just adapt the code to your needs and then run using the command:
```
$ chmod +x cbc
$ ./cbc
```

## License
- Please read [cbc/LICENSE](https://github.com/nemo256/cbc/blob/master/LICENSE)
