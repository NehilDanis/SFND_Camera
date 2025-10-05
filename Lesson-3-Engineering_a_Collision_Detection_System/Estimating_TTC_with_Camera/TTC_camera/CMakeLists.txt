add_executable (compute_ttc_camera src/compute_ttc_camera.cpp src/structIO.cpp)
target_link_libraries (compute_ttc_camera opencv::opencv)
