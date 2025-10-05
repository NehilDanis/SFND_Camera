# Executable for create matrix exercise
add_executable (compute_ttc_lidar src/compute_ttc_lidar.cpp src/structIO.cpp)
target_link_libraries (compute_ttc_lidar opencv::opencv)
