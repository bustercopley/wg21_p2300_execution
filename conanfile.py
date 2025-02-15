from conans import ConanFile, CMake, tools
import re
from os import path


class P2300Recipe(ConanFile):
    name = "P2300"
    description = "std::execution"
    author = "Michał Dominiak, Lewis Baker, Lee Howes, Kirk Shoop, Michael Garland, Eric Niebler, Bryce Adelstein Lelbach"
    topics = ("WG21", "concurrency")
    homepage = "https://github.com/brycelelbach/wg21_p2300_std_execution"
    url = "https://github.com/brycelelbach/wg21_p2300_std_execution"
    license = "Apache 2.0"
    settings = "compiler"  # Header only - compiler only used for flags
    tool_requires = "catch2/2.13.6"
    exports_sources = "include/*"
    generators = "cmake_find_package"

    def validate(self):
        tools.check_min_cppstd(self,"20")

    def set_version(self):
        # Get the version from the spec file
        content = tools.load(path.join(self.recipe_folder, "std_execution.bs"))
        rev = re.search(r"Revision: (\d+)", content).group(1).strip()
        self.version = f"0.{rev}.0"

    def package(self):
        self.copy("*.hpp")

    def package_info(self):
        # Make sure to add the correct flags for gcc
        if self.settings.compiler == "gcc":
            self.cpp_info.cxxflags = ["-fcoroutines", "-Wno-non-template-friend"]
