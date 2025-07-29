cmake_minimum_required(VERSION 3.22 FATAL_ERROR)

add_definitions(-std=c++20)

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS, "${CXX_FLAGS}")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(camera_fusion)

find_package(OpenCV 4.11 REQUIRED)

add_subdirectory(Lesson_2-Autonomous_Vehicles_and_Computer_Vision/The_OpenCV_Library/OpenCV_exercises)