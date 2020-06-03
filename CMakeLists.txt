cmake_minimum_required(VERSION 3.0.0)
project(UnityTest VERSION 0.1.0)


# uncomment one of these out for testing
file(GLOB_RECURSE ELLC_SOURCES src/headeronly/main.cpp)
#file(GLOB_RECURSE ELLC_SOURCES src/cpp/*.cpp)

add_executable(UnityTest ${ELLC_SOURCES})



target_compile_features(UnityTest PRIVATE cxx_std_17)

#uncomment one of these out for testing
#target_include_directories(UnityTest PRIVATE src/cpp)
target_include_directories(UnityTest PRIVATE src/headeronly)






    
    