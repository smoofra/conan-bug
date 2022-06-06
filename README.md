
Conan Bug Report
================


This is a bug report against conan version 1.48.1 


The Problem
-----------

[`cpp_info` is not being propagated correctly when using a private requirement in cross compile mode](https://github.com/conan-io/conan/issues/11402)


### To Reproduce

In this example libfoo is a static library, and quux is an executable that
requires it, using a private requirement. If I try to build quux in
cross-compile mode, libfoo's information disappears from quux's cpp_info and it
can no longer find foo.h


This works, as expected
```
conan create -pr ./Macos-armv8 libfoo
conan create -pr ./Macos-armv8 quux
```

But this does not work
```
conan create -pr:h ./Macos-armv8 -pr:b ./Macos-armv8 quux
```

output:
```
...
cc -O3 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX12.3.sdk -arch arm64 -DNDEBUG   quux.c -lfoo -o quux 
quux.c:3:10: fatal error: 'foo.h' file not found
```


Versions
--------

```
➜  ~/src/conan-bug git:(master) ✗ conan --version
Conan version 1.48.1

➜  ~/src/conan-bug git:(master) ✗ python --version
Python 3.9.12

➜  ~/src/conan-bug git:(master) ✗ sw_vers 
ProductName:	macOS
ProductVersion:	12.3.1
BuildVersion:	21E258
```

