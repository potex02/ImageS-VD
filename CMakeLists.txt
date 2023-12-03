cmake_minimum_required(VERSION 3.5)
project( imageS-VD )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( ${PROJECT_NAME} main.cpp
    Compresser.h Compresser.cpp )
target_link_libraries( ${PROJECT_NAME} ${OpenCV_LIBS} )
