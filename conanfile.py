from conans import ConanFile, CMake

class Package(ConanFile):
    name = "Project"
    version = "master"
    license = "MIT"
    url = "https://github.com/testcca/Project.git"
    description = "<Description of Project here>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"
    requires = (
        "Component1/%s@demo/testing" % version,
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*", dst="bin", src="bin")

    def package_info(self):
        self.cpp_info.libs = [ self.name ]

