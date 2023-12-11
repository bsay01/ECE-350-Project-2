# syntax=docker/dockerfile:1

# Pick a base image to serve as the foundation for the other build stages in this file.
FROM ece350project2_base:latest as base

# Create a stage for building/compiling the application.
FROM base as build

# copy all files for project into image
COPY ./start_433.sh /src

WORKDIR /src/data
WORKDIR /src

# configure libraries
RUN ldconfig

# What the container should run when it is started.
CMD bash /src/start_433.sh
