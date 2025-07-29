
# Executable for create matrix exercise
add_executable (create_matrix src/create_matrix.cpp)
target_link_libraries (create_matrix PUBLIC opencv::opencv)

# Executable for change pixels exercise
add_executable (change_pixels src/change_pixels.cpp)
target_link_libraries (change_pixels PUBLIC opencv::opencv)

# Executables for load image exercises
add_executable (load_image_1 src/load_image_1.cpp)
target_link_libraries(load_image_1 PUBLIC opencv::opencv)

add_executable (load_image_2 src/load_image_2.cpp)
target_link_libraries(load_image_2 PUBLIC opencv::opencv)

add_executable (load_image_3 src/load_image_3.cpp)
target_link_libraries(load_image_3 PUBLIC opencv::opencv)
