# syntax=docker/dockerfile:1

# Pick a base image to serve as the foundation for the other build stages in this file.
FROM ece350project2_base:latest as base

# Create a stage for building/compiling the application.
FROM base as build

# make a working directory for the app
WORKDIR /src

# copy all files for project into image
COPY ./start_433.sh /src

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

# configure libraries
RUN ldconfig

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser

# What the container should run when it is started.
ENTRYPOINT [ "/src/start_433.sh" ]
