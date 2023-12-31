# ImageS-VD
ImageS-VD is a project developed as a part of a Bachelor's thesis in Computer Science and Technologies at the University of Basilicata.<br/>
The goal is the creation of a desktop application for image compression using the Singulat Value Decomposition (SVD).<br/>
The program allow also to save the decomposed matrices of an image in JSON, YAML, XML or binary format to avoid do decompose the image again and load the matrices from the file.<br/>
The project is written in C++ following the MVC (Model-View-Controller) pattern, uses CMake as build system and requires the version 17 of the C++ standard.

## Current status
The project is in a very early state of development and can be used only by command line for now.

## Dependecies
- Pkg-config;
- Gtkmm3;
- OpenCV.

## Compilation
### Windows
1. Install [MSYS2](https://www.msys2.org/) following the instruction of the official site;
2. Select options to install packages for C++ development during installation;
3. Open MSYS2 shell;
4. Run the following commands:
```bash
# Update the system
pacman -Syu
# For 64-bit systems
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-pkg-config mingw-w64-x86_64-gtkmm3 mingw-w64-x86_64-opencv
# For 32-bit systems
pacman -S mingw-w64-i686-gcc mingw-w64-i686-cmake mingw-w64-i686-pkg-config mingw-w64-i686-gtkmm3 mingw-w64-i686-opencv
```
### Debian/Ubuntu
```bash
sudo apt update
sudo apt install g++ cmake pkg-config libgtkmm-3.0-dev libopencv-dev
```
### Fedora 
```bash
sudo dnf update
sudo dnf install gcc-c++ cmake pkgconf gtkmm30-devel opencv-devel
```
### Arch linux
```bash
sudo pacman -Syu
sudo pacman -S gcc cmake pkgconf gtkmm3 opencv
```
### FreeBSD
```bash
sudo pkg update
sudo pkg install cmake pkgconf gtkmm30 opencv
```
### Mac OS
1. Install [Brew](https://brew.sh/) following the instruction of the official site;
2. Open a shell;
3. Run the following commands:
```bash
brew update
brew install gcc cmake pkg-config gtkmm3 opencv
```

# Build
1. Open a shell (MSYS2 on Windows);
2. navigate to the directory of the project with cd command;
3. Run the following commands:
```bash
mkdir build
cd build
cmake ..
cmake --build .
```

# Usage
The application can be used also in cli mode:
```
imageS-VD --cli <input-file-name> <output-file-name> [<singular-value-threshold>]
```
The input file and output file are treaten as images if their extensions is a [supported](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=imread#imread) image extension, or as decomposed images files if they are JSON, YAML, XML or BIN files. If the arguments don't have a supported extension, an error occurs.<br/>
If the output file is a decompose image file, the threshold is useless and can be omitted.

# License
This project is distributed under the BSD-3 license.
