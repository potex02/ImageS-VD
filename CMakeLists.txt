cmake_minimum_required(VERSION 3.5)
project(imageS-VD)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
include_directories(
    includes/model
    includes/view
)
file(GLOB_RECURSE SOURCES src/*.cpp)
find_package(PkgConfig)
pkg_check_modules(GTKMM gtkmm-3.0)
find_package(OpenCV REQUIRED)
link_directories(${GTKMM_LIBRARY_DIRS})
include_directories(${GTKMM_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})
add_executable(${PROJECT_NAME} ${SOURCES})
link_directories(${GTKMM_LIBRARY_DIRS})
target_link_libraries(${PROJECT_NAME} ${GTKMM_LIBRARIES} ${OpenCV_LIBS})
