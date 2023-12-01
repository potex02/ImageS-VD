# ImageS-VD
ImageS-VD is a project developed as a part of a Bachelor's thesis in Computer Science and Technologies at the University of Basilicata.<br/>
The goal is the creation of a desktop application for image compression using the Singulat Value Decomposition (SVD).<br/>
The project is written in C++ and uses CMake as build system.

## Current status
The project is in a very early state of development and can be used only by command line for now.

## Dependecies
- OpenCV;
- Gtkmm (planned, not used yet).

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
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-opencv
# For 32-bit systems
pacman -S mingw-w64-i686-gcc mingw-w64-i686-cmake mingw-w64-i686-opencv
```
### Debian/Ubuntu
```bash
sudo apt update
sudo apt-get install g++ cmake libopencv-dev
```
### Fedora 
```bash
sudo dnf update
sudo dnf upgrade
sudo dnf install gcc-c++ cmake opencv-devel
```
### Arch linux
```bash
sudo pacman -Syu
sudo pacman -S gcc cmake opencv
```
### FreeBSD
```bash
sudo pkg update
sudo pkg install cmake opencv
```
### Mac OS
1. Install [Brew](https://brew.sh/) following the instruction of the official site;
2. Open a shell;
3. Run the following commands:
```bash
brew update
brew install gcc cmake opencv
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
```
imageS-VD <path-to-the-image-to-compress> <output-file-name> <singular-value-threshold>
```

# License
This project is distributed under the BSD-3 license.
