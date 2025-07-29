from conan import ConanFile
from conan.tools.cmake import cmake_layout


class SFND_Camera_Recipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("opencv/4.11.0")

    def layout(self):
        cmake_layout(self)