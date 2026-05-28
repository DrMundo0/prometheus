cmake_minimum_required(VERSION 2.8)

# 项目名称
project(cpp)

aux_source_directory(. DIR_SRCS)
set(CMAKE_BUILD_TYPE "Debug")

# build target 放到target目录中
add_executable(target/a.out ${DIR_SRCS})
