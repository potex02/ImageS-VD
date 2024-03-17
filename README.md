# ImageS-VD
ImageS-VD is a project developed as a part of a Bachelor's thesis in Computer Science and Technologies at the University of Basilicata.<br/>
The goal is the creation of a desktop application for image compression using the Singular Value Decomposition (SVD).<br/>
<!--The program allows also to save the decomposed matrices of an image in JSON, YAML or XML format to avoid do decompose the image again and load the matrices from the file.<br/>-->
The project is written in Python using the numpy library.

## Current status
The project is in a very early state of development and can be used only by command line for now.

## Dependecies
- Pillow;
- Numpy;

# Usage
The project provides two scripts to launch the program.
## Windows
```
imageS-VD <input-file-name> <output-file-name> <singular-value-threshold>
```
## Unix
```
./imageS-VD.sh <input-file-name> <output-file-name> <singular-value-threshold>
```

# License
This project is distributed under the BSD-3 license.
