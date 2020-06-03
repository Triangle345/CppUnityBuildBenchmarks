# CppUnityBuildBenchmarks
Tests the performance of a unity header only build vs a regular c++ build

A cpp unity build is a technique used to speed up release builds by building only a single compilation unit.
To create a compilation unit, one needs to include all the definitions into one cpp file and make sure each header is only included ONE time.

Since I really hate creating header files I decided to create a unity build benchmarks header file only unity source code vs regular header + cpp file source code.

This project contains one script called 'file_creator.py' which simply contains several loops that create many functions/files to build. file_creator.py exports these created files to src/headeronly and src/cpp.

Everything is built using cmake. 

The results for my machine: Windows 10x64 AMD Ryzen5 2600x

headerless unity build
5 s

regular cpp build
30 s

regular cpp incremental build for one compilation unit (one cpp file)
2 s

