# syntax=docker/dockerfile:1

# Pick a base image to serve as the foundation for the other build stages in this file.
FROM ubuntu:latest as base

# Create a stage for building/compiling the application.
FROM base as build

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install git
RUN apt-get -y install cmake
RUN apt-get -y install build-essential
RUN apt-get -y install libusb-1.0-0.dev
RUN apt-get -y install libtool
RUN apt-get -y install librtlsdr-dev
RUN apt-get -y install pkg-config
RUN apt-get -y install kmod
