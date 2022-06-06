from conans import ConanFile, AutoToolsBuildEnvironment, tools


class QuuxConan(ConanFile):
    name = "quux"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    requires = [("libfoo/1.0", "private")]
    
    exports = ['Makefile', 'quux.c']

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make()

    def package(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make(target='install', args=[f"DESTDIR={self.package_folder}"])
