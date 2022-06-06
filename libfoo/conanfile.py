import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools

class LibfooConan(ConanFile):
    name = "libfoo"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    exports = ['foo.c', 'foo.h', 'Makefile']

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make()

    def package(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make(target='install', args=[f"DESTDIR={self.package_folder}"])

