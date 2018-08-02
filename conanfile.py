#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class WingetoptConan(ConanFile):
    name = "wingetopt"
    version = "0.95"
    homepage = "https://github.com/alex85k/wingetopt"
    url = "https://github.com/atolab/conan-wingetopt"
    description = "getopt library for Windows compilers"
    license = "MIT, BSD-2-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        source_url = "https://github.com/alex85k/wingetopt"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        del self.settings.compiler.libcxx

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder, keep_path=False)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
