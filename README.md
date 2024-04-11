# ImageS-VD
ImageS-VD is a project developed as a part of a Bachelor's thesis in Computer Science and Technologies at the University of Basilicata.<br/>
The goal is the creation of a desktop application for image compression using the Singular Value Decomposition (SVD).<br/>
The program allows also to save the decomposed matrices of an image as npz file to avoid do decompose the image again and load the matrices from the file.<br/>
The project is written in Python using the numpy library.

## Current status
The project is in a early state of development.

## Dependencies
- Pillow;
- Numpy;
- PySide6.

# Usage
The project provides two scripts to launch the program.<br/>
It can be used also in cli mode with the --cli or -c flag:
## Windows
```
imageS-VD --cli <input-file-name> <output-file-name> [singular-value-threshold]
```
## Unix
```
./imageS-VD.sh --cli <input-file-name> <output-file-name> [singular-value-threshold]
```
The threshold is needed only if the output file isn't a .npz file.<br/>
If the threshold is set to 0, the image is reconstructed using all singular values.
# License
This project is distributed under the BSD-3 license.
