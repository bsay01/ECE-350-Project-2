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

# make a working directory for the app
WORKDIR /src

# set up rtl-sdr
RUN git clone https://github.com/osmocom/rtl-sdr.git
#RUN su
#RUN rmmod --syslog dvb_usb_rtl28xxu
WORKDIR /src/rtl-sdr/build
RUN cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
RUN make install

# go back to main directory
WORKDIR /src

# set up rtl_433
RUN git clone https://github.com/merbanan/rtl_433.git
WORKDIR /src/rtl_433/build
RUN cmake ../
RUN make
RUN make install
